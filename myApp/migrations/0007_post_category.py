# Generated by Django 3.1.6 on 2021-02-02 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0006_auto_20210202_2052'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ManyToManyField(to='myApp.Category', verbose_name='Categoria'),
        ),
    ]
