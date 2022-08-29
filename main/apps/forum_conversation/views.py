from django.utils.functional import cached_property
from django.views.generic import ListView
from machina.core.db.models import get_model
from machina.core.loading import get_class

from main.apps.forum.enums import ForumKind
from main.apps.forum_category.models import ForumCategory

Post = get_model("forum_conversation", "Post")
Forum = get_model("forum", "Forum")
TopicForm = get_class("forum_conversation.forms", "TopicForm")

PermissionHandler = get_class("forum_permission.handler", "PermissionHandler")


class GroupsFeedListView(ListView):
    template_name = "forum_conversation/feed.html"
    context_object_name = "posts"

    def get_queryset(self):
        forums = self.request.forum_permission_handler.forum_list_filter(
            Forum.objects.exclude(kind=ForumKind.OPENFORUM),
            self.request.user,
        )
        print(forums)
        return (
            Post.objects.filter(topic__forum__in=forums).select_related("topic", "topic__forum").order_by("-created")
        )


class OpenForumsFeedListView(ListView):
    template_name = "forum_conversation/feed.html"
    context_object_name = "posts"

    def get_queryset(self):
        self.category_id = self.kwargs.get("category_id", None)
        return Post.openforums_objects.in_category(self.category_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["kind"] = ForumKind.OPENFORUM
        context["categories"] = self.category
        context["category_id"] = self.category_id

        return context

    @cached_property
    def category(self):
        return ForumCategory.objects.all()
