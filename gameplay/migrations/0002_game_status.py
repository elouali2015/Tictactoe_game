# Generated by Django 3.0.1 on 2020-01-17 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gameplay', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='status',
            field=models.CharField(default='F', max_length=1),
        ),
    ]
