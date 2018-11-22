# Generated by Django 2.1.2 on 2018-11-22 14:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
        ('structure', '0004_customer_account'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer_account',
            name='customer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='customer.Customer'),
            preserve_default=False,
        ),
    ]