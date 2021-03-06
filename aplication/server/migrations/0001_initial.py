# Generated by Django 3.1.13 on 2021-11-02 16:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aplicativos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Categorias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('tipo', models.CharField(choices=[('HARDWARE', 'Hardware'), ('SOFTWARE', 'Software')], max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Configuracoes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='server.categorias')),
            ],
        ),
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('local', models.CharField(max_length=255)),
                ('apps', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='server.aplicativos')),
                ('config', models.ManyToManyField(to='server.Configuracoes')),
            ],
        ),
    ]
