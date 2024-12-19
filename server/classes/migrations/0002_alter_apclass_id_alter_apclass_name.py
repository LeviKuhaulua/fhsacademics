# Generated by Django 4.2.17 on 2024-12-19 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apclass',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='apclass',
            name='name',
            field=models.CharField(help_text="Do not need to put 'AP' before the class name.", max_length=200),
        ),
    ]