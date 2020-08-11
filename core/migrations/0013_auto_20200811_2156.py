# Generated by Django 3.1 on 2020-08-11 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20200811_2113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pipeworkinstance',
            name='status',
            field=models.CharField(choices=[('r', 'Ready'), ('w', 'Expiring'), ('e', 'Expired'), ('n', 'Not Ready')], default='n', help_text='Status of Item', max_length=1),
        ),
        migrations.AlterField(
            model_name='skidinstance',
            name='status',
            field=models.CharField(choices=[('r', 'Ready'), ('w', 'Expiring'), ('e', 'Expired'), ('n', 'Not Ready')], default='n', help_text='Status of Item', max_length=1),
        ),
        migrations.AlterField(
            model_name='slinginstance',
            name='status',
            field=models.CharField(choices=[('r', 'Ready'), ('w', 'Expiring'), ('e', 'Expired'), ('n', 'Not Ready')], default='n', help_text='Status of Item', max_length=1),
        ),
        migrations.AlterField(
            model_name='tmmdeinstance',
            name='status',
            field=models.CharField(choices=[('r', 'Ready'), ('w', 'Expiring'), ('e', 'Expired'), ('n', 'Not Ready')], default='n', help_text='Status of Item', max_length=1),
        ),
    ]
