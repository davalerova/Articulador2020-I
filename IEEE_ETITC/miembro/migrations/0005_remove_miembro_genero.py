# Generated by Django 3.0.6 on 2020-05-23 21:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('miembro', '0004_auto_20200523_2120'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='miembro',
            name='genero',
        ),
    ]
