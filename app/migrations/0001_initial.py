# Generated by Django 4.1.3 on 2023-01-28 10:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('locality', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=50)),
                ('zipcode', models.IntegerField()),
                ('state', models.CharField(choices=[('karnataka', 'karnataka'), ('maharastra', 'maharastra'), ('kerala', 'kerala'), ('madya-pradesh', 'madya-pradesh'), ('west bangal', 'west bangal'), ('goa', 'goa'), ('andra pradesh', 'andra pradesh'), ('sikkim', 'sikkim'), ('Bihar', 'Bihar')], max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('selling_price', models.FloatField()),
                ('discount_price', models.FloatField()),
                ('discription', models.TextField()),
                ('brand', models.CharField(max_length=100)),
                ('catogery', models.CharField(choices=[('M', 'mobile'), ('L', 'laptop'), ('TW', 'topware'), ('BW', 'bottomware')], max_length=10)),
                ('product_image', models.ImageField(upload_to='productimg')),
            ],
        ),
        migrations.CreateModel(
            name='OrderPlaced',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('orderd_date', models.DateTimeField(auto_now_add=True)),
                ('staus', models.CharField(choices=[('accepted', 'accepted'), ('packed', 'packed'), ('on the way', 'on the way'), ('Deliverd', 'Deliverd'), ('cancel', 'cancel')], default='pending', max_length=50)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.customer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
