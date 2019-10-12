from django.db import migrations, models, transaction
from api.models import Event
from datetime import datetime, timedelta
from dateutil.tz import gettz
import requests
import pytz
from requests_toolbelt.utils import dump

page_count = 3

def save_events(events):
    for e in events:
        # deal with some events not having a published date
        if 'published' in e:
            published = pytz.utc.localize(datetime.strptime(e['published'],'%Y-%m-%dT%H:%M:%SZ'))
        else:
            published = None
        event = Event(
            id = e['id'],
            name = e['name']['text'],
            description = e['description']['text'],
            url = e['url'],
            start = datetime.strptime(e['start']['utc'],'%Y-%m-%dT%H:%M:%SZ').astimezone(gettz(e['start']['timezone'])),
            end = datetime.strptime(e['end']['utc'],'%Y-%m-%dT%H:%M:%SZ').astimezone(gettz(e['end']['timezone'])),
            org_id = e['organization_id'],
            date_created = pytz.utc.localize(datetime.strptime(e['created'],'%Y-%m-%dT%H:%M:%SZ')),
            date_modified = pytz.utc.localize(datetime.strptime(e['changed'],'%Y-%m-%dT%H:%M:%SZ')),
            date_published = published,
            status = e['status'],
            currency = e['currency'],
            online_event = e['online_event'],
            hide_start_date = e['hide_start_date'],
            hide_end_date = e['hide_end_date'],
            min_price = e['ticket_availability']['minimum_ticket_price']['major_value'],
            max_price = e['ticket_availability']['maximum_ticket_price']['major_value']
        )
        with transaction.atomic():
            event.save()


def fetch_events(apps, schema_editor):
    end_date = (datetime.now()+timedelta(weeks=3)).strftime("%Y-%m-%dT%H:%M:%SZ")
    headers = {'Authorization':'Bearer 4GQQFB6MUA5Y2RNBIQ55','Accept-Encoding':'application/json'}
    params = {
        'start_date.keyword':'today',
        'start_date.range_end':end_date,
        'price':'paid',
        'expand':'ticket_availability'
    }
    url = 'https://www.eventbriteapi.com/v3/events/search'
    page = 1
    while page < page_count :
        r = requests.get(url,params=params,headers=headers,timeout=60)
        try:
            events = r.json()["events"]
        except:
            data = dump.dump_all(r)
            print(data.decode('utf-8'))
            exit()
        save_events(events)
        page += 1
        params['page'] = page


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20191012_0347'),
    ]

    operations = [
        migrations.RunPython(fetch_events),
    ]
