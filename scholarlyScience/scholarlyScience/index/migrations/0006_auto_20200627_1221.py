# Generated by Django 3.0.7 on 2020-06-27 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0005_auto_20200627_1051'),
    ]

    operations = [
        migrations.DeleteModel(
            name='skill_set',
        ),
        migrations.AddField(
            model_name='companies',
            name='skill1',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='companies',
            name='skill2',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='companies',
            name='skill3',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='companies',
            name='skill4',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='companies',
            name='skill5',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
