# Generated by Django 2.2 on 2019-05-06 15:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inspector', '0003_model'),
    ]

    operations = [
        migrations.RenameField(
            model_name='model',
            old_name='model',
            new_name='upload',
        ),
    ]
