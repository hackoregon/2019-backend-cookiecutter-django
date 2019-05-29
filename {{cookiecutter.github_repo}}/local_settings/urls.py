from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from rest_framework_swagger.views import get_swagger_view
from rest_framework.documentation import include_docs_urls

router = DefaultRouter()

api_title = 'Hack Oregon {{cookiecutter.hack_oregon_team}} {{cookiecutter.year}} API'

schema_view = get_swagger_view(title=api_title)


urlpatterns = [
    url(r'^{{ cookiecutter.hack_oregon_team|lower|replace(' ', '-') }}/schema/', schema_view),
    url(r'^{{ cookiecutter.hack_oregon_team|lower|replace(' ', '-') }}/{{cookiecutter.python_subpackage}}/', include('{{cookiecutter.python_package_namespace}}.{{cookiecutter.python_subpackage}}.urls')),
    url(r'^{{ cookiecutter.hack_oregon_team|lower|replace(' ', '-') }}/docs/', include_docs_urls(title=api_title)),
]
