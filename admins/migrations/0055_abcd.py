# Generated by Django 4.1.7 on 2023-05-11 10:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0054_alter_farmeroffers_productid'),
    ]

    operations = [
        migrations.CreateModel(
            name='abcd',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default=None, max_length=250, null=True)),
                ('productid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product', to='admins.roles')),
            ],
            options={
                'db_table': 'abcd',
            },
        ),
    ]