# django_with_machina
Django project using django-machina as lib

# Translation
1. add your tags in the templates : `{% translate %}` or `{% blocktranslate %}`
2. create a message file : `django-admin makemessages -l fr` where `fr` is the locale name for the message file you want to create,
3. update message files in `./DJANGO_WITH_MACHINA/{PROJECT_NAME}/locale/{LOCALE}/LC_MESSAGES/*.po`
4. compile your message files : `django-admin compilemessages`

# Setup
## env vars
- copy `.envrc.template` into your own `.envrc`, then customize it

## create your env
- check your `pyproject.toml`
- exec `make init`
- migrate and populate your db `make migrate; make populate_db`

# Machina usages
## access apps in shell
```
    make console
    from machina.apps.forum_member.models import ForumProfile
    …
```

## migration files
- your independant apps : stored in `./DJANGO_WITH_MACHINA/main/apps/{APP_NAME}/migrations`
- your overridden machina apps : stored with poetry in `/home/{$USER}/.cache/pypoetry/virtualenvs/django-with-machina-{$ID}-py3.10/lib/{PYTHON_VERSION}/site-packages/machina/apps/{APP_NAME}/migrations/`

## how to override a model class
call "abstracted model", then override it

```
from machina.apps.forum_conversation.abstract_models import AbstractPost

class Post(AbstractPost):
    field = models.…
```

## how to call model class (overriden or not)
use the method `get_model` to get the right version of the model, first the overriden one, then the default machina one.
```
from machina.core.db.models import get_model
Post = get_model("forum_conversation", "Post")
```

## how to call overriden class
### in urls.py
```
from machina.core.loading import get_class
forum_view = get_class("forum.views", "ForumView")
urlpatterns = [
    path(
        "<str:slug>-<int:pk>/",
        forum_view.as_view(),
        name="group",
    ),]
```

### in admin.py
```
from machina.core.loading import get_class

ForumAdmin = get_class("forum.admin", "ForumAdmin")
ForumAdmin.fieldsets += (("Privacy", {"fields": ("kind", "moderators_group", "contributors_group")}),)
```


# Docs
* [django-machina on readthedocs.io](https://django-machina.readthedocs.io/en/stable/)
* [django-machina on github](https://github.com/ellmetha/django-machina/)