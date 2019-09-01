from django.shortcuts import render
from Book.models import Books

# Create your views here.

def view_all_books(request):
    objs = Books.objects.all()
    
    print(objs)
    context = {
        'books': objs
    }
    return render(request, 'view_all_books.html', context=context)

def view_single_book(request, book_id):
    objs = Books.object.get(id=book_id)
    
    context = {
        'book': objs
    }
    return render(request, 'view_single_book.html',context=context)

