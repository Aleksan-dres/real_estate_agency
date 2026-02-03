

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0006_complaint'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='flat',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='likes_flats', to=settings.AUTH_USER_MODEL),
        ),
    ]
