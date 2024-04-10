from django.shortcuts import render
import datetime
from .forms import LoginForm
from django.http import HttpResponseBadRequest
# Create your views here.
def home(request):
    form = LoginForm()
    return render(request,'loginform.html',{'form':form})

def date_time_view(request):
    # form=LoginForm(request.GET)

        user_id = request.GET['user_id']
        response = render(request,'datetime.html',{'user_id':user_id})
        response.set_cookie('user_id',user_id)
        return response

'''def date_time_view(request):
    if request.method == 'GET':
        form =LoginForm(request.GET)
        if form.is_valid():
            user_id = form.cleaned_data['user_id']
            print(form.cleaned_data['user_id'])
            form.save()
            response = render(request, 'datetime.html', {'user_id': user_id})
            response.set_cookie('user_id', user_id)
            return response
        else:
            return HttpResponseBadRequest("Invalid form data")
    else:
        return HttpResponseBadRequest("Only GET method is allowed for this view")'''

def result_views(request):
    user_id=request.COOKIES['user_id']
    date_time = datetime.datetime.now()
    my_dict = {'user_id':user_id,'date_time':date_time}
    return render(request,'result.html',my_dict)

