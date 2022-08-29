from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from machina.core.db.models import get_model
from machina.core.loading import get_class

PermissionHandler = get_class("forum_permission.handler", "PermissionHandler")

ForumProfile = get_model("forum_member", "ForumProfile")
Forum = get_model("forum", "Forum")


class GroupProfilesListView(ListView):
    template_name = "forum/group_profiles_list.html"
    context_object_name = "profiles"
    group_pk_url_kwarg = "pk"
    group_slug_url_kwarg = "slug"

    def get_queryset(self):
        forum = get_object_or_404(
            Forum, pk=self.kwargs[self.group_pk_url_kwarg], slug=self.kwargs[self.group_slug_url_kwarg]
        )
        return (forum.moderators_group.user_set.all() | forum.contributors_group.user_set.all()).values(
            "first_name", "last_name", "groups", "groups__moderators_group", "groups__contributors_group"
        )
