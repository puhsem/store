# Generated by Django 3.2.25 on 2024-11-21 13:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20241118_2136'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-id'], 'verbose_name': 'Продукты', 'verbose_name_plural': 'Продукты'},
        ),
    ]
