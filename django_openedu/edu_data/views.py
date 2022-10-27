from django.shortcuts import render, get_object_or_404
# import the models to be able to access the data and get the context
from .models import EduMaterial
from django.db.models import Q  # required for making more than one query
# https://books.agiliq.com/projects/django-orm-cookbook/en/latest/query_relatedtool.html


# Create your views here.
# CRUD - create retrieve update delete

# create a view to retrieve all the educational material.
# with a function_base_view from django, which take a request and shows data in someway
def edumaterial_list_view(request):
    edu_materials = EduMaterial.objects.all()
    context = {
        'edu_materials': edu_materials
    }
    return render(request, "edumaterial/home.html", context)  # request, template, context

# view giving the detail of the educational material
def detail_page(request, id):
    edu_material = get_object_or_404(EduMaterial, pk=id)
    context = {
        'edu_material': edu_material
    }
    return render(request, "edumaterial/detail.html", context)  # request, template, context


def search(request):
    query = None
    results = []
    if request.method == "GET":
        query = request.GET.get('search')  # where GET is the method used in th html file when creating the form
        results = EduMaterial.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query))
        # If query is either in title or in description then get the results
    return render(request, 'edumaterial/search.html', {'query': query,
                                                       'results': results})
