# Generated by Django 2.2 on 2022-11-29 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_flipkart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='is_staff',
            field=models.BooleanField(default=True),
        ),
    ]
