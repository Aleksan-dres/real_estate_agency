from django.db import migrations


def create_owner(apps, schema_edition): 
    Flat = apps.get_model("property", "Flat") 
    Owner = apps.get_model("property", "Owner") 

    for flat in Flat.objects.all().iterator(): 
        owner, created = Owner.objects.get_or_create(
            full_name=flat.owner,
            defaults={ 
            "phonenumber": flat.owners_phonenumber, 
            "pure_phone": flat.owner_pure_phone,
            },
        ) 

        if not created: 
            if not owner.phonenumber and flat.owners_phonenumber: 
                owner.phonenumber = flat.owners_phonenumber 
            if not owner.pure_phone and flat.owner_pure_phone: 
                owner.pure_phone = flat.owner_pure_phone 
                owner.save()  


def reverse_func(apps, schema_edition): 
    Owner = apps.get_model("property", "Owner") 
    Owner.objects.all().delete() 


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0010_owner'),
    ]

    operations = [migrations.RunPython(create_owner, reverse_func),
    ]

