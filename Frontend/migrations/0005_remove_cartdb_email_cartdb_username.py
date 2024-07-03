# Generated by Django 4.2.7 on 2024-01-03 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Frontend', '0004_remove_cartdb_username_cartdb_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartdb',
            name='Email',
        ),
        migrations.AddField(
            model_name='cartdb',
            name='UserName',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]