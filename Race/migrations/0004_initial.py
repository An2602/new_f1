# Generated by Django 4.1.2 on 2022-11-23 14:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Driver', '0004_remove_driver__id_driver_id'),
        ('Race', '0003_delete_race'),
    ]

    operations = [
        migrations.CreateModel(
            name='Race',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('race_name', models.CharField(max_length=100)),
                ('race_type', models.SmallIntegerField(choices=[(1, 'Regular race'), (2, 'Sprint race')], default=1)),
                ('race_date', models.DateField()),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
                ('fastest_driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Driver.driver')),
            ],
        ),
        migrations.CreateModel(
            name='Standing_in_race',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('standing', models.SmallIntegerField()),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Driver.driver')),
                ('race', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Race.race')),
            ],
        ),
    ]
