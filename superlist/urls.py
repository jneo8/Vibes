from django.conf.urls import url
from . import views
app_name = 'superlist'

urlpatterns = [
    # /superlist/
    # /show nothing but homepage
    url(r'^$', views.home_page, name='home'),
    # /superlist/list/new
    # add new list
    url(r'^new$', views.new_list, name='new_list'),
    # /superlist/list/77
    # show special list
    url(r'^(\d+)/$', views.view_list, name='view_list'),
]
