# Generated by Django 4.1.7 on 2023-04-15 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0041_farmeroffers'),
    ]

    operations = [
        migrations.CreateModel(
            name='buyeroffers',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('offerdate', models.CharField(default=None, max_length=250, null=True)),
                ('productid', models.CharField(default=None, max_length=250, null=True)),
                ('quantity', models.CharField(default=None, max_length=250, null=True)),
                ('price', models.CharField(default=None, max_length=250, null=True)),
                ('bidamount', models.CharField(default=None, max_length=250, null=True)),
                ('delivery_location', models.CharField(default=None, max_length=250, null=True)),
                ('offerstatus', models.CharField(default=None, max_length=250, null=True)),
                ('buyer_id', models.CharField(default=None, max_length=250, null=True)),
            ],
            options={
                'db_table': 'buyer_offers',
            },
        ),
    ]
