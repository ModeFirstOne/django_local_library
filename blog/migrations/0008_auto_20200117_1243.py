# Generated by Django 3.0.2 on 2020-01-17 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20200117_1141'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Mo2',
        ),
        migrations.AddField(
            model_name='model',
            name='catch',
            field=models.TextField(default='', verbose_name='Catck'),
        ),
    ]