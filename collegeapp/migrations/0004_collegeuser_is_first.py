# Generated by Django 3.1.7 on 2021-05-08 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collegeapp', '0003_collegeuser_nirfranking'),
    ]

    operations = [
        migrations.AddField(
            model_name='collegeuser',
            name='is_first',
            field=models.BooleanField(default=False),
        ),
    ]
