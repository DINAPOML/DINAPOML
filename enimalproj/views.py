from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Registration, DogList, DogAdoption, DogDonation


# ADOPTORINFO
def MainPage(request):
    adoptor = Registration.objects.all()
    return render(request, 'mainpage.html')


def ViewList (request, adoptorId): #OK
    NewAdoptor = Registration.objects.all(id=adoptorId)
    return render (request, 'dogadoption.html', {'NewAdoptor': NewAdoptor}) #same with donate page iba lang render html

def NewList(request):  #OK
    Name = request.POST['name']
    ContactNumber = request.POST['number']
    Age = request.POST['age']
    Address = request.POST['address']
    EmailAddress = request.POST['emailaddress']
    NewAdoptor = Registration.objects.create(Name=Name,ContactNumber=ContactNumber,Age=Age,Address=Address,EmailAddress=EmailAddress)
    return redirect(f'/enimalproj/{NewAdoptor.id}/')

# DOGLIST
def AddDog(request, adoptorId): #OK
    AddDog = DogList.objects.get(id=adoptorId)
    Gender = request.POST['gender']
    Breed = request.POST['breed']
    Fur = request.POST['fur']
    Category = request.POST['category']
    DogList.objects.create(adoptorId=AddDog, Gender=gender, Breed=breed, Fur=fur, Category=category)
    return redirect (f'/enimalproj/{adoptorId}/')

def delete(request, adoptorId):
    AddDog = DogList.objects.get(id=adoptorId)
    AddDog.delete()
    return redirect(f'/enimalproj/{None}/AddDog2/')

def AddDog2(request):
    return render(request, 'doglist.html')

def edit(request, adoptorId):
    AddDog = DogList.objects.filter(id=adoptorId)
    print (AddDog)
    return render(request,'edit.html', {'AddDog':AddDog})

def update(request, patientId):
    # newPatient = Patient.objects.get(id=patientId)
    AddDog = DogList.objects.get(id=adoptorId)
    Gender = request.POST['gender']
    Breed = request.POST['breed']
    Fur = request.POST['fur']
    Category = request.POST['category']
    DogList.objects.create(adoptorId=AddDog, Gender=gender, Breed=breed, Fur=fur, Category=category)
    return redirect (f'/enimalproj/{adoptorId}/')

#DOG ADOPTION
def ViewList (request):  #OK
    NewAdoptor = Registration.objects.create(Name=Name,ContactNumber=ContactNumber,Age=Age,Address=Address,EmailAddress=EmailAddress)
    return redirect(request,'dogadoption.html', {'AddAdoption':AddAdoption})

def AddAdoption(request, adoptorId): #OK
    adoption = Adoption.objects.get(id=adoptorId)
    DateToday = request.POST['datetoday']
    DateToAdopt = request.POST['adoptdate']
    Remarks = request.POST['DateRem']
    Adoption.objects.create(adoptorId=AddAdoption, DateToday=datetoday, DateToAdopt=adoptdate, Remarks=DateRem)
    return redirect (request,'dogadoption.html', {'AddAdoption':AddAdoption})

#DOG DONATION
def ViewList (request):  #OK
    NewAdoptor = Registration.objects.create(Name=Name,ContactNumber=ContactNumber,Age=Age,Address=Address,EmailAddress=EmailAddress)
    return redirect(request,'dogadoption.html', {'AddAdoption':AddAdoption})

def AddDonation(request, adoptorId): #OK
    donation = Donation.objects.get(id=adoptorId)
    Amount = request.POST['amount']
    DateTransaction = request.POST['trans']
    Message = request.POST['Message']
    Status = request.POST['DonSts']
    Adoption.objects.create(adoptorId=donation, Amount=amount, DateTransaction=trans, Message=Message, Status=DonSts)
    return redirect (request,'dogadoption.html', {'AddAdoption':AddAdoption})


def Home(request):
    return render(request,'home.html')

def Facts(request):
    return render(request,'facts1.html')

def Aboutus(request):
    return render(request,'aboutus.html')