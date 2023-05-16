# Generated by Django 4.1.7 on 2023-04-17 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0045_farmeroffers_totalamount'),
    ]

    operations = [
        migrations.CreateModel(
            name='transactions',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('treasactiondate', models.CharField(default=None, max_length=250, null=True)),
                ('transaction_id', models.CharField(default=None, max_length=250, null=True)),
                ('cropid', models.CharField(default=None, max_length=250, null=True)),
                ('farmer_id', models.CharField(default=None, max_length=250, null=True)),
                ('farmer_amount', models.CharField(default=None, max_length=250, null=True)),
                ('buyer_id', models.CharField(default=None, max_length=250, null=True)),
                ('buyer_amount', models.CharField(default=None, max_length=250, null=True)),
                ('logistics_id', models.CharField(default=None, max_length=250, null=True)),
                ('logistics_amount', models.CharField(default=None, max_length=250, null=True)),
                ('status', models.CharField(default=None, max_length=250, null=True)),
            ],
            options={
                'db_table': 'transactions',
            },
        ),
    ]
