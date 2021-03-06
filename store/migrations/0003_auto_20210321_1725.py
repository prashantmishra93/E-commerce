# Generated by Django 3.1.4 on 2021-03-21 11:55

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20210312_1536'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='date',
            field=models.DateField(default=datetime.datetime.today),
        ),
        migrations.AddField(
            model_name='orders',
            name='price',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orders',
            name='product',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='store.products'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orders',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='orders',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='store.customerdata'),
            preserve_default=False,
        ),
    ]
