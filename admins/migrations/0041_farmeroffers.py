# Generated by Django 4.1.7 on 2023-04-15 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0040_order_details'),
    ]

    operations = [
        migrations.CreateModel(
            name='farmeroffers',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('offerdate', models.CharField(default=None, max_length=250, null=True)),
                ('productid', models.CharField(default=None, max_length=250, null=True)),
                ('quantity', models.CharField(default=None, max_length=250, null=True)),
                ('price', models.CharField(default=None, max_length=250, null=True)),
                ('pickuplocation', models.CharField(default=None, max_length=250, null=True)),
                ('offerstatus', models.CharField(default=None, max_length=250, null=True)),
                ('farmer_id', models.CharField(default=None, max_length=250, null=True)),
            ],
            options={
                'db_table': 'farmer_offers',
            },
        ),
    ]