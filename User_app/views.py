from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required


# Create your views here.

@login_required
def my_logout(request):
    logout(request)
    return redirect('my_login')

def my_login(request):
    context={}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user:
            #create session
            login(request, user)
            
            next_url = request.POST.get('next_url')
            if next_url:
                return redirect(next_url)
            else:
                return redirect('index')
        else:
            context['username'] = username
            context['password'] = password
            context['error'] = 'Missing Username OR Password'

    next_url = request.GET.get('next')
    if next_url:
        context['next_url'] = next_url
            
     
    return render(request, 'User_app/login.html',context = context)

# def createAccount(request):
#     context={}
#     if request.method == 'POST':
#         completed = request.POST.get('agree-term')
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         re_password = request.POST.get('password_again')
#         fname = request.POST.get('fname')
#         lname = request.POST.get('lname')
#         email = request.POST.get('email')

#         if completed:
#             if re_password != password:
#                 context['error'] = 'Password do not match'
#             else:
#                 try:
#                     user = User.objects.create_user(username, email, password)
#                     print('reach')
#                     Groups = Group.objects.get(name='register_user')
#                     user.first_name = fname
#                     user.last_name = lname
#                     user.groups.add(Groups)
#                     user.save()
#                     success = 'Your Account '+username+' : Success Sign up' 
#                     request.session['success'] = success
#                     return redirect('my_login')
#                 except Exception as e:
#                     context['error'] = '%s' % (e.args)
                
#         else:
#             context['error'] = 'Please agree Terms of service'

#         context['username'] = username
#         context['fname']= fname
#         context['lname'] = lname
#         context['email'] = email
#         context['signup'] = 'True'
 
#     return render(request,'login/create_account.html',context=context)
    
# @login_required
# def ChangePassword(request):
#     context={}
#     if request.method == 'POST':
#         user = request.user.username
#         password = request.POST.get('password')
#         re_password = request.POST.get('password_again')

#         if password != re_password:
#             context['error'] = 'Password do not match'
#         else:
#             u = User.objects.get(username=user)
#             u.set_password(password)
#             u.save()
#             context['success'] = 'Change Password Successfully'
#             return redirect('my_logout')

#     return render(request, 'login/changepassword.html', context=context)

@login_required
def homepage(request):
    contexts = {}
    return render(request, 'User_app/index.html', context=contexts)

@login_required
@permission_required('admin.add_logentry')
def home_admin(request):
    contexts = {}
    return render(request, 'User_app/home_admin.html', context=contexts)

@login_required
@permission_required('admin.add_user')
def add_user(request):
    return render(request, 'User_app/index.html', context=contexts)

@login_required
@permission_required('admin.view_user')
def view_user(request):
    return redirect('home_admin')
    
@login_required
@permission_required('admin.add_doctor')
def add_doctor(request):
    return redirect('home_admin')

@login_required
@permission_required('admin.add_nurse')
def add_nurse(request):
    return redirect('home_admin')

@login_required
@permission_required('admin.add_public_health')
def add_public_health(request):
    return redirect('home_admin')
