# Generated by Django 3.0.7 on 2020-06-28 19:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0004_auto_20200628_0952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='companie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='s_kill', to='index.companies'),
        ),
    ]