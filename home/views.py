from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
@login_required()
def home(request):
    post = [
        {
            'title': "Hello World",
            'author': "Janes Bond",
            'body': "By including these lines in your settings, Django should now be able to serve your static files "
                    "correctly. Remember to run the collectstatic management command whenever you make changes to "
                    "your static files or deploy your project to a production environment.If you have any further "
                    "questions or issues, feel free to ask!",
            'comments': [
                {
                    'user': 'Ni No',
                    'comment': "This is an awesome article"
                },
                {
                    'user': 'Harry',
                    'comment': "This is an awesome article"
                },
                {
                    'user': 'Maguire',
                    'comment': "This is an awesome article"
                }
            ]
        }
    ]
    context = {
        'title': "Welcome",
        'posts': post
    }
    return render(request, 'home/index.html', context=context)
