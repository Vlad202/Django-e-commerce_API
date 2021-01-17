# Generated by Django 3.1.4 on 2020-12-07 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='currency',
            field=models.CharField(choices=[('USD', '$'), ('UAH', '₴'), ('RUB', '₽')], default='USD', max_length=3),
        ),
    ]