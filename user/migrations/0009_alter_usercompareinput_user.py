# Generated by Django 4.2.6 on 2023-11-13 18:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0008_alter_usercompareinput_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercompareinput',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_compare_input', to=settings.AUTH_USER_MODEL),
        ),
    ]
