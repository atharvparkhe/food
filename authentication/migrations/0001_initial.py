# Generated by Django 4.0.2 on 2022-02-23 15:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerModel',
            fields=[
                ('baseuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('newsletter', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'customer',
            },
            bases=('base.baseuser',),
        ),
        migrations.CreateModel(
            name='ShopkeeperModel',
            fields=[
                ('baseuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('aadhar_card', models.CharField(max_length=16, unique=True)),
                ('gst_number', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'db_table': 'shopkeeper',
            },
            bases=('base.baseuser',),
        ),
        migrations.CreateModel(
            name='CustomerAddress',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('address', models.TextField()),
                ('pincode', models.CharField(max_length=100)),
                ('landmark', models.CharField(max_length=50)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer_address', to='authentication.customermodel')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
