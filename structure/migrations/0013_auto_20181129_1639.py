# Generated by Django 2.1.2 on 2018-11-29 14:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('structure', '0012_auto_20181129_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer_account',
            name='clan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='structure.Clan'),
        ),
        migrations.AlterField(
            model_name='customer_account',
            name='customer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='customer_account',
            name='world',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='structure.World_version'),
        ),
    ]