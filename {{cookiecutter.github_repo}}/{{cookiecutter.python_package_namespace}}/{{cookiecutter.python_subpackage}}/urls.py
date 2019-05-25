from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view
from rest_framework_swagger.views import get_swagger_view

router = DefaultRouter()

urlpatterns = [
    url(r'^/', include(router.urls)),
]
