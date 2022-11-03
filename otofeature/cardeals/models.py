from django.db import models
from scrapper import all_deals as deals

# Create your models here.

class RoccoDeal(models.Model):

    price = deals.price
    currency = deals.currency
    year = deals.year
    mileage = deals.mileage
    add_date = deals.add_date