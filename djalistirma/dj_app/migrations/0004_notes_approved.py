# Generated by Django 3.2.9 on 2023-07-30 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dj_app', '0003_alter_notes_note_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='notes',
            name='approved',
            field=models.BooleanField(default=False, help_text='Onaylandımı ?', verbose_name='Onay Aşaması'),
        ),
    ]
