# Generated by Django 2.1.2 on 2018-11-29 10:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('structure', '0009_auto_20181129_1132'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='country',
            name='account_id',
        ),
        migrations.AddField(
            model_name='customer_account',
            name='clan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='structure.Clan'),
        ),
    ]
