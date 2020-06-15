from django.shortcuts import render, redirect,HttpResponse
from django.contrib.auth.forms import UserCreationForm 
from .forms import LocationForm, ProfileCreationForm, PlusPhotoForm, addrForm
from .models import UserLocation, RegiProfile, PlusPhoto, Address
from django.contrib.auth import login as pet_login
from django.contrib.auth.models import User

from haversine import haversine
import json

# Create your views here.

def check_loc(tem_user):
    my_loc = Address.objects.get(user=tem_user.user)
    all_loc = Address.objects.exclude(user= tem_user.user)
    
    my_loc_tu = (my_loc.lat, my_loc.lon)
    
    close_ping = list()
    
    for i in range(len(all_loc)):
        print("#################",print(float(all_loc[i].lat)))
        temp_tu = (float(all_loc[i].lat), float(all_loc[i].lon))
        diff_kilo = haversine(my_loc_tu,temp_tu)
        if diff_kilo < 1:
            close_ping.append(temp_tu)
            print("저장한 거리 : " , diff_kilo)
        else:
            print("아니라서 저장안한 거리 : " , diff_kilo)

    print(tem_user.POST, "T"*100)

    return close_ping

def startpage(request):
    return render(request, 'registration/startpage.html')


def home(request):
    return render(request, 'registration/home.html')

def register(request):
    register_form = UserCreationForm()      #유저생성폼을 만든다
    location_form = LocationForm()
    #  com_location_form = LocationForm(request.POST['ispermit'])  # check box 완성된 상태
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
    if request.method == "POST":

        # petname= ProfileCreationForm(request.POST['pet_name'])
        # pettype= ProfileCreationForm(request.POST['pet_type'])
        # petage= ProfileCreationForm(request.POST['pet_age'])
        # petgender= ProfileCreationForm(request.POST['pet_gender'])
        # # petlocate= ProfileCreationForm(request.POST['pet_locate'])
        # petimage= ProfileCreationForm(request.POST['pet_image'])
        # petintro= ProfileCreationForm(request.POST['pet_intro'])

        saveform = ProfileCreationForm(request.POST,request.FILES,instance=my_pet)
        if saveform.is_valid:
            saveform.save()
            return redirect('myprofile')        #myprofile로 가게 해주세요

    return render(request, 'registration/regi_profile.html', {'regi_profile_form':regi_profile_form, 'my_pet':my_pet})
# 'regi_profile_form':regi_profile_form,
#
# def register(request):
#     if request.method == "POST":
#         if request.POST['password1'] == request.POST['password2']:
#             user = User.objects.create_user(
#                 username=request.POST['username'], password=request.POST['password1'])
#             auth.login(request, user)
#             return redirect('regi_profile')
#     location_form = LocationForm()

#     return render(request, 'registration/register.html', {'location_form': location_form})

#


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
    context['loc'] = check_loc(request)

    return render(request, 'registration/myprofile.html', context)

def photoplus(request):
    photo_plus = RegiProfile.objects.get(user=request.user)
    # photo_plus = RegiProfile.objects.get(pk= pet_id)
    if request.method == "POST":
        plusphoto_form = PlusPhotoForm(request.POST, request.FILES)
        # plusphoto_form.save()
        # plus = PlusPhotoForm(request.POST['plus_image'])
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

    return render(request, 'registration/profileinform.html',{'myprofile':myprofile,'all_pet':all_pet} )

def maptest(request):
    map_form = PersonForm
    return render(request, 'registration/maptest.html', {'map_form':map_form})

def map_home(request):
    return render(request, 'registration/map_home.html')

def map_home_menu(request):
    all_user = Address.objects.all()[0]
    return render(request, 'map_home.html',{'all_user':all_user})



def lat_lon(request):
    if request.method == 'POST':
        lat, lon = request.POST["lat"], request.POST["lon"]

        if Address.objects.filter(user=request.user).exists():
            update_addr= Address.objects.get(user=request.user)
            update_addr.lat = lat 
            update_addr.lon = lon
            update_addr.save()
            status = "업데이트"
        else:
            Address.objects.create(user= request.user, lat=lat, lon=lon)
            status = "생성"

    context = {'status':status}
        
    return HttpResponse(json.dumps(context), content_type='application/json')

def matching(request):
    return render(request, 'registration/matching.html')

def first(request):
    return render(request, 'registration/first.html')

def second(request):
    return render(request, 'registration/second.html')

def third(request):
    return render(request, 'registration/third.html')



def search(request):
    return render(request,'search.html',)
