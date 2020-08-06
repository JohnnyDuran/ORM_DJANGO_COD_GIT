# Generated by Django 3.1 on 2020-08-04 17:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ruc', models.CharField(max_length=13)),
                ('nombre', models.CharField(max_length=300)),
                ('direccion', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=100)),
                ('precio', models.FloatField(default=0)),
                ('stock', models.FloatField(default=0)),
                ('iva', models.BooleanField(default=True)),
                ('creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha Creación')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
                'ordering': ['-creacion'],
            },
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('total', models.FloatField(default=0)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apporm.cliente')),
            ],
            options={
                'verbose_name': 'Factura',
                'verbose_name_plural': 'Facturas',
            },
        ),
        migrations.CreateModel(
            name='DetalleFactura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.FloatField(default=0)),
                ('precio', models.FloatField(default=0)),
                ('subtotal', models.FloatField(default=0)),
                ('factura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apporm.factura')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apporm.producto')),
            ],
        ),
        migrations.AddField(
            model_name='cliente',
            name='producto',
            field=models.ManyToManyField(to='apporm.Producto'),
        ),
    ]
