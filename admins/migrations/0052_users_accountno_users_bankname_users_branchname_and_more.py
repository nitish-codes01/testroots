# Generated by Django 4.1.7 on 2023-05-02 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0051_fieldissue_delete_document'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='accountno',
            field=models.CharField(default=None, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='users',
            name='bankname',
            field=models.CharField(default=None, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='users',
            name='branchname',
            field=models.CharField(default=None, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='users',
            name='ifsc',
            field=models.CharField(default=None, max_length=250, null=True),
        ),
    ]
