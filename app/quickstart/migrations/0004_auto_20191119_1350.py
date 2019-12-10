# Generated by Django 2.2.5 on 2019-11-19 13:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0003_auto_20191118_2341'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='nationality',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='books', to='quickstart.Author'),
        ),
    ]
