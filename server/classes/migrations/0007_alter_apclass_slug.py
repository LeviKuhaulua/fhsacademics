# Generated by Django 4.2.17 on 2024-12-19 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0006_alter_apclass_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apclass',
            name='slug',
            field=models.SlugField(default='', editable=False, unique=True),
        ),
    ]
