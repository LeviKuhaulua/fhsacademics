# Generated by Django 4.2.17 on 2024-12-21 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0023_alter_apclass_grade_levels_alter_apclass_slug_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apclass',
            name='grade_levels',
            field=models.ManyToManyField(to='classes.gradelevel'),
        ),
    ]
