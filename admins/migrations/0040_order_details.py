# Generated by Django 4.1.7 on 2023-04-11 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0039_alter_aboutus_table_alter_privacypolicy_table_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order_details',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('order_id', models.CharField(default=None, max_length=250, null=True)),
                ('product_id', models.CharField(default=None, max_length=250, null=True)),
                ('seller_id', models.CharField(default=None, max_length=250, null=True)),
                ('qty', models.CharField(default=None, max_length=250, null=True)),
                ('price', models.CharField(default=None, max_length=250, null=True)),
                ('discount', models.CharField(default=None, max_length=250, null=True)),
                ('tax', models.CharField(default=None, max_length=250, null=True)),
                ('delivery_status', models.CharField(default=None, max_length=250, null=True)),
                ('datetime', models.CharField(default=None, max_length=250, null=True)),
            ],
            options={
                'db_table': 'order_details',
            },
        ),
    ]
