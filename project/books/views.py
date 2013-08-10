# Create your views here.
from django.http import HttpResponseRedirect,HttpResponse
from django.utils import simplejson

from books.models import Book

def data(request):
    
    books   = Book.objects.all()
    results = []
    for book in books:
        results.append({"id": book.id, "name": book.name, "author": str(book.author.username), "publisher": book.publisher, "copies": str(book.no_of_copies_sold)})

    return HttpResponse(simplejson.dumps(results), mimetype = 'application/json')
