# Generated by Django 2.2 on 2021-08-18 08:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_items_active'),
    ]

    operations = [
        migrations.RenameField(
            model_name='items',
            old_name='prot',
            new_name='prodt',
        ),
    ]
