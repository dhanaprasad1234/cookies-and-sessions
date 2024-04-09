from django.shortcuts import render

# Create your views here
def name_view(request):
    return render(request,'name.html')

def father_view(request):
    name=request.GET['name']

    response = render(request,'fathername.html',{'name':name})
    response.set_cookie('name',name)
    return response

def mother_view(request):
    fathername=request.GET['fathername']
    name = request.COOKIES['name']
    response = render(request,'mothername.html',{'name':name})
    response.set_cookie('fathername',fathername)
    return response

def results_view(request):
    name = request.COOKIES['name']
    fathername = request.COOKIES['fathername']
    mothername = request.GET['mothername']
    response = render(request,'detailsresult.html',{'name':name,'fathername':fathername,'mothername':mothername})
    response.set_cookie('mothername',mothername)
    return response


