from django.conf.urls import include, url
from django.contrib import admin

from photos.views import PhotoView
from feedback.views import FeedbackView

urlpatterns = [
    url(r'^$', PhotoView.as_view(), name="home"),
    url(r'^feedback/$', FeedbackView.as_view(), name="feedback"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^cloub/', include('cloub.urls', namespace='cloub')),

]
