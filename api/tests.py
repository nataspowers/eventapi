from django.test import TestCase
from django.core import serializers
from rest_framework.test import APIClient
from rest_framework import status
from rest_framework.reverse import reverse
from api.models import Event
from datetime import datetime, date
from json import dumps
from urllib import parse
import pytz

# Create your tests here.

def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""

    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    raise TypeError ("Type %s not serializable" % type(obj))

def createTestEvent():
    e = Event(
        id = "1234",
        name = "Test Event",
        description = "Test Description - isn't it long? No? Better? lorium ipsum?",
        url = "http://notarealevent.com/1234",
        vanity_url = "http://iamsupercool.com/1234",
        start = datetime.strptime("2019-10-13 10:00:00","%Y-%m-%d %H:%M:%S").astimezone(pytz.utc),
        end = datetime.strptime("2019-10-13 12:00:00","%Y-%m-%d %H:%M:%S").astimezone(pytz.utc),
        org_id = "1234",
        date_created = datetime.now(pytz.utc),
        date_modified = datetime.now(pytz.utc),
        date_published = datetime.now(pytz.utc),
        status = "live",
        currency = "USD",
        online_event = True,
        hide_start_date = False,
        hide_end_date = False,
        max_price = 10.32,
        min_price = 7.34,
    )
    return e

class ModelTestCase(TestCase):
    """This class defines the test suite for the event model."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.event = createTestEvent()

    def test_model_can_create_a_bucketlist(self):
        """Test the bucketlist model can create a bucketlist."""
        old_count = Event.objects.count()
        self.event.save()
        new_count = Event.objects.count()
        self.assertNotEqual(old_count, new_count)

class ViewTestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        self.event = createTestEvent()
        self.event.save()

    def test_api_can_get_an_eventlist(self):
        """Test the api can get an event list."""
        events = Event.objects.all()
        qp = {'name':self.event.name, 'org_id':self.event.org_id, 'start':self.event.start}
        url = reverse('event-list') + '?' + parse.urlencode(qp)
        res = self.client.get(url, format="json")
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        #self.assertContains(events, response.data)

    def test_api_can_patch_event(self):
        """Test the api can patch a given event."""
        change_event = {'name': 'Something new'}
        res = self.client.patch(
            reverse('event-detail', kwargs={'pk': self.event.id}),
                    change_event, format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_update_event(self):
        """Test the api can update a given event."""
        updatedEvent = createTestEvent()
        updatedEvent.max_price = 99.99
        updatedEvent.__dict__.__delitem__('_state') #remove the _state item, as we don't need that for the JSON request
        data = dumps(updatedEvent.__dict__, default=json_serial)
        res = self.client.put(
            reverse('event-detail', kwargs={'pk': self.event.id}),
                    updatedEvent.__dict__, format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data["max_price"], str(updatedEvent.max_price))
