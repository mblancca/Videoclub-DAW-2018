# Generated by Django 2.0.5 on 2018-06-29 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videoclub', '0010_auto_20180629_1538'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pelicula',
            name='reparto',
        ),
        migrations.AddField(
            model_name='pelicula',
            name='reparto',
            field=models.ManyToManyField(related_name='reparto', to='videoclub.Persona'),
        ),
    ]
