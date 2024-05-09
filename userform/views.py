from django.shortcuts import render
from .models import UserInfo
from django.middleware.csrf import get_token
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.http import require_POST
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET','POST'])
def UserCreate(request):
    if request.method=='POST':
        data=request.data
        name=data.get('Name')
        email=data.get('Mail_ID')
        resume=request.FILES.get('file')
        print(name,email,resume)
        user=UserInfo(name=name,email=email,resume=resume)
        user.save()
        return Response({"action":"success"},status=201)
        
        
    return Response("Not saved..")
    

@ensure_csrf_cookie
def get_csrf_token(request):
    csrf_token=get_token(request)
    return JsonResponse({'csrf_token':csrf_token})

