# Generated by Django 2.0.5 on 2018-07-01 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videoclub', '0013_auto_20180629_1733'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='urlFoto',
            field=models.CharField(default='https://www.yueimg.com/en/images/common/avatar.b6a87.png', max_length=200),
        ),
        migrations.AlterField(
            model_name='genero',
            name='name',
            field=models.CharField(help_text='Introduzca un género de película', max_length=200),
        ),
    ]
