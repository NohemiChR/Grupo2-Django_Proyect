# Generated by Django 5.1 on 2024-09-06 04:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0004_remove_profile_created_at_remove_profile_updated_at'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Task',
        ),
    ]