# Generated by Django 3.1.7 on 2021-05-16 14:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('collegeapp', '0014_images_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collegereview',
            name='collegeId',
        ),
        migrations.RemoveField(
            model_name='collegereview',
            name='studentId',
        ),
        migrations.RemoveField(
            model_name='coursereview',
            name='studentId',
        ),
        migrations.AddField(
            model_name='collegereview',
            name='user1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='onecol_review', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='collegereview',
            name='user2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='twocol_review', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='coursereview',
            name='userId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
