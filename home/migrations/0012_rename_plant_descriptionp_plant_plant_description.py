# Generated by Django 4.1.4 on 2022-12-22 18:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_rename_lant_descriptionp_plant_plant_descriptionp'),
    ]

    operations = [
        migrations.RenameField(
            model_name='plant',
            old_name='plant_descriptionp',
            new_name='plant_description',
        ),
    ]
