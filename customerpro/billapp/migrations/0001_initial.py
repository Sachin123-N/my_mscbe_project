# Generated by Django 5.0.4 on 2024-04-07 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=20)),
                ('bill_amount', models.IntegerField()),
                ('bill_date', models.DateField()),
                ('payment_mode', models.CharField(choices=[('ON', 'Online Payment'), ('OL', 'Offline Payment')], max_length=10)),
            ],
        ),
    ]
