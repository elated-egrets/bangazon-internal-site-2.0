# Generated by Django 2.1 on 2018-08-20 14:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_auto_20180820_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date_closed',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='payment_type',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='website.PaymentType'),
        ),
    ]