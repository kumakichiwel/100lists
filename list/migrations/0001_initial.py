# Generated by Django 2.1.4 on 2018-12-17 03:56

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(max_length=100)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2018, 12, 17, 12, 56, 34, 411177))),
            ],
            options={
                'db_table': 'comment',
            },
        ),
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('due_date', models.DateField(blank=True, null=True)),
                ('rank', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2018, 12, 17, 12, 56, 34, 409876))),
                ('image', models.ImageField(blank=True, upload_to='uploads/%Y/%m/%d/')),
                ('status', models.BooleanField(default=False)),
                ('share', models.IntegerField(default=2)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'list',
            },
        ),
        migrations.AddField(
            model_name='comment',
            name='list',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='list.List'),
        ),
    ]
