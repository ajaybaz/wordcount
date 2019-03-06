from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, 'home.html',{'key':'Ajay Kumar'})


def count(request):
    data= request.GET['textname']
    list=data.split()
    lenght= len(data)
    array= {}

    for w in list:
            if w in array:
                array[w]+=1
            else:
                array[w]=1
    sorted1= sorted(array.items(), key= operator.itemgetter(1), reverse = True)
    return render(request, 'count.html',{'key':'Ajay Kumar','key1': data,'lenght': lenght, 'array':sorted1 })


def about(request):
    return render(request, 'about.html',{'key':'Ajay Kumar'})
