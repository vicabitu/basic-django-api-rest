# Generated by Django 2.2.5 on 2019-11-27 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0004_auto_20191119_1350'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='available_quantity',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
