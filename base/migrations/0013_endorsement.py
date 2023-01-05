# Generated by Django 4.1.3 on 2023-01-05 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='Endorsement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('body', models.TextField()),
                ('is_read', models.BooleanField(default=False)),
            ],
        ),
    ]
