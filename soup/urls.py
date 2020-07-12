
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls import url,static
from django.views.generic import TemplateView
from buti import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
     url(r'^main', views.obj, name='obj'),
    url(r'^extract', views.main, name='extract'),
    #url(r'^home/', views.crawl, name='crawl'),
    # url(r'^soup', views.soup, name='soup'),
    # url(r'^trans', views.trans, name='trans'),
    # url(r'^newput', views.put, name='put'),
    # url(r'^put/index',views.te,name='test'),
]
# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]
