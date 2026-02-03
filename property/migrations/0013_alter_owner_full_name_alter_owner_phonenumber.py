

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0012_auto_20260203_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='full_name',
            field=models.CharField(db_index=True, max_length=200, verbose_name='ФИО владельца'),
        ),
        migrations.AlterField(
            model_name='owner',
            name='phonenumber',
            field=models.CharField(db_index=True, max_length=20, verbose_name='Номер владельца'),
        ),
    ]
