# Generated by Django 2.1.2 on 2018-11-25 08:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('structure', '0005_customer_account_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer_account',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
