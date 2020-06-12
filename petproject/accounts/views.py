from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm 
from .forms import LocationForm, ProfileCreationForm, PlusPhotoForm, PersonForm
from .models import UserLocation, RegiProfile, PlusPhoto
from django.contrib.auth import login as pet_login
from django.contrib.auth.models import User
# Create your views here.


def startpage(request):
    return render(request, 'registration/startpage.html')

def register(request):
    register_form = UserCreationForm()      #유저생성폼을 만든다
    location_form = LocationForm()

    if request.method == "POST":
        register_form = UserCreationForm(request.POST)
        # request.POST안에 담긴 정보들을 UserCreateForm에 담고,
        com_location_form = LocationForm(request.POST['ispermit'])
        if register_form.is_valid():
            register_form.save()
            user = User.objects.get(username = register_form.cleaned_data['username'])
            pet_login(request, user)
            return redirect('regi_profile')
        else:
            pass
    context = {'register_form':register_form,'location_form':location_form}
    return render(request, 'registration/register.html', context)

def regi_profile(request):
    my_pet = RegiProfile.objects.get(user=request.user)
    regi_profile_form = ProfileCreationForm(instance=my_pet)
    print("*"*100, regi_profile_form)
    if request.method == "POST":
        saveform = ProfileCreationForm(request.POST,request.FILES,instance=my_pet)
        print("#"*100,saveform)
        if saveform.is_valid:
            print("@"*100,saveform)
            # print("*"*100,saveform.user)
            saveform.save()
            return redirect('myprofile')        #myprofile로 가게 해주세요
    
    return render(request, 'registration/regi_profile.html', {'regi_profile_form':regi_profile_form, 'my_pet':my_pet})

def login(request):
    return render(request, 'registration/login.html')

def myprofile(request):
    context = {}
    all_pet = RegiProfile.objects.all()
    myprofile = RegiProfile.objects.get(user=request.user)
    photo = PlusPhoto.objects.filter(user=request.user)
    context['myprofile'] = myprofile
    context['all_pet'] = all_pet
    context['photo'] = photo
    return render(request, 'registration/myprofile.html', context)

def photoplus(request):
    photo_plus = RegiProfile.objects.get(user=request.user)
    # photo_plus = RegiProfile.objects.get(pk= pet_id)
    if request.method == "POST":
        plusphoto_form = PlusPhotoForm(request.POST, request.FILES)
        # plusphoto_form.save()
        
        if plusphoto_form.is_valid():   
            temp = plusphoto_form.save(commit=False)
            temp.user = request.user
            temp.save()
            return redirect('myprofile') 
        # else:
        #     return redirect('photoplus')
        
    plusphoto_form = PlusPhotoForm()

    return render(request, 'registration/photoplus.html', {'plusphoto_form':plusphoto_form})


def profileinform(request):
    all_pet = RegiProfile.objects.all()
    myprofile = RegiProfile.objects.get(user=request.user)

    return render(request, 'registration/profileinform.html',{'myprofile':myprofile}, {'all_pet':all_pet})

def maptest(request):
    map_form = PersonForm
    return render(request, 'registration/maptest.html', {'map_form':map_form})