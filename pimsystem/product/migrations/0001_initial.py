# Generated by Django 3.1.2 on 2020-10-23 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('price', models.FloatField(default=0)),
                ('quantity', models.IntegerField(default=0)),
                ('status', models.BooleanField(default=True)),
                ('product_image', models.ImageField(blank=True, null=True, upload_to='media/')),
            ],
        ),
    ]
