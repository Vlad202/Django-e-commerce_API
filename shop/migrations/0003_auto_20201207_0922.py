# Generated by Django 3.1.4 on 2020-12-07 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20201207_0918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='currency',
            field=models.CharField(choices=[('$', 'USD'), ('₴', 'UAH'), ('₽', 'RUB')], default='USD', max_length=3),
        ),
    ]