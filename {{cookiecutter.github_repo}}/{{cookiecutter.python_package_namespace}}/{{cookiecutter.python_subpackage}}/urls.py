from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

## We will be using URLPath Versioning:

### add the appropriate versiong keywords to your url paths: ie r'^(?P<version>(v1|v2))/stops/$' for version 1 and 2
urlpatterns = [
    url(r'^', include(router.urls)),
]
