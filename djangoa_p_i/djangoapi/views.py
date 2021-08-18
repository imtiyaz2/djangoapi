from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .serializers import *

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import EmployeeSerializers
from rest_framework.response import Response

@api_view(['POST'])
def create_employee(request):
    if request.method == 'POST':
        myform = EmployeeSerializers(data=request.data)
        if myform.is_valid():
            myform.save()
            return Response(myform.data, status=status.HTTP_201_CREATED)
        print(myform.data)
        return Response({"error":"badrequest"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_allrecord(request):
    if request.method=='GET':
        moni=Employee.objects.all()
        record=EmployeeSerializers(moni,many=True)
        return Response(record.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def filter_record(request):
    # s_record= request.GET.get('search_record', None)
    if request.method=='GET':
        moni=Employee.objects.filter(name='hari')
        record=EmployeeSerializers(moni,many=True)
        return Response(record.data, status=status.HTTP_200_OK)

@api_view(['DELETE'])
def delete_record(request):
    # s_record= request.GET.get('search_record', None)
    record = Employee.objects.filter(job='executive')
    if record:
        record.delete()
        record.is_deleted = True
        record.save()
        return Response({"ok": "Record Deleted"}, status= status.HTTP_200_OK)
    return Response({"failed":"record not found"},status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def update_record(request):
    record=Employee.objects.get(name='kumar')
    if request.method == 'PUT':
        my_form = EmployeeSerializers(data=request.data, instance=record)
        if my_form.is_valid():
            my_form.save()
            print('success')
            return Response({"success:record has been updated successfully"},status=status.HTTP_200_OK)
        return Response({"failed":"record has not updated"},status=status.HTTP_400_BAD_REQUEST)


