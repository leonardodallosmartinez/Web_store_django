# Generated by Django 3.2.6 on 2021-09-21 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_app_servicios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicio',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='servicio',
            name='updated',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
