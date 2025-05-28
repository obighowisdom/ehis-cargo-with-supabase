from django.db import models
from .utils import create_new_ref_number
from .utils import customer_ref
from .utils import product_ref
from .utils import carrier_ref
# Create your models here.
from django.utils.text import slugify


class cons(models.Model):
    caption = models.CharField(max_length=200)
    true = models.CharField(max_length=200)
    trac_one = models.CharField(max_length=200)
    def __str__(self):
        return self.caption


# comment

class comment(models.Model):
    name = models.CharField(max_length=200)
    comments = models.CharField(max_length=1000)
    def __str__(self):
        return self.name

# location
class location(models.Model):
    status = models.CharField(max_length=200)
    previous_location = models.CharField(max_length=200)
    current_location = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    destination = models.CharField(max_length=200)
    delivery_date = models.CharField(max_length=200)
    map = models.CharField(max_length=1000)

    def __str__(self):
        return self.status


class location_two(models.Model):
    status = models.CharField(max_length=200)
    previous_location = models.CharField(max_length=200)
    current_location = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    destination = models.CharField(max_length=200)
    delivery_date = models.CharField(max_length=200)
    map = models.CharField(max_length=1000)

    def __str__(self):
        return self.status

class TrackDatas(models.Model):
    track_Number = models.CharField(
           max_length = 1000,
           blank=True,
           editable=False,
           unique=True,
           default=create_new_ref_number
      )
    ship_from = models.CharField(max_length=2000, null=False, blank=False)
    ship_to = models.CharField(max_length=200, null=False, blank=False)
    sender_email = models.CharField(max_length=200, null=False, blank=False)
    sender_phone = models.CharField(max_length=200, null=False, blank=False)
    sender_address = models.CharField(max_length=2000, null=False, blank=False)
    receiver_email = models.CharField(max_length=200, null=False, blank=False)
    receiver_phone = models.CharField(max_length=200, null=False, blank=False)
    receiver_address = models.CharField(max_length=2000, null=False, blank=False)
    customer_name = models.CharField(max_length=200, null=False, blank=False)
    customer_email = models.CharField(max_length=200, null=False, blank=False)
    customer_address = models.CharField(max_length=2000, null=False, blank=False)
    package = models.CharField(max_length=2000, null=False, blank=False)
    shipment_mode = models.CharField(max_length=200, null=False, blank=False)
    expected_delivery_date = models.CharField(max_length=200, null=False, blank=False)
    origin = models.CharField(max_length=200, null=False, blank=False)
    destination = models.CharField(max_length=200, null=False, blank=False)
    package_weight = models.CharField(max_length=200, null=False, blank=False)
    carrier = models.CharField(max_length=200, null=False, blank=False)
    carrier_number = models.CharField(max_length=20000, editable=False, default=carrier_ref)
    map = models.CharField(max_length=20000, null=True, blank=True)
    current_location = models.CharField(max_length=200, null=False, blank=False)
    product_id = models.CharField(max_length=13, null=False, blank=False, editable=False, default=product_ref)
    customer_ref = models.CharField(max_length=200, null=False, blank=False, editable=False, default=customer_ref)
    comment = models.CharField(max_length=20000, null=False, blank=False)
    status = models.CharField(max_length=200, null=False, blank=False)


    def __str__(self):
        return self.track_Number