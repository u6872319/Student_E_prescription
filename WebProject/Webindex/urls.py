from django.urls import path
from django.conf.urls import url
from . import views
from . import search,Post_method

urlpatterns = [
    path('', views.index, name='index'),
    path('heh',views.y_,name="y"),  ## url to Another page

    path('eh', views.show, name="yq"),
    url(r'^show$', views.show),
    url(r'^search-form/$', search.search_form),
    url(r'^search/$', search.search),
    url(r'^search-post/$', Post_method.search_post),
    url(r'^search-post/$', Post_method.runoob),
    url(r'^json1/$', Post_method.Post_json),

]