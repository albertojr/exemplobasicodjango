# Generated by Django 3.0.6 on 2020-05-30 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Somas',
            fields=[
                ('idSomas', models.AutoField(primary_key=True, serialize=False)),
                ('valor1', models.FloatField(verbose_name='Primeiro Valor:')),
                ('valor2', models.FloatField(verbose_name='Segundo Valor:')),
                ('resultado', models.FloatField(blank=True, null=True, verbose_name='resultado')),
            ],
            options={
                'db_table': 'Somas',
                'managed': True,
            },
        ),
    ]
