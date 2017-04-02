from django.conf.urls import patterns, include, url
from maiagogo import views

urlpatterns = patterns('',

url(r'^post_list/', 'maiagogo.views.post_list', name='post_list'),
url(r'^post/(?P<pk>\d+)/', 'maiagogo.views.post_detail', name='post_detail'),
url(r'^post/new/', 'maiagogo.views.post_new', name='post_new'),
url(r'^post/(?P<pk>\d+)/edit/$', 'maiagogo.views.post_edit', name='post_edit'),
url(r'^register/', 'maiagogo.views.register', name='register'),
url(r'^user_login/', 'maiagogo.views.user_login', name='user_login'),
url(r'^user_logout/', 'maiagogo.views.user_logout', name='user_logout'),
url(r'^Home/', 'maiagogo.views.index', name='index'),
url(r'^category/(?P<category_name_url>\w+)/', 'maiagogo.views.category', name='category'),
url(r'^add_category/', 'maiagogo.views.add_category', name='add_category'),
url(r'^category/(?P<category_name_url>\w+)/add_page/', 'maiagogo.views.add_page', name='add_page'),
url(r'^profile/', 'maiagogo.views.profile', name='profile'),
url(r'^goto/', 'maiagogo.views.track_url', name='track_url'),
 url(r'^like_category/', 'maiagogo.views.like_category', name='like_category'),
)



