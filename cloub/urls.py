from django.conf.urls import url, include
from .restviews import Euipment_class_set


equipmentclasses_detail = Euipment_class_set.as_view({
	'get':'retrieve'
})


urlpatterns = [
	url(r'^equipmentclasses/$', Euipment_class_set.as_view(
			{'get':'list'}
			) ),
	url(r'^equipmentclasses/(?P<pk>[0-9]+)/$', equipmentclasses_detail)
]