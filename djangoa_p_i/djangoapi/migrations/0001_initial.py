# Generated by Django 3.2.6 on 2021-08-09 13:10

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=225)),
                ('email', models.EmailField(max_length=225)),
                ('job', models.CharField(max_length=225)),
            ],
        ),
    ]
