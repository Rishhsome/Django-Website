from django.shortcuts import render, HttpResponse
from django.contrib import messages
from datetime import date, datetime
from MyAppTrial.models import Contact

# Create your views here.
def index(request):
    # context={
    #     'variable1' : 'Rishabh done for now',
    #     'variable2' : 'Omkay'
    # }
    #return render(request, 'index.html', context)  # when we want to render the template files
    # return HttpResponse("This is Rishabh's page")
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')
    # return HttpResponse("This is about page")

def services(request):
    return render(request, 'services.html')
    # return HttpResponse("This is services page")

def contact(request):
    if request.method == "POST":
        FirstName = request.POST.get('First-Name')
        LastName = request.POST.get('Last-Name')
        Query = request.POST.get('Query')
        City = request.POST.get('City')
        PhoneNumber = request.POST.get('Phone-Number')
        contact = Contact(FirstName=FirstName, LastName=LastName, Query=Query, City=City, PhoneNumber=PhoneNumber, date=datetime.today())
        contact.save()
        messages.success(request, 'YOUR QUERY HAS REACHED US!')
    return render(request, 'contact.html')
    # return HttpResponse("This is contact page")

        
    
