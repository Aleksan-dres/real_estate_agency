

from django.db import migrations


def set_owner_flat_relations(apps, schema_edition):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')

    for flat in Flat.objects.all():
        owner = Owner.objects.filter(
            full_name=flat.owner,
            phonenumber=flat.owners_phonenumber
        ).first()

        if owner:
            owner.flats.add(flat)


def reverse_func(apps, schema_edition):
    Owner = apps.get_model('property', 'Owner')
    for owner in Owner.objects.all():
        owner.flats.clear()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0011_auto_20260202_1737'),
    ]

    operations = [migrations.RunPython(set_owner_flat_relations, reverse_func),
                  ]
