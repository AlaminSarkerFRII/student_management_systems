# Generated by Django 4.2.6 on 2023-10-06 08:39

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
                ('student_number', models.PositiveIntegerField()),
                ('fisrt_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('field_of_study', models.CharField(max_length=100)),
                ('gpa', models.FloatField()),
            ],
            options={
                'verbose_name_plural': 'students',
                'db_table': 'students_info',
            },
        ),
    ]
