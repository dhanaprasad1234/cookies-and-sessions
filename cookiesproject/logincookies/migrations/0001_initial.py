# Generated by Django 5.0.3 on 2024-04-06 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=12)),
                ('password', models.CharField(max_length=115)),
                ('datetime', models.DateTimeField()),
            ],
            options={
                'db_table': 'loginform',
            },
        ),
    ]
