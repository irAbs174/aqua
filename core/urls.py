'''DEV : #ABS174'''

from wagtail.documents import urls as wagtaildocs_urls
from wagtail.admin import urls as wagtailadmin_urls
from django.urls import path, re_path, include
from django.conf.urls.static import static
from wagtail import urls as wagtail_urls
from django.contrib import admin
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cms/', include(wagtailadmin_urls)),
    path('documents/', include(wagtaildocs_urls)),

    path('', include(wagtail_urls)),
]

urlpatterns = [
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)