# Generated by Django 4.1 on 2022-08-19 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bin',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('cost', models.CharField(max_length=280, null=True)),
                ('title', models.CharField(max_length=280, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('cost', models.CharField(max_length=280, null=True)),
                ('title', models.CharField(max_length=280, null=True)),
            ],
        ),
    ]
