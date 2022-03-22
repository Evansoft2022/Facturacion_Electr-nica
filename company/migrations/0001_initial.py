# Generated by Django 3.2.8 on 2022-03-22 19:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('documentIdentification', models.TextField(unique=True)),
                ('business_name', models.TextField()),
                ('address', models.TextField()),
                ('phone', models.TextField()),
                ('email', models.TextField()),
                ('certificate_generation_date', models.CharField(max_length=10)),
                ('certificate_expiration_date', models.CharField(max_length=10)),
                ('resolution_generation_date', models.CharField(max_length=10)),
                ('resolution_expiration_date', models.CharField(default='', max_length=10)),
                ('block', models.BooleanField(default=False)),
                ('municipality', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.municipality')),
                ('type_documentI', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.type_document_identification')),
                ('type_organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.type_organization')),
                ('type_regime', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.type_regime')),
            ],
        ),
    ]
