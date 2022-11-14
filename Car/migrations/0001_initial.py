# Generated by Django 4.1.2 on 2022-10-24 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('score', models.SmallIntegerField()),
                ('standing', models.SmallIntegerField()),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
            ],
        ),
    ]