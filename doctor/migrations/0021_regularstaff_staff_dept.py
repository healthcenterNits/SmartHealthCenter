# Generated by Django 2.2.5 on 2020-02-25 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0020_auto_20200210_2315'),
    ]

    operations = [
        migrations.AddField(
            model_name='regularstaff',
            name='staff_dept',
            field=models.CharField(default='x', max_length=50),
            preserve_default=False,
        ),
    ]