from django.db import models

class Event(models.Model):
    """This class represents the event model"""
    id = models.CharField(max_length=12, primary_key=True) # don't want to assume it's an integer as it wasn't validated as such in the API documentation
    name = models.CharField(max_length=255, blank=False)
    description = models.TextField(null=True, blank=True)
    url = models.URLField()
    vanity_url = models.URLField(null=True, blank=True)
    start = models.DateTimeField()
    end = models.DateTimeField()
    org_id = models.CharField(max_length=12) # don't want to assume it's an integer as it wasn't validated as such in the API documentation
    date_created = models.DateTimeField()
    date_modified = models.DateTimeField()
    date_published = models.DateTimeField(null=True, blank=True)
    status = models.CharField(
        max_length=9,
        choices=[('draft','draft'),('live','live'),('started','started'),('ended','ended'),('completed','completed'),('cancelled','cancelled')]
        )
    currency = models.CharField(max_length=3)
    online_event = models.BooleanField()
    hide_start_date = models.BooleanField()
    hide_end_date = models.BooleanField()
    min_price = models.DecimalField(max_digits=7, decimal_places=2)
    max_price = models.DecimalField(max_digits=7, decimal_places=2)
    """ Not including other expanision or private fields"""

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "({}) {} starting at {}".format(self.id, self.name, self.start)
