import json

from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic
from book.models import Book
from .forms import SearchForm


class HomeView(generic.ListView):
    queryset = Book.objects.all()
    template_name = "home/index.html"

    def get_queryset(self):
        queryset = self.queryset.exclude(image__in=["", None]).order_by("-created_at")[
            :8
        ]
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["books"] = self.get_queryset()
        return context


class CatalogView(generic.ListView):
    queryset = Book.objects.all()
    template_name = "catalog/index.html"
    paginate_by = 12

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["books"] = self.get_queryset()
        return context


def search(request):
    if request.method == "POST":
        form = SearchForm(request.POST)
        query = form.cleaned_data["query"]
        if form.is_valid():
            context = {
                "query": query,
                "books": Book.objects.filter(title__icontains=query),
            }
            return render(request, "pages/search_books.html", context)
    return HttpResponseRedirect(reverse("home:index"))


def search_auto(request):
    if request.is_ajax():
        q = request.GET.get("term", "")
        books = Book.objects.filter(title__icontains=q)
        results = []
        for item in books:
            results.append(item.title)
        data = json.dumps(results)
    else:
        data = "fail"
    mimetype = "application/json"
    return HttpResponse(data, mimetype)
