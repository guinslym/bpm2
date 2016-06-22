from django.conf.urls import url
from django.views.generic import TemplateView

urlpatterns = [
    #url(r'^$', admin.site.urls),
    url(r'^about/', TemplateView.as_view(template_name="about.html")),
    url(r'^about/', TemplateView.as_view(template_name="about.html")),
]
