# Generated by Django 5.0.4 on 2024-07-04 23:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('granja', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='peso',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='peso_animal', to='granja.registro'),
        ),
        migrations.AddField(
            model_name='trabajador',
            name='salario',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
