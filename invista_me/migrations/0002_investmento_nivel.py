# Generated by Django 4.2.5 on 2023-09-10 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invista_me', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='investmento',
            name='nivel',
            field=models.IntegerField(default=1),
        ),
    ]
