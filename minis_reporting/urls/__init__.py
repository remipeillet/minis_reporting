from django.conf import settings
from django.conf.urls import re_path, include
from django.contrib import admin


__all__ = [
    'urlpatterns',
]

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^autocomplete/', include('minis_reporting.urls.autocomplete',
            namespace='autocomplete')),
    re_path(r'^restapi/', include('minis_reporting.urls.restapi',
                                  namespace='restapi')),
]

if settings.ADMIN_DEBUG_TOOLBAR and 'debug_toolbar' in settings.INSTALLED_APPS:
    import debug_toolbar
    urlpatterns.append(
        re_path(r'^djdt/', include(debug_toolbar.urls)))

if settings.DEBUG:
    from django.views.static import serve as static_serve
    urlpatterns.append(
        re_path(r'^__media__/(?P<path>.*)$',
                static_serve, {
                    'document_root': settings.MEDIA_ROOT,
                    'show_indexes': True
                })
    )
