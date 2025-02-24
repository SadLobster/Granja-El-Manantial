# Generated by Django 5.0.4 on 2024-07-08 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('granja', '0006_alter_animal_peso'),
    ]

    operations = [
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_insert', models.DateField(auto_now_add=True)),
                ('tipo', models.CharField(max_length=20)),
                ('cantidad', models.IntegerField()),
                ('precio_total', models.FloatField()),
                ('id_vendidas', models.CharField(default='N/A', max_length=100)),
                ('precio_uni', models.FloatField(default=None)),
                ('tipo_ganado', models.CharField(choices=[('toro', 'Toro'), ('vaca', 'Vaca'), ('ternero', 'Ternero')], default='N/A', max_length=20)),
                ('adicional', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='produccion',
            name='cantidad_vendidas',
        ),
        migrations.RemoveField(
            model_name='produccion',
            name='id_vendidas',
        ),
        migrations.RemoveField(
            model_name='produccion',
            name='precio',
        ),
        migrations.RemoveField(
            model_name='produccion',
            name='tipo',
        ),
        migrations.RemoveField(
            model_name='produccion',
            name='tipo_ganado',
        ),
    ]
