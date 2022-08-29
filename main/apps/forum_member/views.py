from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from machina.core.db.models import get_model
from machina.core.loading import get_class

ForumProfile = get_model("forum_member", "ForumProfile")
Forum = get_model("forum", "Forum")

PermissionRequiredMixin = get_class("forum_permission.viewmixins", "PermissionRequiredMixin")


class ProfilesListView(ListView):
    model = ForumProfile
    template_name = "forum_member/profiles.html"
    context_object_name = "forum_profiles"

    def get_context_data(self, **kwargs):

        context = super(ProfilesListView, self).get_context_data(**kwargs)
        context["MEDIA_URL"] = settings.MEDIA_URL

        return context


class ProfileGroupsListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    template_name = "forum_member/profile_groups_list.html"
    context_object_name = "groups"
    user_pk_url_kwarg = "pk"

    def get_queryset(self):
        user_model = get_user_model()
        user = get_object_or_404(user_model, pk=self.kwargs[self.user_pk_url_kwarg])
        return (Forum.objects.filter(Q(contributors_group__user=user) | Q(moderators_group__user=user))).distinct()
