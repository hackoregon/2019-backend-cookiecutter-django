from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from rest_framework_swagger.views import get_swagger_view

router = DefaultRouter()

schema_view = get_swagger_view(title='Hack Oregon {{cookiecutter.hack_oregon_team}} {{cookiecutter.year}} API')


urlpatterns = [
    url(r'^{{ cookiecutter.hack_oregon_team|lower|replace(' ', '-') }}/schema/', schema_view),
    url(r'^{{ cookiecutter.hack_oregon_team|lower|replace(' ', '-') }}/{{cookiecutter.python_subpackage}}/', include('{{cookiecutter.python_package_namespace}}.{{cookiecutter.python_subpackage}}.urls')),
]