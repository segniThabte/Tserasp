# Generated by Django 3.2.5 on 2021-08-25 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MaterialApp', '0002_alter_material_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='material',
            name='model',
            field=models.CharField(max_length=200, null=True),
        ),
    ]