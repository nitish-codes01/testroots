# Generated by Django 4.1.7 on 2023-04-15 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0042_buyeroffers'),
    ]

    operations = [
        migrations.AddField(
            model_name='buyeroffers',
            name='farmeroffer_id',
            field=models.CharField(default=None, max_length=250, null=True),
        ),
    ]
