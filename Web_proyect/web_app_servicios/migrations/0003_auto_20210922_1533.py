# Generated by Django 3.2.6 on 2021-09-22 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_app_servicios', '0002_auto_20210921_1711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicio',
            name='imagen',
            field=models.ImageField(upload_to='servicios'),
        ),
        migrations.AlterField(
            model_name='servicio',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
