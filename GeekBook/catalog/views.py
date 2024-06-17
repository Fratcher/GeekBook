from django.shortcuts import render
from django.views import generic


# Create your views here.
from .models import Book, Month, Day, Image, Video

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_months = Month.objects.all().count()

    # Available books (status = 'a')
    #num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default.
    num_image= Image.objects.count()

    team = [
        {'name': 'Riley King', 'role': 'Member 1', 'image_url': '/static/images/member1.jpg'},
        {'name': 'Rachel Strober', 'role': 'Member 2', 'image_url': '/static/images/member1.jpg'},
        {'name': 'Piper Smith', 'role': 'Member 3', 'image_url': '/static/images/member1.jpg'},
        {'name': 'Sara Morgan', 'role': 'Member 4', 'image_url': '/static/images/member1.jpg'},
        {'name': 'Myrie Murphy', 'role': 'Member 5', 'image_url': '/static/images/member1.jpg'},
        # Add more team members as needed...
    ]

    
    context = {
        'num_books': num_books,
        'num_instances': num_months,
        #'num_instances_available': num_instances_available,
        'num_authors': num_image,
        'team':team
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)



class BookListView(generic.ListView):
    model = Book

class BookDetailView(generic.DetailView):
    model = Book

