# Generated by Django 3.2.25 on 2024-12-11 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_product_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='stripe_product_price_id',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
