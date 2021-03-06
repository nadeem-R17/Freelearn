# Generated by Django 4.0 on 2021-12-27 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gama', '0002_nacbio_nacchem_nacphy_nambio_namchem_namphy_natbio_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='bcbio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('batan', models.CharField(default='some_string', max_length=1000)),
                ('url', models.CharField(default='some_string', max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='bcchem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('batan', models.CharField(default='some_string', max_length=1000)),
                ('url', models.CharField(default='some_string', max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='bcmath',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('batan', models.CharField(default='some_string', max_length=1000)),
                ('url', models.CharField(default='some_string', max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='bcphy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('batan', models.CharField(default='some_string', max_length=1000)),
                ('url', models.CharField(default='some_string', max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='bmbio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('batan', models.CharField(default='some_string', max_length=1000)),
                ('url', models.CharField(default='some_string', max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='bmchem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('batan', models.CharField(default='some_string', max_length=1000)),
                ('url', models.CharField(default='some_string', max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='bmmath',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('batan', models.CharField(default='some_string', max_length=1000)),
                ('url', models.CharField(default='some_string', max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='bmphy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('batan', models.CharField(default='some_string', max_length=1000)),
                ('url', models.CharField(default='some_string', max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='btbio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('batan', models.CharField(default='some_string', max_length=1000)),
                ('url', models.CharField(default='some_string', max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='btchem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('batan', models.CharField(default='some_string', max_length=1000)),
                ('url', models.CharField(default='some_string', max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='btmath',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('batan', models.CharField(default='some_string', max_length=1000)),
                ('url', models.CharField(default='some_string', max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='btphy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('batan', models.CharField(default='some_string', max_length=1000)),
                ('url', models.CharField(default='some_string', max_length=1000)),
            ],
        ),
    ]
