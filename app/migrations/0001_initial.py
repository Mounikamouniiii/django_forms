# Generated by Django 4.0.5 on 2022-07-15 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('Sid', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('Sname', models.CharField(max_length=100)),
            ],
        ),
    ]