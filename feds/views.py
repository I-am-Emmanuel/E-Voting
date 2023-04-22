from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from datetime import datetime
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
from . serializers import CitizenSerializer
from . models import Citizen



# Create your views here.
# def greetings(request):
#     return render(request, 'feds/index.html', {'Good': 'Morning', 'time': datetime.today() })





class CitizensList(APIView):
    def get(self, request):
        citizens = Citizens.objects.all()
        serializer = CitizenSerializer(citizens, many=True, context = {'request': request})
        return Response(serializer.data)
    
    def post(self, request):
        serializer = CitizenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class CitizensDetails(APIView):
    def get(self, request, id):
        citizen = get_object_or_404(Citizens, pk=id)
        serializer = CitizenSerializer(citizen)
        return Response(serializer.data)
    
    def put(self, request, id):
        citizen = get_object_or_404(Citizens, pk=id)
        serializer = CitizenSerializer(citizen, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)




# @api_view(['GET', 'POST'])
# def citizen_list(request):
#     if request.method == 'GET':
#         citizens = Citizens.objects.all()
#         serializer = CitizenSerializer(citizens, many=True, context={'request': request})
#         return Response(serializer.data)
    
#     elif request.method == 'POST':
#         serializer = CitizenSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
    
# @api_view(['GET', 'PUT'])
# def citizen_details(request, id):
#     citizen = get_object_or_404(Citizens, pk=id)
#     if request.method == 'GET':
#         serializer = CitizenSerializer(citizen)
#         return Response(serializer.data)
    
#     elif request.method == 'PUT':
#         serializer = CitizenSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)


