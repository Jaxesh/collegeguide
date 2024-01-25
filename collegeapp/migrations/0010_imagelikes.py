# Generated by Django 3.1.7 on 2021-05-10 14:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('collegeapp', '0009_followers_like'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageLikes',
            fields=[
                ('likeId', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('imageId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collegeapp.images')),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]