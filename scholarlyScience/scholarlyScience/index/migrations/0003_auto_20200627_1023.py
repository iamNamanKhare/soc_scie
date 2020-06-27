# Generated by Django 3.0.7 on 2020-06-27 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_auto_20200626_1029'),
    ]

    operations = [
        migrations.CreateModel(
            name='skill_set',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('LiveRamp', models.CharField(max_length=45)),
                ('Twilio', models.CharField(max_length=45)),
                ('Github', models.CharField(max_length=45)),
                ('Asana', models.CharField(max_length=45)),
                ('Robinhood', models.CharField(max_length=45)),
                ('Postmates', models.CharField(max_length=45)),
                ('BitGo', models.CharField(max_length=45)),
                ('Sysdig', models.CharField(max_length=45)),
                ('Harrys', models.CharField(max_length=45)),
                ('Justworks', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'skills',
            },
        ),
        migrations.RemoveField(
            model_name='companies',
            name='skills',
        ),
    ]