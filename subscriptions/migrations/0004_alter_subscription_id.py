# Generated by Django 5.0.4 on 2024-04-14 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0003_alter_subscription_currency_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
