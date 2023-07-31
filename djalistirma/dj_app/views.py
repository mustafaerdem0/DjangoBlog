from django.shortcuts import render,redirect
from django.contrib.auth.models import User,Group
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
# Create your views here.


# Kendi Oluşturdugun Modeli İmport Et
from .models import *


# form import et

from .form import *

def index(request):
    context = {}
    context['Notes'] = Notes.objects.filter(approved = True)
    context['logo'] = logo.objects.first()
    return render(request,'index.html', context)

def notdetaylari(request,notId):
    context = {}
    note =  Notes.objects.filter(id = notId).first()
    if request.method == 'POST':
        form  = notupdate(request.POST, request.FILES,instance=note)
        note.noteauthor = request.user
        form.save()
        return redirect('notedetails',note.id)
    else:
        if note:
            context['note'] = note
            context['form'] = notupdate(instance=note)
            context['user'] = User.objects.filter(id = note.noteauthor.id).first()
        else:
            return redirect('404')
        return render(request,'notdetay.html',context)

def kayitol(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_check = request.POST.get('password_check')
        if username and email and password and password_check:
            User.objects.create_user(username=username,email=email,password=password)
            return redirect('/giris')
    
    else:
        return render(request,'kayitol.html')


def girisyap(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            user = authenticate(request, username= username,password = password)
            if user:
                login(request, user)
                print('GİRİŞ BAŞARILI')
                return redirect('/')
            else:
                messages.add_message(request,messages.SUCCESS,"Böyle Bir Kullanıcı Bulamadık")
                return redirect('girisyap')
        else:
            return redirect('404')
    else:
        return render(request,'girisyap.html')

def notekle(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            notbaslik = request.POST.get('notbaslik')
            noticerik = request.POST.get('noticerik')
            notresim = request.FILES.get('notresim')
            noturl = request.POST.get('noturl')
            status = False
            if notbaslik and noticerik:
                if request.user.is_superuser:
                    status= True
                Notes.objects.create(
                    noteauthor=request.user,
                    note_title=notbaslik,
                    note_content=noticerik,
                    note_image=notresim,
                    note_url=noturl,
                    approved = status
                )
                messages.add_message(request,messages.WARNING,'Postunuz admin tarafından onaylandıktan sonra yayınlanacaktır')
                return redirect('/')
            else:
                return redirect('/')
        else:
            return render(request, 'index.html')
    else:
        return redirect('404')
def cikisyap(request):
    logout(request)
    return redirect('/') 

# notu sil
def notsil(request,notId):
        note = Notes.objects.filter(id=notId).first()
        if note:
            if request.user.is_superuser:
                note.delete()
                messages.add_message(request,messages.WARNING,"admin oldugunuz için Notunuz Başarılı bir şekilde silindi ")
                return redirect('/')

            if request.user == note.noteauthor:
                note.notsil = True
                note.save()
                messages.add_message(request,messages.WARNING,"Notunuz admin onay verdikten sonra silincektir ")
                return redirect('/')
                
            else:
                return redirect('404')
        else:
            return redirect('404')

def hata(request):
    return render(request,"404.html")

def k_kontrol(request):
    if request.user.is_authenticated:
        if request.user.groups.filter(name='Premium').exists():
            print('Kullanıcı premium üyedir.')
            return redirect('404')
        else:
            print('Kullanıcı preimum değil.')
            return redirect('404')
    else:
        return redirect('404')


def blog(request):
    context = {}
    context['bloglar'] = Notes.objects.all()
    return render(request,'blog.html',context)



# notgüncelle


def notEdit(request,notId):
    context = {}
    note = Notes.objects.filter(id = notId).first()
    if request.method == 'POST':
        editform = notupdate(request.POST,request.FILES,instance=note)
        if editform:
            editform.is_valid()
            editform = editform.save(commit=False)
            note.noteauthor = request.user
            editform.save()
            return redirect('notedit',note.id)
        else:
            return redirect('404')
    else:
        context['note'] = note
        context['form'] = notupdate(instance=note)
        return render(request,'notedit.html',context)
    

def userprofile(request, usernames, userid):
    user = User.objects.filter(id=userid ).first()
    username = User.objects.filter(username=usernames).first()
    banlıuser = banned.objects.filter(banneduser = user).exists()
    if banlıuser:
        redirect('userprofile',user.username,user.id)
    context = {}
    context["user"] = user
    context["username"] = username
    context["banlıuser"] = banlıuser
    print(user)
    return render(request, 'userprofile.html', context)

def profileedit(request,userid):
    context = {}
    if request.method == 'POST':
        formedit = formprofile(request.POST,instance=request.user)
        if formedit:
            formedit.is_valid()
            formedit.save()
            return redirect('profileedit', userid)
    else:
        user = User.objects.filter(id = userid).first()
        context['user'] = user
        context['formuser'] = formprofile(instance=request.user)
        if request.user.id == user.id:
            return render(request,'profiledit.html',context)
        else:
            return redirect('404')
        
def notonaybekleme(request):
    context={}
    note = Notes.objects.filter(approved = False)
    formonay = notupdate()
    context['note'] = note
    context['formonay'] = formonay
    return render(request,'notonay.html',context)

def notonay(request,noteId):
    if request.user.is_superuser:
        note = Notes.objects.filter(id = noteId).first()
        if note: 
            note.approved = True
            note.save()
            return redirect('/')
        else:
            return redirect('404')
    else:
        return redirect('404')
    
    

def banneduser(request,userid):
    user = User.objects.filter(id = userid).first()
    if user:
        if request.user.is_superuser:
            banned.objects.create(banneduser = user,authorized = request.user)
            return redirect('/')
        
def notsilbekleyen(request):
    context = {}
    note = Notes.objects.filter(notsil = True)
    context['note'] = note
    return render(request,'notsilonay.html',context)

def notsilonay(request,notId):
    if request.user.is_superuser:
        noteid = Notes.objects.filter(id = notId).first()
        noteid.delete()
        print('başarılı şekilde notunuz silind')
        return redirect('notsilbekleyen')
    else:
        return redirect('404')