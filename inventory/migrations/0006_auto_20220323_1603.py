# Generated by Django 3.2.8 on 2022-03-23 21:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0005_consecutive_elec_consecutive_pos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='consecutive_pos',
            name='company',
        ),
        migrations.DeleteModel(
            name='Consecutive_Elec',
        ),
        migrations.DeleteModel(
            name='Consecutive_POS',
        ),
    ]
