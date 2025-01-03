# Generated by Django 4.2.17 on 2024-12-20 16:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0018_apclass_subject_alter_subject_subject'),
    ]

    operations = [
        migrations.AddField(
            model_name='apclass',
            name='available_to',
            field=models.ManyToManyField(to='classes.gradelevel'),
        ),
        migrations.AlterField(
            model_name='apclass',
            name='subject',
            field=models.ForeignKey(default='1', help_text='Choose the subject that best relates to this class', on_delete=django.db.models.deletion.PROTECT, related_name='+', to='classes.subject'),
        ),
    ]
