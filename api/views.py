from api.models import Event
from api.serializers import EventSerializer
from api.validations import event_query_schema
from rest_framework import (filters)
from filters.mixins import (FiltersMixin)
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse

# Create your views here.
class EventList(FiltersMixin, generics.ListAPIView):
    serializer_class = EventSerializer
    queryset = Event.objects.all()
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = ('id', 'name', 'update_date')
    ordering = ('id',)

    #mapping of query_params to db_columns
    filter_mappings = {
        'name': 'name__icontains',
        'org_id': 'org_id',
        'start':  'start__gte',
        'cost': 'min_price__gte',
    }

    # validate query_params
    filter_validation_schema = event_query_schema

class EventDetail(generics.UpdateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'events': reverse('event-list', request=request, format=format),
        'event-detail': reverse('event-detail', kwargs={'pk':'1234'}, request=request, format=format)
    })
