# Generated by Django 4.1.7 on 2023-04-05 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0032_privacypolicy'),
    ]

    operations = [
        migrations.CreateModel(
            name='Termcondition',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('terms', models.CharField(default=None, max_length=15000, null=True)),
            ],
        ),
    ]