# Generated by Django 2.2.4 on 2019-08-23 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20190822_0945'),
    ]

    operations = [
        migrations.CreateModel(
            name='visualise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cancer_Class', models.CharField(max_length=100)),
                ('Description', models.TextField()),
                ('Symptoms', models.TextField()),
            ],
        ),
    ]
