from django.shortcuts import render
from django.views import generic
from django.contrib.auth.models import User #imports User
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.utils.deprecation import MiddlewareMixin
from django.urls import resolve, reverse
from django.http import HttpResponseRedirect
from django.conf import settings


# Create your views here.
from .models import Book, Month, Day, Image, Video

@login_required
def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_months = Month.objects.all().count()


    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

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
        'team':team,
        'num_visits': num_visits
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

@method_decorator(login_required, name='dispatch')
class BookListView(generic.ListView):
    model = Book
    paginate_by = 10


class BookDetailView(generic.DetailView):
    model = Book


@login_required
def profile(request, username=None):
    if username:
        post_owner = get_object_or_404(User, username=username)

    else:
        post_owner = request.user

    args1 = {
        'post_owner': post_owner,
      }
    return render(request, 'profile.html', args1)

