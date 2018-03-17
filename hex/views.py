from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from .models import Volunteer, Benefactor, Organizer

# Create your views here.
def signup(request):
    #print(request.POST)
    if request.method == 'POST':
        dictionary = request.POST
        print(dictionary)
        dummy_data = {"username" : "dupex",
                        "fullname" : "Jan Boratynski",
                        "password" : "dupa123",
                        "telephone" : "997",
                        "email" : "jan@wsadzicitam.pl",
                        "usertype" : "Benefactor"}

        #TODO INPUT VERIFICATION
        errors = {"username" : False, "email" : False, "passwordmatch" : False,
                }
        if User.objects.filter(username=dictionary.get("username")).exists():i
            pass


        User.objects.create_user(username=dictionary.get("username"),
                                email=dictionary.get("email"),
                                password=dictionary.get("password"))
        user = authenticate(username=dictionary.get("username"),
                            password=dictionary.get("password"))
        login(request,user)
        if (dictionary.get("usertype") == "Benefactor"):
            Benefactor.objects.get_or_create(user = user)
        elif (dictionary.get("usertype") == "Volunteer"):
            Volunteer.objects.get_or_create(user = user)
        elif(dictionary.get("usertype") == "Organizer"):
            Organizer.objects.get_or_create(user = user)

    else:
        return render(request,'hex/signin.html',)

def login_view(request):
    return render(request, 'hex/login.html', )



def index(request):
    return render(request, 'hex/index.html', )


def getEventList(request):
    Events.objects.get()
