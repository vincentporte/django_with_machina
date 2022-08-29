from machina.apps.forum.apps import ForumAppConfig as BaseForumAppConfig


class ForumAppConfig(BaseForumAppConfig):
    name = "main.apps.forum"
    default = True
