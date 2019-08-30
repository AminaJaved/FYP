# Generated by Django 2.2.4 on 2019-08-22 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_cancer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cancer',
            name='AADACL4',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='cancer',
            name='ADRA2C',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='cancer',
            name='CLDN8',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='cancer',
            name='DRD5',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='cancer',
            name='FEM1A',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='cancer',
            name='GJC3',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='cancer',
            name='HIST1H4C',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='cancer',
            name='KRT20',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='cancer',
            name='MC2R',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='cancer',
            name='NACA2',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='cancer',
            name='NPFFR1',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='cancer',
            name='PABPC3',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='cancer',
            name='SOWAHA',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='cancer',
            name='TAS2R19',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='cancer',
            name='TAS2R60',
            field=models.CharField(max_length=100),
        ),
    ]
