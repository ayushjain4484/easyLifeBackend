# Generated by Django 5.0.4 on 2024-04-14 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0004_alter_subscription_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='renewal_type',
            field=models.CharField(default='monthly', max_length=255),
        ),
    ]