from machina.core.db.models import get_model
from machina.core.loading import get_class

Forum = get_model("forum", "Forum")
ForumAdmin = get_class("forum.admin", "ForumAdmin")

ForumAdmin.fieldsets += (("Privacy", {"fields": ("kind", "moderators_group", "contributors_group")}),)
