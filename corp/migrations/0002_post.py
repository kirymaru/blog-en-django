# Generated by Django 5.0.1 on 2024-03-12 20:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=100, verbose_name='Titulo del Post')),
                ('contenido', models.CharField(blank=True, max_length=500, verbose_name='Contenido del Post')),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='corp.autor')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='corp.categoria')),
            ],
        ),
    ]
