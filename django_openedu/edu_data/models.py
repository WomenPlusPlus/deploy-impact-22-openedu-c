from django.db import models
from django.urls import  reverse

# Create your models here.
# id is not required, given that one imports from django model

# Model that contains the new educational material entries
class Author(models.Model):
    Name=models.CharField(max_length=40)
    Email=models.EmailField(max_length=40)
    Phone=models.CharField(max_length=40, blank = True, null = True)
    Website_url=models.URLField(max_length=300, blank = True, null = True)

class Publisher(models.Model):
    Name=models.CharField(max_length=40)
    Website_url=models.URLField(max_length=300)


class Media_Channel(models.Model):
    Name=models.CharField(max_length=50)
    Website_url=models.URLField(max_length=300)


class Institution(models.Model):
    Name=models.CharField(max_length=50)
    Website_url=models.URLField(max_length=300)
    id_media_channel = models.ForeignKey(Media_Channel, on_delete=models.PROTECT, blank = True, null = True)


class EduMaterial(models.Model):
    title = models.CharField(max_length=120)  # we can change this default to a larger value if required
    description = models.TextField()
    id_author = models.ForeignKey(Author, on_delete=models.PROTECT, blank = True, null = True)
    id_publisher = models.ForeignKey(Publisher, on_delete=models.PROTECT, blank = True, null = True)
    id_Media_Channel = models.ForeignKey(Media_Channel, on_delete=models.PROTECT, blank = True, null = True)
    id_Institution = models.ForeignKey(Institution, on_delete=models.PROTECT, blank=True, null=True)



    def __str__(self):
        return self.title  # this is the return one gets when referenced to this model
        # for example at the admin page
    def get_absolute_url(self):
        return reverse('edu_data:detail', args=[self.id, ])


# Model that contains the categories entries
class Categories(models.Model):
    categories = models.CharField(max_length=50)


# Model that contains the link between the model EduMaterial and the categories, a new model is required given that
# one project can belong to more than one category
class EduMaterial_Categories(models.Model):
    id_edumaterial = models.ForeignKey(EduMaterial, on_delete=models.CASCADE)  # cascade, for deleting the entry if the
    # educational material is deleted
    id_category = models.ForeignKey(Categories, on_delete=models.CASCADE)  # cascade, for deleting the entry if the
    # category is deleted




