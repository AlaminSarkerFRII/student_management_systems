# Generated by Django 4.2.6 on 2023-10-05 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_by', models.CharField(blank=True, max_length=200, null=True)),
                ('created_at', models.DateTimeField()),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('fees', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Student',
                'db_table': 'student_info',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_by', models.CharField(blank=True, max_length=200, null=True)),
                ('created_at', models.DateTimeField()),
                ('name', models.CharField(max_length=100)),
                ('salary', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Teacher',
                'db_table': 'teacher_info',
            },
        ),
    ]
