# Generated by Django 3.1.5 on 2022-04-12 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Assistant', '0005_notice'),
    ]

    operations = [
        migrations.CreateModel(
            name='calendar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.CharField(max_length=20)),
                ('date', models.DateTimeField()),
                ('purpose', models.TextField()),
            ],
        ),
    ]