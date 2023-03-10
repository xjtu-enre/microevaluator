# Generated by Django 3.2.8 on 2023-03-07 12:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='逻辑删除')),
                ('projectname', models.CharField(max_length=500)),
                ('url', models.CharField(max_length=500)),
                ('description', models.TextField()),
                ('ismicro', models.BooleanField(default=0)),
                ('process', models.IntegerField(default=0)),
                ('language', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'Project',
            },
        ),
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='逻辑删除')),
                ('loc', models.IntegerField(default=0, max_length=50)),
                ('score', models.FloatField(default=0, max_length=50)),
                ('version', models.CharField(max_length=50)),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='project.project', verbose_name='所属项目')),
            ],
            options={
                'db_table': 'Version',
                'ordering': ['-timestamp'],
            },
        ),
    ]
