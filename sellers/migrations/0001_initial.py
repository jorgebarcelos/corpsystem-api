# Generated by Django 4.2.7 on 2023-11-27 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sellers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seller_id', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]
