# Generated by Django 3.0 on 2022-11-20 22:56

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('paternal_surname', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=255)),
            ],
            options={
                'permissions': [('can_add_customer', 'can add customer'), ('can_edit_customer', 'can edit customer propperties'), ('can_delete_customer', 'can delete customer')],
            },
        ),
        migrations.CreateModel(
            name='PaymentsCustomer',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=6)),
                ('product_name', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Customer')),
            ],
            options={
                'permissions': [('can_edit_payment', 'can edit payment propperties'), ('can_delete_payment', 'can delete payment')],
            },
        ),
    ]
