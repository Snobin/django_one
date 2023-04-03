from django.shortcuts import render
from .models import destination

# Create your views here.
def index(request):
    dest1=destination()
    dest1.id=7
    dest1.desc='just for fun'
    dest1.img='news1.png'
    
    dest2=destination()
    dest2.id=7
    dest2.desc='just for fun'
    dest2.img='news2.png'
    
    dest3=destination()
    dest3.id=7
    dest3.desc='just for fun'
    dest3.img='news3.png'
    
    dests=[dest1,dest2,dest3]
    return render(request,'index.html',{'dests':dests})