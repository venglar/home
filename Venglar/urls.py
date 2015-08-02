from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', TemplateView.as_view(template_name="home.html"), name='home'),
    url(r'^portfolio/$', TemplateView.as_view(template_name="portfolio.html"), name='portfolio'),
    url(r'^contact/$', TemplateView.as_view(template_name="contact.html"), name='contact')
]
