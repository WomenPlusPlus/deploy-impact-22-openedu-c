from django.shortcuts import render, get_object_or_404
# import the models to be able to access the data and get the context
from .models import EduMaterial, RelatedProjects, Topics, MaterialType, EduMaterial_topics, EduMaterial_materialtype
from django.db.models import Q  # required for making more than one query
import sys

# this is the only way to import function from the ../../NLP folder
# see here: https://www.geeksforgeeks.org/python-import-module-from-different-directory/
sys.path.insert(0, '../NLP/')
from semantic_search import semantic_search

#import os
#os.environ['KMP_DUPLICATE_LIB_OK']='True'
# https://books.agiliq.com/projects/django-orm-cookbook/en/latest/query_relatedtool.html


# Create your views here.
# CRUD - create retrieve update delete

def is_valid_queryparam(param):
    return param != '' and param is not None

# create a view to retrieve all the educational material.
# with a function_base_view from django, which take a request and shows data in someway
def edumaterial_list_view(request):
    edu_materials = EduMaterial.objects.all()
    categories = Topics.objects.all()
    print(categories)
    formats = MaterialType.objects.all()
    context = {
        'edu_materials': edu_materials,
        'categories': categories,
        'formats': formats
    }
    return render(request, "edumaterial/home.html", context)  # request, template, context

# view giving the detail of the educational material
def detail_page(request, id):
    edu_material = get_object_or_404(EduMaterial, pk=id)
    related_projects = RelatedProjects.objects.filter(edumaterial_id__exact=id).order_by('-date').first()

    #last_three = EduMaterial.objects.all().order_by('-id')[:3]#filter(since=since).order_by('-id')[:10]
    #last_three_ascending_order = reversed(last_three)
    #print(list(last_three_ascending_order))
    #print(len(related_projects.similarity))
    #print(id)
    #print(related_projects.similarity)
    context = {
        'edu_material': edu_material,
        'related_projects': EduMaterial.objects.filter(id__in=related_projects.similarity),
        #'last_three_edu': last_three_ascending_order
    }
    return render(request, "edumaterial/detail.html", context)  # request, template, context


def apply_main_filters(results, request):
    topic = request.GET.get('category')
    mformat = request.GET.get('materialformat')
    # print(format)
    if is_valid_queryparam(topic) and topic != 'Choose...':
        ids = EduMaterial_topics.objects.filter(topics__exact=topic).values_list('edumaterial',
                                                                                 flat=True)
        results = results.filter(id__in=ids)
    if is_valid_queryparam(mformat) and mformat != 'Choose...':
        ids = EduMaterial_materialtype.objects.filter(materialtype__exact=mformat).values_list('edumaterial',
                                                                                              flat=True)
        results = results.filter(id__in=ids)
    return results


def search(request):
    query = None
    results = []
    if request.method == "GET":
        query = request.GET.get('search')  # where GET is the method used in th html file when creating the form
        results = EduMaterial.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query))

        print(results)
        dic_count = {project.title: project.title.lower().count(query.lower()) + project.description.lower().count(query.lower()) for project in results}
        print(dic_count)
        # If query is either in title or in description then get the results

        results = apply_main_filters(results, request)
    return render(request, 'edumaterial/search.html', {'query': query,

                                                       'results': results})
def search_filter(request):
    query = None
    results = []
    if request.method == "GET":
        query = request.GET.get('search')  # where GET is the method used in th html file when creating the form
        # if is_valid_queryparam(query):
        results = EduMaterial.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query))
        print(results)
        results = apply_main_filters(results, request)
        print(results)
        dic_count = {
            project.title: project.title.lower().count(query.lower()) + project.description.lower().count(query.lower())
            for project in results}
        print(dic_count)
        dic_count = {
            project.title: project.pk
            for project in results}
        print(dic_count)

        # If query is either in title or in description then get the results
    return render(request, 'edumaterial/search.html', {'query': query,
                                                       'results': results})


def search_NLP(request):
    query = None
    results = []
    if request.method == "GET":

        query = request.GET.get('search')  # where GET is the method used in th html file when creating the form
        #if is_valid_queryparam(search):
            #pass
            # TODO make an if for returning a text if no word is given in the search
        ids = semantic_search(query)
        results = EduMaterial.objects.filter(id__in=ids)

        results = apply_main_filters(results, request)

        # If query is either in title or in description then get the results
    return render(request, 'edumaterial/search.html', {'query': query,
                                                       'results': results})
