# Generated by Django 3.0.2 on 2020-01-16 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_model_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='model',
            name='sort',
            field=models.PositiveIntegerField(default=0, verbose_name='Порядок'),
        ),
    ]