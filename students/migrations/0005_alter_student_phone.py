# Generated by Django 4.2.6 on 2023-10-11 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_rename_fisrt_name_student_first_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='phone',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
