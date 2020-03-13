# Generated by Django 3.0 on 2020-03-13 13:29

import django.contrib.postgres.fields.ranges
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period', django.contrib.postgres.fields.ranges.DateTimeRangeField()),
                ('profession', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='filter_related_through.Profession')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='professions', to='filter_related_through.User')),
            ],
        ),
        migrations.AddField(
            model_name='profession',
            name='users',
            field=models.ManyToManyField(through='filter_related_through.UserProfession', to='filter_related_through.User'),
        ),
    ]
