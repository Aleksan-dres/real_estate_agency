

from django.db import migrations

def auto_status_new_building(apps,schema_edition): 
    Flat = apps.get_model('property', 'Flat') 
    for flat in Flat.objects.all():  
        if flat.construction_year is not None and flat.construction_year >=2015: 
            flat.new_building = True 
        else: 
            flat.new_building = False 
        flat.save() 

class Migration(migrations.Migration):

    dependencies = [
        ('property', '0004_flat_new_building'),
    ]

    operations = [ 
        migrations.RunPython(auto_status_new_building)
    ]
