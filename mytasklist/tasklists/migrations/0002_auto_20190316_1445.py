# Generated by Django 2.1.7 on 2019-03-16 14:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasklists', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='atualizado_por',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='tasks',
            name='criado_por',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='users', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]