import json
from rest_framework.views import APIView
from django.shortcuts import render

from account.models import Application,slot
from .serializers import (MyTokenObtainPairSerializer,RegisterSerializer,
ApplicationSerializer,slotSerializer)
from rest_framework import generics
from rest_framework import status,serializers
from rest_framework.response import Response
# Create your views here.
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.decorators import api_view
from django.contrib.auth.models import User


class MyTokenObtainPairView(TokenObtainPairView):
    
         serializer_class = MyTokenObtainPairSerializer
    
        


class userBlockView(APIView):
    def put(self,request,id):
        block_user=User.objects.get(id=id)
        if block_user.is_active:
            block_user.is_active=False
        else:
            block_user.is_active=True
        block_user.save()
        id=block_user.id
        return Response({id:block_user.is_active,},status=status.HTTP_200_OK)
        

class UserCreateView(APIView):
    # serializer_class=RegisterSerializer
    def get(self,request):
            pass
    
    
    def post(self,request):
        
        serializer=RegisterSerializer(data=request.data)
        if serializer.is_valid():

                account=serializer.save()
                
                refresh = RefreshToken.for_user(account)

                return Response({
                    'username':account.username,
                    'password':account.password,
                    'refresh': str(refresh),
                'access': str(refresh.access_token),
                },status=status.HTTP_201_CREATED)
                
                #return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)


class ApplicationCreateView(generics.ListCreateAPIView):
    # permission_classes = [IsAuthenticatedOrReadOnly]
    
    serializer_class = ApplicationSerializer

class ApplicationListView(generics.ListAPIView):
    # authentication_classes = [TokenAuthentication]
    queryset = Application.objects.filter(Approved=False,Denied=False)
    serializer_class = ApplicationSerializer
class UserListView(generics.ListAPIView):
    # authentication_classes = [TokenAuthentication]
    queryset = User.objects.all()
    serializer_class =RegisterSerializer

# class UserListView(APIView):
#     def  get(self,request):
#         try:
#             user=User.objects.all()
#             print(user[0].id)
#             serializer=RegisterSerializer(user)
#             return Response(serializer.data,status=status.HTTP_200_OK)
#         except:
#             return Response({"error":"no data"},status=status.HTTP_404_NOT_FOUND)




# class ApplicationDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Application.objects.all()
#     serializer_class = ApplicationSerializer

class ApplicationDetailView(APIView):
    def  get(self,request,pk):
        try:
            application=Application.objects.get(pk=pk)
            serializer=ApplicationSerializer(application)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except:
            return Response({"error":"no data"},status=status.HTTP_404_NOT_FOUND)
    # def post(self,request):
    #     serializer=Application(data=request.data)
    #     if serializer.is_valid():
    #        serializer.save()
    #        return Response(status=status.HTTP_201_CREATED)
    #     else:
    #         return Response(status=status.HTTP_400_BAD_REQUEST)


class approveRequest(APIView):
    def put(self,request,pk):
        application = Application.objects.filter(id=pk)
        application.update(Approved=True)
        return Response (200)

class declineRequest(APIView):
     def put(self,request,pk):
        application = Application.objects.filter(id=pk)
        application.update(Denied=True)
        return Response (200)

class AprovedApplicationView(APIView):
    def get(self,request):
        try:  
            applications=Application.objects.filter(Approved=True,Denied=False)
            serializer=ApplicationSerializer(applications,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except:
            return Response({"error":"no data"},status=status.HTTP_404_NOT_FOUND)


class DeniedApplicationView(APIView):
    def get(self,request):
        try:  
            applications=Application.objects.filter(Approved=False,Denied=True)
            serializer=ApplicationSerializer(applications,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except:
            return Response({"error":"no data"},status=status.HTTP_404_NOT_FOUND)


class seat(APIView):
    def get(self,request):
        seat = slot.objects.all()
        serializeobj=slotSerializer(seat,many=True)
        return Response(serializeobj.data)

class AllotedSeat(APIView):
    def put(self,request,id):
        body = request.body.decode('utf-8')
        body = json.loads(body)
        num=body["id"]
        print("ivide print")
        print(id)
        print(num)
        application= Application.objects.filter(id=num)
        application.update(is_alloted = True ,alloted_slot = id)
        seat =  slot.objects.filter(id=id)
        print(application[0].user.id)
        seat.update( is_available=False , assigned_user=application[0].user)
        return Response(200)

class ClearSeat(APIView):
    def put(self,request,id):
        body = request.body.decode('utf-8')
        body = json.loads(body)
        #  num=body["id"]
        print("helooo")
        print(id)
        application= Application.objects.filter(alloted_slot=id)
        application.update(is_alloted = False ,alloted_slot =None)
        seat =  slot.objects.filter(id=id)
        # print(application[0].user)
        seat.update(is_available=True , assigned_user=None)
        return Response(200)



@api_view(['POST'])
def UserCreate(request):
    if request.method == 'POST':
        serializer=RegisterSerializer(data=request.data)
        if serializer.is_valid():
            # serializer.save()
                account=serializer.save()
                
                refresh = RefreshToken.for_user(account)

                return Response({
                    'username':account.username,
                    'password':account.password,
                    'refresh': str(refresh),
                'access': str(refresh.access_token),
                },status=status.HTTP_201_CREATED)
              
                
            # return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)