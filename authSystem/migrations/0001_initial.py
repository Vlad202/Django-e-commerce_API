# Generated by Django 3.1.4 on 2020-12-06 20:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=32)),
                ('last_name', models.CharField(max_length=32)),
                ('father_name', models.CharField(max_length=32)),
                ('phone', models.CharField(blank=True, help_text='Contact phone number', max_length=12)),
                ('email', models.CharField(max_length=64)),
                ('country', models.CharField(max_length=32)),
                ('city', models.CharField(max_length=32)),
                ('region', models.CharField(max_length=32)),
                ('address', models.CharField(max_length=144)),
                ('post_index', models.IntegerField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
