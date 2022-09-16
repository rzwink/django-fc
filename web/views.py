from django.shortcuts import render
from django.views import generic

from web.models import Content
from web.models import News
from web.models import Product
from web.models import Sponsor


def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Product.objects.all().count()

    context = {
        "num_books": num_books,
        "product_list": Product.objects.filter(is_active=True),
        "sponsor_list": Sponsor.objects.filter(is_active=True),
        "news_list": News.objects.filter(is_active=True),
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, "web/index.html", context=context)


class ProductListView(generic.ListView):
    model = Product
    context_object_name = "product_list"
    queryset = Product.objects.filter(is_active=True)


def get_content(slug):
    obj1, _ = Content.objects.get_or_create(slug=slug)
    obj2, _ = Content.objects.get_or_create(slug=slug + "-title")
    return {"content": obj1.content, "title": obj2.content}
