# Generated by Django 4.0.4 on 2022-04-14 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addressbook_app', '0002_alter_userprofile_status_alter_usersignup_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='SqlLogin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(blank=True, max_length=50, null=True)),
                ('created_date_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]