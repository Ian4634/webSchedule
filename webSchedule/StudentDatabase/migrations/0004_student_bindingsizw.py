# Generated by Django 4.1 on 2022-08-11 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StudentDatabase', '0003_alter_student_shoe'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='bindingSizw',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]