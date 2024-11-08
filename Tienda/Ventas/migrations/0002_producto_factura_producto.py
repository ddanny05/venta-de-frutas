# Generated by Django 5.1.3 on 2024-11-08 04:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ventas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('codigo_de_producto', models.CharField(max_length=5, primary_key=True, serialize=False, validators=[django.core.validators.MinLengthValidator(3), django.core.validators.MaxLengthValidator(5)])),
                ('nombre', models.CharField(max_length=50)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
        migrations.AddField(
            model_name='factura',
            name='producto',
            field=models.ManyToManyField(to='Ventas.producto'),
        ),
    ]
