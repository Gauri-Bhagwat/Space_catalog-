# Generated by Django 5.0.7 on 2024-11-15 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='spaceobject',
            name='distance_from_earth',
        ),
        migrations.RemoveField(
            model_name='spaceobject',
            name='object_type',
        ),
        migrations.AddField(
            model_name='spaceobject',
            name='category',
            field=models.CharField(choices=[('planet', 'Planet'), ('star', 'Star'), ('galaxy', 'Galaxy'), ('comet', 'Comet')], default='planet', max_length=20),
        ),
        migrations.AddField(
            model_name='spaceobject',
            name='created_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='spaceobject',
            name='distance',
            field=models.FloatField(blank=True, help_text='Distance from Earth in light-years', null=True),
        ),
        migrations.AddField(
            model_name='spaceobject',
            name='size',
            field=models.FloatField(blank=True, help_text='Size in kilometers or other units', null=True),
        ),
        migrations.AddField(
            model_name='spaceobject',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]