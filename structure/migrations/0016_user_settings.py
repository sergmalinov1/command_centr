# Generated by Django 2.1.2 on 2018-12-07 12:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('structure', '0015_country_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_settings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('world_by_default', models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='structure.World_version')),
            ],
        ),
    ]
