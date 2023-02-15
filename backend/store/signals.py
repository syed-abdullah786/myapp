from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Timeline, Order

@receiver(post_save, sender=Order)
def timeline(sender, instance, created, **kwargs):
    # Check if a new instance of Table1 is created
    print('signal catched')
    if created:
        # Save the CRUD operation in Table2
        Timeline.objects.create(operation='create', table1=instance)