# Generated by Django 4.2.7 on 2024-01-03 14:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Frontend', '0005_remove_cartdb_email_cartdb_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartdb',
            old_name='TotalPrice',
            new_name='Totalprice',
        ),
        migrations.RenameField(
            model_name='cartdb',
            old_name='UserName',
            new_name='Username',
        ),
    ]
