from django_cron import CronJobBase, Schedule
from django.core.management import call_command


class RenewalCronJob(CronJobBase):
    # Running once a day
    RUN_AT_TIMES = ['00:00']  # Set the time to midnight

    schedule = Schedule(run_at_times=RUN_AT_TIMES)
    code = 'subscriptions.renewal_cron_job'  # an identifier for this job

    def do(self):
        call_command('update_renewals')
        self.stdout.write("Ran renewal update command.")



#   */5 * * * * /path/to/your/virtualenv/bin/python /path/to/your/manage.py runcrons >> /path/to/cron.log 2>&1
#   python manage.py update_renewals