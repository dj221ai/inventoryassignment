# Generated by Django 3.1.2 on 2020-10-23 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productinformation',
            name='product_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]