# Generated by Django 3.0.7 on 2020-07-30 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200730_1920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='description',
            field=models.CharField(max_length=2500),
        ),
    ]
