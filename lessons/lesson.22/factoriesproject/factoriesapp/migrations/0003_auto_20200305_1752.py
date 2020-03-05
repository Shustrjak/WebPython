# Generated by Django 2.2.11 on 2020-03-05 17:52

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('factoriesapp', '0002_user_nickname'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='factoriesapp.User')),
                ('internal_id', models.IntegerField()),
                ('internal_email', models.EmailField(max_length=254)),
            ],
            options={
                'abstract': False,
            },
            bases=('factoriesapp.user',),
        ),
        migrations.AddField(
            model_name='user',
            name='birth_dt',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='birth_month',
            field=models.IntegerField(default=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='lang',
            field=models.CharField(default='en', max_length=2),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(choices=[('Pending', 'pending'), ('Awaiting shipment', 'awaiting_shipment'), ('Shipped', 'shipped'), ('Delivered', 'delivered')], max_length=30)),
                ('shipped_on', models.DateTimeField(null=True)),
                ('delivered_on', models.DateTimeField(null=True)),
                ('shipped_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='factoriesapp.Employee')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]