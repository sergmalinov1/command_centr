# Generated by Django 2.1.2 on 2018-11-25 10:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('structure', '0006_auto_20181125_1044'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('world', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='structure.World_version')),
            ],
        ),
        migrations.AddField(
            model_name='clan',
            name='country',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='structure.Country'),
        ),
    ]