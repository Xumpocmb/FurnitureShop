# Generated by Django 5.0 on 2023-12-28 06:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog_app', '0002_alter_category_name_alter_category_slug_product'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['id'], 'verbose_name': 'Товар', 'verbose_name_plural': 'Товары'},
        ),
    ]
