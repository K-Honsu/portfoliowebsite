# Generated by Django 3.2.18 on 2023-02-21 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0020_alter_skill_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='logo',
            field=models.ImageField(default='default--skill--icon.png', null=True, upload_to=''),
        ),
    ]