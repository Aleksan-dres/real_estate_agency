from django.db import migrations

def auto_status_new_building(apps,schema_edition): 
    Flat = apps.get_model('property', 'Flat') 
    Flat.objects.filter(construction_year__gte=2015).update(new_building=True)
    Flat.objects.exclude(construction_year__gte=2015).update(new_building=False)

class Migration(migrations.Migration):

    dependencies = [
        ('property', '0004_flat_new_building'),
    ]

    operations = [ 
        migrations.RunPython(auto_status_new_building)
    ]


