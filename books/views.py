from django.shortcuts import render
from django.views.generic import ListView
from .models import CategoryModel, BookModel, AudioModel




def indexView(request):
    cate = CategoryModel.objects.all()
    books = BookModel.objects.all()

    data = {
        "categories" : cate,
        "books": books
    }
    return render(request, "index.html", data)



def categoriesView(request, cate_id):
    by_categories = BookModel.objects.all().filter(category=cate_id)
    cate_name = CategoryModel.objects.get(pk=int(cate_id))
    
    data = {
        "by_categories": by_categories,
        "cate_name" : cate_name.name
        
    }
    return render(request, "books/categories.html", data)



def my_booksView(request, user_id):
    users_book = BookModel.objects.all().filter(user=user_id)

    data = {
        "users_book": users_book
        
    }
    return render(request, "books/my_books.html", data)


def audiosView(request, book_id):
    book = BookModel.objects.get(pk=int(book_id))
    audios = AudioModel.objects.all().filter(book=book_id)
   

    data = {
    
        "book_":book,
        "audios":audios
    }
    return render(request, "books/audios.html", data)




def search_results(request):
    if request.method == 'POST':
        search_query = request.POST.get('search_query', '')

        results = BookModel.objects.filter(
            book_name__icontains=search_query
        )

        return render(request, 'books/search_results.html', {'results': results, 'query': search_query})

    return render(request, 'index.html')  






