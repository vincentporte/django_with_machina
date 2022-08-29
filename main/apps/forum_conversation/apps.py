from machina.apps.forum_conversation.apps import (
    ForumConversationAppConfig as BaseForumConversationAppConfig,
)


class ForumConversationAppConfig(BaseForumConversationAppConfig):
    name = "main.apps.forum_conversation"
    default = True
