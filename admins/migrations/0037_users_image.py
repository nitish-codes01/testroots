# Generated by Django 4.1.7 on 2023-04-10 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0036_settings_company_favicon_alter_settings_company_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='image',
            field=models.FileField(default=None, max_length=500, null=True, upload_to='user/'),
        ),
    ]
