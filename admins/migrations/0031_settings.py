# Generated by Django 4.1.7 on 2023-04-04 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0030_admin_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('company_name', models.CharField(default=None, max_length=250, null=True)),
                ('company_logo', models.FileField(default=None, max_length=500, null=True, upload_to='settings/')),
                ('company_email', models.CharField(default=None, max_length=250, null=True)),
                ('company_mobile', models.CharField(default=None, max_length=250, null=True)),
                ('copyright', models.CharField(default=None, max_length=250, null=True)),
                ('shopaddress', models.CharField(default=None, max_length=250, null=True)),
                ('status', models.CharField(default=None, max_length=250, null=True)),
            ],
        ),
    ]
