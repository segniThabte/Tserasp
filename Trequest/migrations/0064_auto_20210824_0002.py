# Generated by Django 3.2.5 on 2021-08-23 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Trequest', '0063_assignrequest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignrequest',
            name='driver_to',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='assignrequest',
            name='user_to',
            field=models.CharField(max_length=200),
        ),
    ]