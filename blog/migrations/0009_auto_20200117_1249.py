# Generated by Django 3.0.2 on 2020-01-17 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20200117_1243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='model',
            name='catch',
            field=models.TextField(verbose_name='Catck'),
        ),
    ]
