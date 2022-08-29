from django.urls import path
from machina.core.loading import get_class

groups_feed_list_view = get_class("forum_conversation.views", "GroupsFeedListView")
openforums_feed_list_view = get_class("forum_conversation.views", "OpenForumsFeedListView")

app_name = "conversations"

urlpatterns = [
    path(
        "groups/",
        groups_feed_list_view.as_view(),
        name="groups",
    ),
    path("openforums/", openforums_feed_list_view.as_view(), name="openforums"),
    path("openforums/category/<int:category_id>", openforums_feed_list_view.as_view(), name="openforums_category"),
]
