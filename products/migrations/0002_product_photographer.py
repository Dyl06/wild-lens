# Generated by Django 3.2.20 on 2023-08-19 11:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photographer', '0002_auto_20230819_1136'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='photographer',
            field=models.ForeignKey(
                default='',
                on_delete=django.db.models.deletion.CASCADE,
                to='photographer.photographer'),
        ),
    ]
