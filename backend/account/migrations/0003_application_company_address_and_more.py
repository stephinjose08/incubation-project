# Generated by Django 4.1.2 on 2022-10-25 13:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0002_slot_room_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='company_Address',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='alloted_slot',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='company_email',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='company_name',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='name',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='number_of_clients',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='number_of_emp',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='number_of_room',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='phone',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='application', to=settings.AUTH_USER_MODEL),
        ),
    ]
