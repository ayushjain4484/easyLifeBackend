from django.core.management.base import BaseCommand
from django.utils import timezone
import datetime
from subscriptions.models import Subscription  # Make sure this path matches your actual model import


class Command(BaseCommand):
    help = 'Updates the renewal dates for subscriptions'

    def handle(self, *args, **options):
        today = timezone.now().date()
        subscriptions = Subscription.objects.filter(renews__lt=today, is_active=True)

        for subscription in subscriptions:
            if subscription.renewal_type == 'monthly':
                next_month = subscription.renews + datetime.timedelta(days=30)  # rough approximation
            elif subscription.renewal_type == 'first_of_month':
                if subscription.renews.month == 12:
                    next_month = datetime.date(subscription.renews.year + 1, 1, 1)
                else:
                    next_month = datetime.date(subscription.renews.year, subscription.renews.month + 1, 1)

            subscription.renews = next_month
            subscription.save()

            self.stdout.write(self.style.SUCCESS(f'Successfully updated renewal date for {subscription.service}'))

