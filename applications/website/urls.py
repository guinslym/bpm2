from django.conf.urls import url

#from .views import WebsiteListView, WebsiteDetailView
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^about/', TemplateView.as_view(template_name="about.html")),
    url(r'^$', TemplateView.as_view(template_name="about.html")),
    #url(r'^$', WebsitesListView.as_view(), name='websites_list'),
    #url(r'^(?P<slug>[-\w]+)/$', WebsitesDetailView.as_view(), name='websites_detail'),
]
