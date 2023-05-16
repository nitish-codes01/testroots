# Generated by Django 4.1.7 on 2023-05-12 05:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0056_alter_abcd_table'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='farmeroffers',
            name='productid',
        ),
        migrations.AddField(
            model_name='farmeroffers',
            name='roleid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='roles', to='admins.product'),
        ),
    ]