# Generated by Django 3.2.20 on 2023-08-27 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_auto_20230827_1045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderlineitem',
            name='size',
            field=models.CharField(default='S', max_length=1),
        ),
    ]