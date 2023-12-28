from django.contrib.postgres.search import SearchVector, SearchQuery

from .models import Product
from django.db.models import Q


def q_search(query):
    # поиск по id
    if query.isdigit() and len(query) <= 5:
        return Product.objects.filter(id=int(query))

    # поиск по названию и описанию
    return Product.objects.annotate(
        search=SearchVector('name', 'description')) \
        .filter(search=query)

    # поиск на коленке
    # q_objects = Q()
    # keywords = [word for word in query.split() if len(word) > 2]
    # for token in keywords:
    #     q_objects |= Q(name__icontains=token)
    #     q_objects |= Q(description__icontains=token)
    # return Product.objects.filter(q_objects)
