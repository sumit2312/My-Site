#My-Site
Use **django-tinymce** (A Django application that contains a widget to render a form field as a TinyMCE editor.)
#Installation
1. Install django-tinymce
> $ pip install django-tinymce
2.Add tinymce to INSTALLED_APPS in settings.py
> INSTALLED_APPS = (
    ...
    'tinymce',
    ...
)
3.Add tinymce.urls to urls.py
> urlpatterns = patterns('',
    ...
    path('tinymce/',include('tinymce.urls')),
    ...
)
