from django.urls import path
from machina.core.loading import get_class

topic_subscription_list_view = get_class("forum_member.views", "TopicSubscriptionListView")
profiles_list_view = get_class("forum_member.views", "ProfilesListView")
profile_groups_list_view = get_class("forum_member.views", "ProfileGroupsListView")
user_posts_list = get_class("forum_member.views", "UserPostsView")
forum_profile_detail_view = get_class("forum_member.views", "ForumProfileDetailView")

app_name = "members"

urlpatterns = [
    path("", profiles_list_view.as_view(), name="profiles"),
    path("<str:pk>/", forum_profile_detail_view.as_view(), name="profile"),
    path("<str:pk>/posts/", user_posts_list.as_view(), name="profile_posts"),
    path("me/subscriptions/", topic_subscription_list_view.as_view(), name="profile_subscriptions"),
    path("<str:pk>/groups/", profile_groups_list_view.as_view(), name="profile_groups"),
]
