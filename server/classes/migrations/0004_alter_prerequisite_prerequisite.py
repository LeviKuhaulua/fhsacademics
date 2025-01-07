# Generated by Django 4.2.17 on 2025-01-07 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0003_alter_apclass_benefits_alter_apclass_prerequisite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prerequisite',
            name='prerequisite',
            field=models.CharField(help_text='Classes needed before a student can apply to the course. \n        Please enter full name of course', max_length=50, null=True, unique=True),
        ),
    ]
