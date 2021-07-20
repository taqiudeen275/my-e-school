# Generated by Django 3.2.2 on 2021-07-20 11:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('student', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('verified', models.BooleanField(default=False)),
                ('student', models.ManyToManyField(related_name='parent', to='student.Student')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='is_parent', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]