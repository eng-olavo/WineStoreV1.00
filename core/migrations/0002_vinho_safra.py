# Generated by Django 3.2.8 on 2021-10-15 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vinho',
            name='safra',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
