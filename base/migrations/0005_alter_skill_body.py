# Generated by Django 4.1.3 on 2023-01-02 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_alter_project_slug_alter_skill_body_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='body',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
    ]
