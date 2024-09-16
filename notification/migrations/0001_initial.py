# Generated by Django 5.0.6 on 2024-09-14 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('message', models.TextField()),
                ('type', models.CharField(choices=[('info', 'Information'), ('warn', 'Warning'), ('error', 'Error'), ('success', 'Success')], max_length=255)),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
        ),
    ]