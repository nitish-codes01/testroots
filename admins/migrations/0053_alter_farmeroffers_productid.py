# Generated by Django 4.1.7 on 2023-05-11 09:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0052_users_accountno_users_bankname_users_branchname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmeroffers',
            name='productid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='farmeroffers', to='admins.product'),
        ),
    ]