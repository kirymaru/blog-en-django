# Generated by Django 5.0.1 on 2024-03-21 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_delete_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='apellidos',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='nombre',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
