# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, render_to_response
from django.template import Context, loader, RequestContext
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect
from django.core.context_processors import csrf
from django.contrib import auth
from MOOC.models import Notes

def home(request):
        template = loader.get_template('MOOC/home.html')
        context = Context({})
        return HttpResponse(template.render(context))

def login(request):
        template = loader.get_template('MOOC/login.html')
        context = RequestContext(request, {})
        return HttpResponse(template.render(context))

def loggedin(request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
                auth.login(request, user)
                return render(request, "MOOC/chooseVid.html", RequestContext(request))
                #return render(request, "MOOC14/index.html", RequestContext(request))
        else:
                return HttpResponse("Username password did not match.")


def register(request):
        template = loader.get_template('MOOC/register.html')
        context = RequestContext(request, {})
        return HttpResponse(template.render(context))


def registered(request):
        username = request.POST.get('username')
        password = request.POST.get('cpassword')
        email = request.POST.get('email')
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')

        user = User.objects.create_user(username, email, password)
        user.last_name=lastname
        user.first_name=firstname
        user.save()
        return render(request, "MOOC/registered.html", RequestContext(request)) 

def loadVideo(request):
        if not request.GET.get('Video'):
                ID=request.GET.get('video')
                start=request.GET.get('start')
                end=request.GET.get('end')
                cont=request.GET.get('note')
                n=Notes(username=request.user, videoid=ID, startTime=start, endTime=end, content=cont)
                n.save()
                l=Notes.objects.filter(videoid=ID).filter(username=request.user)
                #return HttpResponse("note is saved")
		return render(request, "MOOC/loadVid.html", RequestContext(request, {'videoid' : ID, 'mynotes' : l}))
        else:
                ID=request.GET.get('Video')
                l=Notes.objects.filter(videoid=ID).filter(username=request.user)
                return render(request, "MOOC/loadVid.html", RequestContext(request, {'videoid' : request.GET.get('Video'), 'mynotes': l}))

def logout(request):
	auth.logout(request)
	return render(request, "MOOC/home.html", RequestContext(request))
