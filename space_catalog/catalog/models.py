from django.db import models

class SpaceObject(models.Model):
    CATEGORY_CHOICES = [
        ('planet', 'Planet'),
        ('star', 'Star'),
        ('galaxy', 'Galaxy'),
        ('comet', 'Comet'),
        # Add other categories as needed
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='planet')
    description = models.TextField()
    distance = models.FloatField(null=True, blank=True, help_text="Distance from Earth in light-years")
    size = models.FloatField(null=True, blank=True, help_text="Size in kilometers or other units")
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name



class Note(models.Model):
    spaceobject = models.ForeignKey('SpaceObject', on_delete=models.CASCADE, related_name='notes')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Note for {self.spaceobject.name} (Created: {self.created_at.strftime('%Y-%m-%d')})"

