# Generated by Django 4.1.3 on 2023-01-05 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0019_skill_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='logo',
            field=models.ImageField(default='default--skill--icon', null=True, upload_to=''),
        ),
    ]
