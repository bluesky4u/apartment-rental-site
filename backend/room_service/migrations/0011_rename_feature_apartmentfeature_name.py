# Generated by Django 4.1.1 on 2022-10-05 18:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('room_service', '0010_apartmentfeature_apartment_features'),
    ]

    operations = [
        migrations.RenameField(
            model_name='apartmentfeature',
            old_name='feature',
            new_name='name',
        ),
    ]