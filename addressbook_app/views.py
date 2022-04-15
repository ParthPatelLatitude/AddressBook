from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.hashers import make_password,check_password
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

def SignUpView(request):
    try:
        if request.method == 'POST':
            data = UserSignup()
            data.email_id = request.POST["email_id"]
            data.password = make_password(request.POST['password'])
            data.save()
            detail = SqlLogin()
            detail.action = 'Signup'
            detail.save()
            return redirect('login')
    except: 
        return redirect('signup')

    return render(request, "signup.html")


def LoginView(request):
    context={}
    if request.method == 'POST':
        email_id = request.POST['email_id']
        password = request.POST['password']
        try:
            record = UserSignup.objects.get(email_id = email_id)
        except: 
            record = None
        if record:
            if check_password(password, record.password):
                request.session['email_id']=record.email_id
                detail = SqlLogin()
                detail.action = 'Login'
                detail.save()
                return redirect('data')
        
        else:
            context = {
                'message':'Incorrect Email ID or Password.'
            }

    return render(request, 'login.html', context)


def LogoutView(request):
    if request.session.has_key('email_id'):
        del request.session['email_id']
        detail = SqlLogin()
        detail.action = 'Logout'
        detail.save()
        return redirect('login')
    else:
        return redirect('login')

def DataView(request):
    if not request.session.has_key('email_id'):
        return redirect('login')
    email_id = request.session['email_id']
    if request.method=='POST':
    
        try:
            data = UserProfile.objects.get(**{'id':request.POST.get("idname")})
        except Exception as ex:
            data = None
        if data is not None:
            profile1 = {
            'first_name':request.POST.get('first_name',data.first_name), 
            'last_name':request.POST.get('last_name',data.last_name),
            'phone_number':request.POST.get('phone_number',data.phone_number),
            'address':request.POST.get('address',data.address),
            
            }
            for key,value in profile1.items(): 
                setattr(data,key,value)
            data.save()
            detail = SqlLogin()
            detail.action = 'Edit'
            detail.save()
            return redirect('data')

        else:
            model = UserProfile()
            model.first_name = request.POST['first_name']
            model.last_name = request.POST['last_name']
            model.address = request.POST['address']
            model.phone_number = request.POST['phone_number']
            model.save() 
            detail = SqlLogin()
            detail.action = 'Create'
            detail.save()
            return redirect('data')
    else:
        data = UserProfile.objects.filter(**{'status':1})
        context = {
            'data' : data
        }
        detail = SqlLogin()
        detail.action = 'View'
        detail.save()
    return render(request,'data.html', context)


def DeleteView(request,id):
    if not request.session.has_key('email_id'):
        return redirect('login')
    
    try:
        data = UserProfile.objects.get(**{'id':id})
    except Exception as ex:
        data = None
    try:
        if data is not None:
            record_map = {} 
            record_map['status_id'] = 2
            
        for key,value in record_map.items():
            setattr(data,key,value)
        data.save() 
        detail = SqlLogin()
        detail.action = 'Delete'
        detail.save()
        return redirect('data')
    except Exception as ex:
        return redirect('data')
    

@csrf_exempt
def EditView(request):
    try:
        if request.method == 'POST':
            id = request.POST.get('id')
            data = UserProfile.objects.get(**{'id':id})
            profile_data = {'first_name':data.first_name, 'last_name':data.last_name, 'phone_number':data.phone_number, 'address':data.address, "idd":data.id}
            return JsonResponse(profile_data)
    except Exception as ex:
        return redirect('data')
        
