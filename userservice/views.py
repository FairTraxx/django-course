from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from rest_framework import status



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def test(request):
    return JsonResponse({'message':"user is sucessfully authenticated and ready to use endpoints that require authentication"},status=status.HTTP_200_OK )






