# Generated by Django 4.1.7 on 2023-04-11 09:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0038_product_discount_product_discounted_price_and_more'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='aboutus',
            table='aboutus',
        ),
        migrations.AlterModelTable(
            name='privacypolicy',
            table='privacy_policy',
        ),
        migrations.AlterModelTable(
            name='settings',
            table='settings',
        ),
        migrations.AlterModelTable(
            name='termcondition',
            table='term_condition',
        ),
    ]
