# Generated by Django 3.0.6 on 2020-05-23 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miembro', '0007_eps'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('fc', models.DateTimeField(auto_now_add=True)),
                ('fm', models.DateTimeField(auto_now=True)),
                ('uc', models.IntegerField(blank=True, editable=False, null=True)),
                ('um', models.IntegerField(blank=True, editable=False, null=True)),
                ('descripcion', models.CharField(help_text='Descripción de la ciudad', max_length=45, unique=True, verbose_name='Descripción ciudad')),
            ],
            options={
                'verbose_name': 'Ciudad',
                'verbose_name_plural': 'Ciudades',
            },
        ),
    ]
