# Generated by Django 5.0.4 on 2024-07-11 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('granja', '0007_venta_remove_produccion_cantidad_vendidas_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='venta',
            name='email_cli',
            field=models.EmailField(default=0, max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='venta',
            name='nom_cli',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]
