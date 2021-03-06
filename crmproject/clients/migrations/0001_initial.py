# Generated by Django 3.1.1 on 2020-10-30 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='First Name', max_length=36)),
                ('last_name', models.CharField(default='Last Name', max_length=36)),
                ('mobile', models.CharField(default='Mobile', max_length=13, unique=True)),
                ('status', models.CharField(choices=[('1', 'New Client'), ('2', 'Client In Progress'), ('3', 'Client Processed')], default='1', max_length=9)),
            ],
        ),
    ]
