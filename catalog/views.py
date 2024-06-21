from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Book, Category


def book_list(request):
    books = Book.objects.all()
    return render(request, 'catalog/book_list.html', {'books': books})


def add_book(request):
    categories = Category.objects.all()

    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        description = request.POST.get('description')
        price = request.POST.get('price')
        published_date = request.POST.get('published_date')
        category_id = request.POST.get('category')
        category = get_object_or_404(Category, id=int(category_id))

        try:
            new_book = Book(
                title=title,
                author=author,
                description=description,
                price=price,
                published_date=published_date,
                category=category
            )
            new_book.full_clean()
        except Exception as e:
            return HttpResponse(f'Invalid values: {e}')
        else:
            new_book.save()
            return redirect('catalog:book_list')

    return render(request, 'catalog/add_book.html', {'categories': categories})
