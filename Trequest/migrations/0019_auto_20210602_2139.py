# Generated by Django 3.0.3 on 2021-06-02 18:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Trequest', '0018_auto_20210602_2137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='approverequest',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Trequest.TransportRequest'),
        ),
    ]