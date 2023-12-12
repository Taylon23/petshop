# Generated by Django 4.1.12 on 2023-12-11 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animais', '0002_animal_favoritado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='animal',
            name='favoritado',
        ),
        migrations.AlterField(
            model_name='animal',
            name='sexo',
            field=models.CharField(choices=[('M', 'Macho'), ('F', 'Fêmea'), ('O', 'Outro Animal')], max_length=1, verbose_name='sexo'),
        ),
    ]