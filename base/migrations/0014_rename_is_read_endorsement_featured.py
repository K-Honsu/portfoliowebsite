# Generated by Django 4.1.3 on 2023-01-05 13:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0013_endorsement'),
    ]

    operations = [
        migrations.RenameField(
            model_name='endorsement',
            old_name='is_read',
            new_name='featured',
        ),
    ]
