import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import redirect
from django.utils.functional import cached_property
from django.views.generic import DetailView, ListView

from changes.forms import ActivitiesViewForm
from changes.models import Change
from changes.utils import CustomHtmlHTML
from core.constants import PRODUCT_SEPARATOR
from projects.models import Project


class ActivityPaginator(Paginator):
    """
    A custom paginator used to improve the performance of the changes
    list. The count number is much larger than expected, so Django doesn't
    have to compute it.
    See: https://pganalyze.com/blog/pagination-django-postgres#pagination-in-django-option-1--removing-the-count-query
    """

    @cached_property
    def count(self):
        return 9999999999


class ChangeListView(LoginRequiredMixin, ListView):
    model = Change
    context_object_name = "changes"
    template_name = "changes/change_list.html"
    paginate_by = 20
    paginator_class = ActivityPaginator
    form_class = ActivitiesViewForm

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("cves")
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        query = Change.objects
        query = query.select_related("cve").prefetch_related("events")

        # Filter on user subscriptions
        if self.request.user.settings["activities_view"] == "subscriptions":
            vendors = [v["vendor_name"] for v in self.request.user.get_raw_vendors()]
            vendors.extend(
                [
                    f"{product['vendor_name']}{PRODUCT_SEPARATOR}{product['product_name']}"
                    for product in self.request.user.get_raw_products()
                ]
            )

            if vendors:
                query = query.filter(cve__vendors__has_any_keys=vendors)

        return query.order_by("-created_at")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Add the user tags
        context["tags"] = self.request.user.tags.all()

        # Add the projects
        context["projects"] = self.request.user.projects.all().order_by("-updated_at")

        # Add the view form
        view = self.request.user.settings["activities_view"]
        context["form"] = ActivitiesViewForm(initial={"view": view})
        return context

    def post(self, request, *args, **kwargs):
        form = ActivitiesViewForm(request.POST)
        if form.is_valid():
            self.request.user.settings = {
                **self.request.user.settings,
                "activities_view": form.cleaned_data["view"],
            }
            self.request.user.save()
        return redirect("home")


class ChangeDetailView(DetailView):
    model = Change
    template_name = "changes/change_detail.html"

    def get_object(self):
        change_id = self.kwargs["id"]
        cve_id = self.kwargs["cve_id"]

        change = Change.objects.filter(cve__cve_id=cve_id).filter(id=change_id).first()
        if not change:
            raise Http404(f"Change {change_id} not found for {cve_id}")
        return change

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        change = context["change"]

        previous = (
            Change.objects.filter(created_at__lt=change.created_at)
            .filter(cve=change.cve)
            .order_by("-created_at")
            .first()
        )

        previous_json = {}
        if previous:
            previous_json = previous.json

        differ = CustomHtmlHTML()
        context["diff"] = differ.make_table(
            fromlines=json.dumps(previous_json, sort_keys=True, indent=2).split("\n"),
            tolines=json.dumps(change.json, sort_keys=True, indent=2).split("\n"),
            context=True,
        )
        return context
