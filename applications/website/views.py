from django.shortcuts import render
from django.shortcuts import get_object_or_404

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.base import RedirectView
from django.utils import timezone

from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.template import Context

#from .models import website404

import logging
logger = logging.getLogger(__name__)
logger.info('On WebsitesListView')
print('hello')

class WebsiteListView(ListView):

    model = website404
    template_name = "websites_list.html"
    ordering = '-created'
    paginate_by=3
    logger.info('On WebsitesListView')

    def get_context_data(self, **kwargs):
        logger.info('On WebsitesListView')
        print(self.request.META['REMOTE_ADDR'])
        context = super(WebsitesListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

def handler404(request):
    response = render(request, 'page_not_found.html')
    logger.info('Error page not found 404')
    response.status_code = 404
    return response

def handler500(request):
    response = render(request, 'server_error.html')
    logger.info('Error page not found 500')
    response.status_code = 500
    return response
