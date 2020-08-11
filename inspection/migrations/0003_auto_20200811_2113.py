# Generated by Django 3.1 on 2020-08-11 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inspection', '0002_annualinspection_majorinspection_pipeworkndeinspection_prepostjobinspection'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mpiinpection',
            options={'verbose_name': 'MPI Inspection (Lifting)', 'verbose_name_plural': 'Lifting MPI Inspections'},
        ),
        migrations.AlterModelOptions(
            name='visualinspection',
            options={'verbose_name': 'Visual Inspection (Lifting)', 'verbose_name_plural': 'Lifting Visual Inspections'},
        ),
        migrations.RemoveField(
            model_name='annualinspection',
            name='material_instance',
        ),
        migrations.RemoveField(
            model_name='calibrationinspection',
            name='material_instance',
        ),
        migrations.RemoveField(
            model_name='majorinspection',
            name='material_instance',
        ),
        migrations.RemoveField(
            model_name='mpiinpection',
            name='material_instance',
        ),
        migrations.RemoveField(
            model_name='pipeworkndeinspection',
            name='material_instance',
        ),
        migrations.RemoveField(
            model_name='prepostjobinspection',
            name='material_instance',
        ),
        migrations.RemoveField(
            model_name='visualinspection',
            name='material_instance',
        ),
        migrations.AlterField(
            model_name='mpiinpection',
            name='type',
            field=models.CharField(choices=[('k', 'Skid'), ('s', 'Sling')], default='k', help_text='Type of Item', max_length=1),
        ),
        migrations.AlterField(
            model_name='visualinspection',
            name='type',
            field=models.CharField(choices=[('k', 'Skid'), ('s', 'Sling')], default='k', help_text='Type of Item', max_length=1),
        ),
    ]
