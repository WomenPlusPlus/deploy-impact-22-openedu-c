from django.db import models
from django.urls import reverse

# Create your models here.
# id is not required, given that one imports from django model


class Author(models.Model):
    Name=models.CharField(max_length=40)
    Email=models.EmailField(max_length=40)
    Phone=models.CharField(max_length=40, blank=True, null=True)
    Website_url=models.URLField(max_length=300, blank=True, null=True)

class Publisher(models.Model):
    Name=models.CharField(max_length=40)
    Website_url=models.URLField(max_length=300)


class MediaChannel(models.Model):
    Name = models.CharField(max_length=50)
    Website_url = models.URLField(max_length=300)


class Institution(models.Model):
    Name = models.CharField(max_length=50)
    Website_url = models.URLField(max_length=300)
    id_media_channel = models.ForeignKey(MediaChannel, on_delete=models.PROTECT, blank=True, null=True)



# Model that contains the new educational material entries
class EduMaterial(models.Model):
    title = models.CharField(max_length=120)  # we can change this default to a larger value if required
    description = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.PROTECT, blank = True, null = True)
    publisher = models.ForeignKey(Publisher, on_delete=models.PROTECT, blank = True, null = True)
    Media_Channel = models.ForeignKey(MediaChannel, on_delete=models.PROTECT, blank = True, null = True)
    Institution = models.ForeignKey(Institution, on_delete=models.PROTECT, blank=True, null=True)
    reviewed = models.BooleanField(default=False)

    def __str__(self):
        return self.title  # this is the return one gets when referenced to this model
        # for example at the admin page

    def get_absolute_url(self):
        return reverse('edu_data:detail', args=[self.id, ])


# Model that contains the categories entries
class Topics(models.Model):
    name = models.CharField(max_length=50)


# Model that contains the link between the model EduMaterial and the categories, a new model is required given that
# one project can belong to more than one category
class EduMaterial_topics(models.Model):
    edumaterial = models.ForeignKey(EduMaterial, on_delete=models.CASCADE)  # cascade, for deleting the entry if the
    # educational material is deleted
    topics = models.ForeignKey(Topics, on_delete=models.CASCADE, default='')  # cascade, for deleting the entry if the
    # category is deleted


class Skill(models.Model):
    name = models.CharField(max_length=50)


class EduMaterial_skill(models.Model):
    edumaterial = models.ForeignKey(EduMaterial, on_delete=models.CASCADE)  # cascade, for deleting the entry if the
    # educational material is deleted
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE, default=0)  # cascade, for deleting the entry if the
    # category is deleted


class CompetencyLevel(models.Model):
    name = models.CharField(max_length=50)


class EduMaterial_level(models.Model):
    edumaterial = models.ForeignKey(EduMaterial, on_delete=models.CASCADE, default=0)  # cascade, for deleting the entry if the
    # educational material is deleted
    level = models.ForeignKey(CompetencyLevel, on_delete=models.CASCADE, default=0)

class ToWhom(models.Model):
    name = models.CharField(max_length=50)

class EduMaterial_towhom(models.Model):
    edumaterial = models.ForeignKey(EduMaterial,
                                       on_delete=models.CASCADE)  # cascade, for deleting the entry if the
    # educational material is deleted
    towhom = models.ForeignKey(ToWhom, on_delete=models.CASCADE, default='')


class MaterialType(models.Model):
    name = models.CharField(max_length=50)


class EduMaterial_materialtype(models.Model):
    edumaterial = models.ForeignKey(EduMaterial, on_delete=models.CASCADE)  # cascade, for deleting the entry if the
    # educational material is deleted
    materialtype = models.ForeignKey(MaterialType, on_delete=models.CASCADE, default=0)


# This model is created to save the similarities between the project. A JSONField is chosen for being able to save a
# many to many relationship. A new JSON entry will be generated depending on the required time to calculate the
# similarity between projects. If this occurs fast, the similarity can ba calculated after each project upload.
# Otherwise, this calculation should be done on a daily basis or a weekly basis.
class RelatedProjects(models.Model):
    edumaterial = models.ForeignKey(EduMaterial, on_delete=models.CASCADE, default=0)
    date = models.DateTimeField(auto_now_add=True)  # auto_now_add to include the curretn datetime
    similarity = models.JSONField(null=True)


class embeddings(models.Model):
    edumaterial = models.ForeignKey(EduMaterial, on_delete=models.CASCADE, default=0)
    embeding = models.JSONField(null=True)