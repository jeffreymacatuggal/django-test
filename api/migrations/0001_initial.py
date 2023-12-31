# Generated by Django 4.2.3 on 2023-07-31 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('url', models.CharField(max_length=1000)),
                ('image_url', models.CharField(max_length=1000)),
            ],
        ),
    ]
