# Generated by Django 2.1.2 on 2018-12-07 12:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('structure', '0016_user_settings'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_settings',
            name='world_by_default',
        ),
        migrations.AddField(
            model_name='user_settings',
            name='customer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='user_settings',
            name='selected_world',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='structure.World_version'),
        ),
    ]
