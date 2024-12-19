# Generated by Django 4.2.17 on 2024-12-19 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0009_alter_apclass_options_alter_apclass_is_active_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apclass',
            name='slug',
            field=models.SlugField(blank=True, default='', help_text='Unique link generated based on class name. \n                                                                              Example: classes/calculus instead of classes/9', unique=True),
        ),
    ]
