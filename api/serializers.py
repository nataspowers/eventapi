from rest_framework import serializers
from api.models import Event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id','name','description','url','vanity_url','start','end','org_id','date_created','date_modified',
                  'date_published','status','currency','online_event','hide_start_date','hide_end_date','min_price','max_price']
