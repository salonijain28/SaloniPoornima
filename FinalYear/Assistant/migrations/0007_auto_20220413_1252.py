# Generated by Django 3.1.5 on 2022-04-13 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Assistant', '0006_calendar'),
    ]

    operations = [
        migrations.CreateModel(
            name='calendardetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.CharField(max_length=20)),
                ('date', models.DateField()),
                ('purpose', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='calendar',
        ),
    ]