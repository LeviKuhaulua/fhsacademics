# Generated by Django 4.2.17 on 2024-12-20 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0013_alter_apclass_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name="apclass",
            old_name="is_active",
            new_name="is_offered",
        ),
    ]