

import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0009_auto_20260118_2130'),
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200, verbose_name='ФИО владельца')),
                ('phonenumber', models.CharField(max_length=20, verbose_name='Номер владельца')),
                ('pure_phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region='RU', verbose_name='Нормализованный номер владельца')),
                ('flats', models.ManyToManyField(blank=True, related_name='owners', to='property.flat', verbose_name='Квартиры в собственности')),
            ],
        ),
    ]
