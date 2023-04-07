from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.db.models import Q, Value, F
from django.db.models.aggregates import Count

from rest_framework import permissions
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, DestroyModelMixin, UpdateModelMixin

from core_2.models import Verification, Election
from core.models import UserModel

from feds.models import Citizens

from .serializers import VerificationSerializer,ElectionSerializer, ElectionResultSerializer

from datetime import date, datetime
# Create your views here.



 


class VerificationViewSet(CreateModelMixin, GenericViewSet):
    queryset = Verification.objects.all()

    serializer_class = VerificationSerializer
    
    
    def create(self, request):    
        
        data = request.data
        try:
            birth_date = data.get('birth_date')

            today = date.today()
            birth_date = datetime.strptime(birth_date, "%Y-%m-%d").date()
            age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        except ValueError:
            return Response({'Error': 'Date box cannot be empty!'}, status=status.HTTP_400_BAD_REQUEST)

        
        if Citizens.objects.filter(Q(nin=data.get('nin')) & Q(birth_date=birth_date)) and age >= 18:
            serializer = VerificationSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({'Success': 'You have successfully done your accreditation. You are now eligible to vote'}, status=status.HTTP_201_CREATED)
        elif Citizens.objects.filter(Q(nin=data.get('nin')) & Q(birth_date=birth_date)) and age < 18:
            return Response({'Fail': 'We have your data in place but your age is not eligible to vote!!'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({'Fail': "Your registration cannot be found in the database. Make sure you have registered and your data is input correctly!!"}, status=status.HTTP_401_UNAUTHORIZED)
    
        

    

class ElectionViewSet(CreateModelMixin, GenericViewSet):
    
    queryset = Election.objects.all()

    def get_serializer_class(self):
        return ElectionSerializer
    

    def create(self, request):
    
        if Verification.objects.filter(nin='nin'):
            serializer = ElectionSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({'Success': 'You have successfully casted your vote for your candidate of choice'}, status=status.HTTP_201_CREATED)
        return Response({'error': "You are not eligible to vote!!! Reason: You have not yet done your accreditation!!"}, status=status.HTTP_401_UNAUTHORIZED)
    
    
class ElectionResultViewSet(ModelViewSet):      
    # pass

    # queryset = Election.objects.all

    def get_queryset(self):
        return Election.objects.annotate(bola_ahmed=Count('candidate')).filter(candidate='icontains__Atiku')                                  

    def get_serializer_class(self):
        return ElectionResultSerializer

    # queryset = Verification.objects.aggregate(count=Count('nin'))
    # serializers = ElectionSerializer
    
    # def get_serializer_context(self):
    #     return {'request': self.request}

    



    
    # def post(self, request, *args, **kwargs):
    #     # if Citizens.objects.filter(nin__in=self.kwargs['nin']) and Citizens.objects.filter(birth_date__in=self.kwargs['birth_date']):
            # if request.method == 'POST':
            #     # serializer = VerificationSerializer(data=request.data)
            #     # serializer.is_valid(raise_exception=True)
            #     return Citizens.objects.filter(nin__in=self.kwargs['']) and Citizens.objects.filter(birth_date__in=self.kwargs['birth_date'])
    
    # def post(self, request, **kwargs):
    #     # query_nin, query_birth_date = Citizens.objects.filter('nin', 'birth_date')
        # if request.method == 'POST':
        #     serializer = VerificationSerializer(data=request.data)
        #     serializer.is_valid(raise_exception=True)
    #         if  Citizens.objects.filter(nin__in=serializer) and Citizens.objects.filter(birth_date__in=serializer):
    #             serializer.save()
    #             return render(request, serializer.data)
            # return Response(serializer.errors, status=)

                
#  query_set = Product.objects.only('id', 'title')
            # else
            # serializer = VerificationSerializer(data=request.data)
            # serializer.is_valid(raise_exception=True)
            # # query_set = Citizens.objects.filter('nin', 'birth_date')
            # if serializer in query_set:
            #     serializer.save()
            #     return Response(serializer.data)
            


    

    # def post(self, request):
    #     if request.method == 'POST':
    #         serializer = VerificationSerializer(data=request.data)
    #         serializer.is_valid(raise_exception=True)
    #         query_set, query = Citizens.objects.filter('nin', 'birth_date')
    #         if serializer in query_set:
    #             serializer.save()
    #             return Response(serializer.data)
            # return Response(serializer.errors)
            
            


