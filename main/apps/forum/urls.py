from django.urls import path
from machina.core.loading import get_class

app_name = "forums"

forum_view = get_class("forum.views", "ForumView")
group_profiles_list_view = get_class("forum.views", "GroupProfilesListView")

urlpatterns = [
    path(
        "<str:slug>-<int:pk>/",
        forum_view.as_view(),
        name="group",
    ),
    path(
        "<str:slug>-<int:pk>/members/",
        group_profiles_list_view.as_view(),
        name="group_members",
    ),
]
