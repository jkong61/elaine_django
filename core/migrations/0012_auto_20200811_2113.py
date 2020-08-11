# Generated by Django 3.1 on 2020-08-11 13:13

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('inspection', '0003_auto_20200811_2113'),
        ('core', '0011_auto_20200810_2346'),
    ]

    operations = [
        migrations.CreateModel(
            name='PipeworkInstance',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for Material Instance', primary_key=True, serialize=False, unique=True, verbose_name='ID')),
                ('serial_number', models.CharField(help_text='Manufacturing Serial Number', max_length=64, verbose_name='Mfg S/N')),
                ('status', models.CharField(choices=[('e', 'Expired'), ('n', 'Not Ready'), ('r', 'Ready'), ('w', 'Expiring')], default='n', help_text='Status of Item', max_length=1)),
                ('instance_remarks', models.CharField(blank=True, help_text='Additional Comments', max_length=255, null=True, verbose_name='Additional Remarks')),
                ('instance_allocation', models.ForeignKey(blank=True, help_text='Item Allocated to which project', null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.joblocation')),
                ('material', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.material', verbose_name='Material Item')),
            ],
            options={
                'verbose_name': 'Pipework Instance',
                'verbose_name_plural': 'Pipework Instances',
            },
        ),
        migrations.CreateModel(
            name='SkidInstance',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for Material Instance', primary_key=True, serialize=False, unique=True, verbose_name='ID')),
                ('serial_number', models.CharField(help_text='Manufacturing Serial Number', max_length=64, verbose_name='Mfg S/N')),
                ('status', models.CharField(choices=[('e', 'Expired'), ('n', 'Not Ready'), ('r', 'Ready'), ('w', 'Expiring')], default='n', help_text='Status of Item', max_length=1)),
                ('instance_remarks', models.CharField(blank=True, help_text='Additional Comments', max_length=255, null=True, verbose_name='Additional Remarks')),
                ('instance_allocation', models.ForeignKey(blank=True, help_text='Item Allocated to which project', null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.joblocation')),
                ('material', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.material', verbose_name='Material Item')),
            ],
            options={
                'verbose_name': 'Skid Instance',
                'verbose_name_plural': 'Skid Instances',
            },
        ),
        migrations.CreateModel(
            name='SlingInstance',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for Material Instance', primary_key=True, serialize=False, unique=True, verbose_name='ID')),
                ('serial_number', models.CharField(help_text='Manufacturing Serial Number', max_length=64, verbose_name='Mfg S/N')),
                ('status', models.CharField(choices=[('e', 'Expired'), ('n', 'Not Ready'), ('r', 'Ready'), ('w', 'Expiring')], default='n', help_text='Status of Item', max_length=1)),
                ('instance_remarks', models.CharField(blank=True, help_text='Additional Comments', max_length=255, null=True, verbose_name='Additional Remarks')),
                ('instance_allocation', models.ForeignKey(blank=True, help_text='Item Allocated to which project', null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.joblocation')),
                ('material', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.material', verbose_name='Material Item')),
            ],
            options={
                'verbose_name': 'Slings Instance',
                'verbose_name_plural': 'Slings Instances',
            },
        ),
        migrations.CreateModel(
            name='TMMDEInstance',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for Material Instance', primary_key=True, serialize=False, unique=True, verbose_name='ID')),
                ('serial_number', models.CharField(help_text='Manufacturing Serial Number', max_length=64, verbose_name='Mfg S/N')),
                ('status', models.CharField(choices=[('e', 'Expired'), ('n', 'Not Ready'), ('r', 'Ready'), ('w', 'Expiring')], default='n', help_text='Status of Item', max_length=1)),
                ('instance_remarks', models.CharField(blank=True, help_text='Additional Comments', max_length=255, null=True, verbose_name='Additional Remarks')),
                ('instance_allocation', models.ForeignKey(blank=True, help_text='Item Allocated to which project', null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.joblocation')),
                ('material', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.material', verbose_name='Material Item')),
            ],
            options={
                'verbose_name': 'TMMDE Instance',
                'verbose_name_plural': 'TMMDE Instances',
            },
        ),
        migrations.DeleteModel(
            name='Instance',
        ),
    ]