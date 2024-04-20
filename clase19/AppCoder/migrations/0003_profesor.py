# Generated by Django 5.0.4 on 2024-04-13 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0002_alumno'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('legajo', models.IntegerField()),
                ('edad', models.IntegerField()),
                ('tutor', models.CharField(max_length=25)),
                ('email', models.CharField(max_length=20)),
            ],
        ),
    ]
