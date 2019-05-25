from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view
from rest_framework_swagger.views import get_swagger_view

router = DefaultRouter()


#schema view
schema_view = get_swagger_view(title='{{cookiecutter.hack_oregon_team}} {{cookiecutter.year}} API')

urlpatterns = [
    url(r'^schema/', schema_view),
    url(r'^{{cookiecutter.python_subpackage}}/', include(router.urls)),
]
