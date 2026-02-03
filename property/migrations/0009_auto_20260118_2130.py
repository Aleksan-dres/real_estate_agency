

from django.db import migrations 
from phonenumbers import parse, format_number, PhoneNumberFormat
from phonenumbers import NumberParseException


def auto_phone_number(apps,schema_edition): 
    Flat = apps.get_model('property', 'Flat') 
    for flat in Flat.objects.all():  
        if flat.owners_phonenumber: 
            try: 
                parse_number = parse(flat.owners_phonenumber, 'RU') 
                normal_number = format_number(parse_number, PhoneNumberFormat.E164) 
                flat.owner_pure_phone = normal_number 
                flat.save() 

            except NumberParseException: 
                pass 

            
class Migration(migrations.Migration):

    dependencies = [
        ('property', '0008_flat_owner_pure_phone'),
    ]

    operations = [migrations.RunPython(auto_phone_number)
    ]
