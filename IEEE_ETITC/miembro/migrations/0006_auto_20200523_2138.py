# Generated by Django 3.0.6 on 2020-05-23 21:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('miembro', '0005_remove_miembro_genero'),
    ]

    operations = [
        migrations.AddField(
            model_name='miembro',
            name='genero',
            field=models.ForeignKey(default=1, help_text='Gérero del beneficiario', on_delete=django.db.models.deletion.PROTECT, to='miembro.Genero', verbose_name='Género'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='miembro',
            name='email_personal',
            field=models.EmailField(blank=True, max_length=70, unique=True),
        ),
    ]
