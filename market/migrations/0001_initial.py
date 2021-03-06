# Generated by Django 2.1.7 on 2019-03-09 09:37

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Product category', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('description', models.TextField(blank=True, help_text='brief description of the product', max_length=1000)),
                ('image', models.ImageField(blank=True, default='default.png', upload_to='')),
                ('stock', models.PositiveIntegerField(default=1)),
                ('category', models.ManyToManyField(blank=True, help_text='Categories for this product', to='market.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, unique=True)),
                ('address', models.TextField(max_length=500, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='seller',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='market.Seller'),
        ),
    ]
