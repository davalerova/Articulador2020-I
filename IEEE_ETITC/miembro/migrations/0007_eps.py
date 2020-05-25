# Generated by Django 3.0.6 on 2020-05-23 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miembro', '0006_auto_20200523_2138'),
    ]

    operations = [
        migrations.CreateModel(
            name='Eps',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('fc', models.DateTimeField(auto_now_add=True)),
                ('fm', models.DateTimeField(auto_now=True)),
                ('uc', models.IntegerField(blank=True, editable=False, null=True)),
                ('um', models.IntegerField(blank=True, editable=False, null=True)),
                ('descripcion', models.CharField(help_text='Descripción de la EPS', max_length=45, unique=True, verbose_name='Descripción EPS')),
            ],
            options={
                'verbose_name': 'EPS',
                'verbose_name_plural': "EPS's",
            },
        ),
    ]