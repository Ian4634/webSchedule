# Generated by Django 4.1 on 2022-08-10 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduleBoard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='student_names',
            field=models.CharField(default='no info', max_length=500),
        ),
    ]