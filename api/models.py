from django.db import models

class Event(models.Model):
    """This class represents the event model"""
    id = models.CharField(max_length=12, primary_key=True) # don't want to assume it's an integer as it wasn't validated as such in the API documentation
    name = models.CharField(max_length=255, blank=False)
    description = models.TextField()
    url = models.URLField()
    vanity_url = models.URLField()
    start = models.DateTimeField()
    end = models.DateTimeField()
    org_id = models.CharField(max_length=12) # don't want to assume it's an integer as it wasn't validated as such in the API documentation
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    date_published = models.DateTimeField()
    status = models.CharField(
        max_length=9,
        choices=[('draft','draft'),('live','live'),('started','started'),('ended','ended'),('completed','completed'),('cancelled','cancelled')]
        )
    currency = models.CharField(max_length=3)
    online_event = models.BooleanField()
    hide_start_date = models.BooleanField()
    hide_end_date = models.BooleanField()
    """ Not including other expanision or private fields"""

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name)
