# Generated by Django 2.2 on 2019-04-28 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booklibrary', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='borrows',
            name='statr',
            field=models.BooleanField(default=False),
        ),
    ]