# Generated by Django 3.2.4 on 2021-06-05 22:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Trequest', '0023_auto_20210605_0225'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transportrequest',
            old_name='user',
            new_name='passenger',
        ),
    ]