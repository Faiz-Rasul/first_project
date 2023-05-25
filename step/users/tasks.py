from datetime import datetime
from django.utils import timezone
from .models import Fees




#@shared_task
def add_monthly_fee():
    today = timezone.now().date()
    if today.day == 1:
        fee = Fees.objects.first()
        fee.monthly_fees = fee.monthly_fees + 2000
        fee.save()

