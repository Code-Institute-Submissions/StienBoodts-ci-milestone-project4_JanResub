# Generated by Django 3.2.16 on 2022-12-20 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_has_sizes'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='colour',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
