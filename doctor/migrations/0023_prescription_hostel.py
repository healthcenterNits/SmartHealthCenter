# Generated by Django 2.2.6 on 2020-05-01 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0022_auto_20200419_2111'),
    ]

    operations = [
        migrations.AddField(
            model_name='prescription',
            name='hostel',
            field=models.CharField(default=None, max_length=100),
        ),
    ]