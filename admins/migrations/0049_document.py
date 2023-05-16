# Generated by Django 4.1.7 on 2023-04-26 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0048_logisticsoffers_quantity'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=255)),
                ('document', models.FileField(upload_to='documents/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
