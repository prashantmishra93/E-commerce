# Generated by Django 3.1.4 on 2021-03-21 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20210321_1725'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='address',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orders',
            name='phone',
            field=models.CharField(default=0, max_length=12),
            preserve_default=False,
        ),
    ]