# Generated by Django 2.0.5 on 2018-06-28 23:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('videoclub', '0003_auto_20180628_0013'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='esDirector',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='pelicula',
            name='director',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='director', to='videoclub.Persona'),
        ),
        migrations.AlterField(
            model_name='pelicula',
            name='reparto',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reparto', to='videoclub.Persona'),
        ),
        migrations.AlterField(
            model_name='pelicula',
            name='valoracion',
            field=models.PositiveIntegerField(),
        ),
    ]
