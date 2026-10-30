from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.db.models import Avg, Count, Q

from .models import Book
from django.utils.text import slugify

def index(request):
     # Ուղղում ենք բազայի այն գրքերը, որոնք տեխնիկական պատճառով slug չունեն
    
    books_to_fix = Book.objects.filter(Q(slug="") | Q(slug__isnull=True))
    
    #ավտոմատ ուղղում ենք բազայի այն գրքերը, որոնք slug չունեն
    for book in books_to_fix:
        book.slug = slugify(book.title,allow_unicode=True )
        book.save()
    #արդեն վերցնում ենք բոլոր գրքերը    
    books = Book.objects.all().order_by("title")
    num_books = books.count()
    avg_data = books.aggregate(rating_avg=Avg("rating"))#հաշվում ենք միջինը և վերցնում ենք միայն թիվը
    avg_rating = avg_data['rating_avg']

    return render(request, "book_outlet/index.html",{
                   "books": books,
                    "total_number_of_books":num_books,
                    "average_rating":avg_rating,
                    })


def book_detail(request, slug):
    # try:
    #     book = Book.objects.get(pk=id)
    # except:
    #     raise Http404()
    book = get_object_or_404(Book, slug=slug)
    return render(request,"book_outlet/book_detail.html", {
        "book": book
        # "title":book.title,
        # "author":book.author,
        # "rating":book.rating,
        # "is_bestseller":book.is_bestselling,
    })