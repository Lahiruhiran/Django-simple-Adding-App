from django.shortcuts import render
from .models import Destination
# Create your views here.
def index(request):
    dest1 = Destination()
    dest1.name ="Sri Lanka"
    dest1.des ="It's beautiful place in the world fro visit"
    dest1.price =1000
    dest1.img ="destination_1.jpg"

    dest2 = Destination()
    dest2.name ="Paris"
    dest2.des ="It's beautiful place in the world fro visit"
    dest2.price =800
    dest2.img ="destination_2.jpg"

    dest3 = Destination()
    dest3.name ="Bali"
    dest3.des ="It's beautiful place in the world fro visit"
    dest3.price =450
    dest3.img ="destination_2.jpg"

    dest =[dest1,dest2,dest3]
    return render(request,'index.html',{'dest':dest})