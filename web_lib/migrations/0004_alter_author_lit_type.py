# Generated by Django 4.1 on 2022-09-01 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_lib', '0003_alter_author_lit_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='lit_type',
            field=models.CharField(choices=[('a', 'foreign'), ('b', 'domestic'), ('c', 'other')], default='a', max_length=1, verbose_name='Тип литературы'),
        ),
    ]
