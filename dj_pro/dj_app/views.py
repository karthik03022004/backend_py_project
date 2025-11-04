from django.shortcuts import render
from .models import Movies
from .Serealizer import Movie_ser
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.
def valid_file(pic):
    max=5*1024*1024
    if(pic.size>max):
        return False ,"size is too large"
    allow_type=['image/png','image/jpeg']
    if(pic.content_type not in allow_type):
        return False,"invalid type! type should in png,jpeg"
    return True,'valid response'
@csrf_exempt
def create_user(req):
    mname=req.POST.get('name')
    mstatus=req.POST.get('status')
    m_budget=req.POST.get('budget')
    m_pic=req.FILES['pic']
    isfile,msg=valid_file(m_pic)
    if(isfile):
        pass
    else:
        HttpResponse(msg)
    Movies.objects.create(name=mname,status=mstatus,budget=m_budget,pic=m_pic)
    Movies.save()
    return JsonResponse({"data":"successful"})

def read_user(req):
    data=Movies.objects.all()
    movie=Movie_ser(data,many=True)
    return JsonResponse({"data":movie.data})


@csrf_exempt
def update_user(req,mid):
    try:
        single_data=Movies.objects.get(id=mid)
        data_mov=json.loads(req.body)
        movie_data=Movie_ser(single_data,data=data_mov,partial=True)
        if(movie_data.is_valid()):
            movie_data.save()
            return HttpResponse("updated")
    except:
        return HttpResponse("not updated")
    
@csrf_exempt
def delete_user(req,mid):
    try:
        data=Movies.objects.get(id=mid)
        data.delete()
        return HttpResponse("deleted")
    except:
        return HttpResponse("cant deleted")
    