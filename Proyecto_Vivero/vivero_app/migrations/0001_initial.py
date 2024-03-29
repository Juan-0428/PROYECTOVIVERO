# Generated by Django 2.2.3 on 2024-03-18 19:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Finca',
            fields=[
                ('NumCatastro', models.IntegerField(primary_key=True, serialize=False)),
                ('Municipio', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Labor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fecha', models.DateTimeField(auto_now=True)),
                ('Descripcion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ProductoControl',
            fields=[
                ('RegistroICA', models.IntegerField(primary_key=True, serialize=False)),
                ('NombreProducto', models.CharField(max_length=50)),
                ('Frecuencia', models.CharField(max_length=50)),
                ('ValorProducto', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Labor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ProductosControl', to='vivero_app.Labor')),
            ],
        ),
        migrations.CreateModel(
            name='Productor',
            fields=[
                ('Documento', models.IntegerField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=100)),
                ('Apellido', models.CharField(max_length=100)),
                ('Correo', models.EmailField(max_length=254)),
                ('Telefono', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Vivero',
            fields=[
                ('Codigo', models.IntegerField(primary_key=True, serialize=False)),
                ('TipoDeCultivo', models.CharField(max_length=100)),
                ('Finca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Viveros', to='vivero_app.Finca')),
            ],
        ),
        migrations.AddField(
            model_name='labor',
            name='Vivero',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Labores', to='vivero_app.Vivero'),
        ),
        migrations.AddField(
            model_name='finca',
            name='Productor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Fincas', to='vivero_app.Productor'),
        ),
        migrations.CreateModel(
            name='ControlPlaga',
            fields=[
                ('productocontrol_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='vivero_app.ProductoControl')),
                ('PeriodoCarencia', models.IntegerField()),
                ('ProductoControl', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ControlPlaga', to='vivero_app.ProductoControl')),
            ],
            bases=('vivero_app.productocontrol',),
        ),
        migrations.CreateModel(
            name='ControlHongo',
            fields=[
                ('productocontrol_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='vivero_app.ProductoControl')),
                ('PeriodoCarencia', models.IntegerField()),
                ('NombreHongo', models.CharField(max_length=100)),
                ('ProductoControl', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ControlHongo', to='vivero_app.ProductoControl')),
            ],
            bases=('vivero_app.productocontrol',),
        ),
        migrations.CreateModel(
            name='ControlFertilizante',
            fields=[
                ('productocontrol_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='vivero_app.ProductoControl')),
                ('FechaUltimaAplicacion', models.DateField()),
                ('ProductoControl', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ControlFertilizante', to='vivero_app.ProductoControl')),
            ],
            bases=('vivero_app.productocontrol',),
        ),
    ]
