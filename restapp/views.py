from django.shortcuts import render
from rest_framework.decorators import api_view,APIView
from rest_framework.response import Response
from .serializers import BookSerializer,UserSerializer,StudentSerializer,TaskSerializer
from .models import User,BookModel,StudentModel,Taskmodel
from rest_framework import status
import jwt
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.
@api_view(['GET'])
def list_books(request):
    book=BookModel.objects.all()
    book_obj=BookSerializer(book,many=True)
    return Response(book_obj.data,status=status.HTTP_200_OK)

@api_view(['GET'])
def get_book(request,id):
    try:
        book = BookModel.objects.get(id=id)
        book_obj = BookSerializer(book,many=False)
        return Response(book_obj.data,status=status.HTTP_200_OK)
    except BookModel.DoesNotExist:
        return Response({'error:Book not found'},status=status.HTTP_404_NOT_FOUND)

@api_view(['POST','GET'])
def add_book(request):
    book=BookModel.objects.all()
    if request.method=="GET":
       obj=BookSerializer(book,many=True)
       return Response(obj.data,status=status.HTTP_200_OK)
    elif request.method=="POST":
       obj=BookSerializer(data=request.data) 
       if obj.is_valid():
           obj.save()
           return Response(obj.data,status=status.HTTP_201_CREATED)
       return Response(obj.errors,status=status.HTTP_400_BAD_REQUEST)


    

    
@api_view(['GET','PUT'])
def bookedit(request,id):
    book = BookModel.objects.get(id=id)
    if request.method=='GET':
        serializer=BookSerializer(book)
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method=='PUT':
        serializer=BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    



@api_view(['GET','PATCH'])
def bookupdate(request,id):
    book = BookModel.objects.get(id=id)
    if request.method=='GET':
        serializer=BookSerializer(book)
        return Response(book.data,status=status.HTTP_200_OK)
    elif request.method=='PATCH':
        serializer=BookSerializer(book, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)   
    
@api_view(['GET','DELETE'])
def delete_book(request,id):
    book=BookModel.objects.get(id=id)
    if request.method=='GET':
        serializer=BookSerializer(book)
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method=='DELETE':
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)   


@api_view(['POST','GET'])
def add_user(request):
    user=User.objects.all()
    if request.method=="GET":
       obj=UserSerializer(user,many=True)
       return Response(obj.data,status=status.HTTP_200_OK)
    elif request.method=="POST":
       obj=UserSerializer(data=request.data) 
       if obj.is_valid():
           obj.save()
           return Response(obj.data,status=status.HTTP_201_CREATED)
       return Response(obj.errors,status=status.HTTP_400_BAD_REQUEST)
    


@api_view(['GET','PUT'])
def useredit(request,userid):
    user = User.objects.get(id=userid)
    if request.method=='GET':
        serializer=UserSerializer(user)
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method=='PUT':
        serializer=UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    



@api_view(['GET','PATCH'])
def userupdate(request,userid):
    user = User.objects.get(id=userid)
    if request.method=='GET':
        serializer=UserSerializer(user)
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method=='PATCH':
        serializer=UserSerializer(user, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)   
    
@api_view(['GET','DELETE'])
def delete_user(request,userid):
    user=User.objects.get(id=userid)
    if request.method=='GET':
        serializer=UserSerializer(user)
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method=='DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)   

@api_view(['GET'])
def list_users(request):
    user=User.objects.all()
    obj=UserSerializer(user,many=True)
    return Response(obj.data,status=status.HTTP_200_OK)


@api_view(['GET'])
def get_user(request,userid):
    try:
        user = User.objects.get(id=userid)
        user_obj = UserSerializer(user,many=False)
        return Response(user_obj.data,status=status.HTTP_200_OK)
    except User.DoesNotExist:
        return Response({'error:Book not found'},status=status.HTTP_404_NOT_FOUND)
   
  
#   {
  
#  "username":"Jyothika",
#  "password":"jyo13"
  
# }  
# {
  
#  "username":"Charutha",
#  "password":"charu04"
# }
# {
  
# "username":"Devika",
# "password":"dev2002"
  
# }


@api_view(['POST'])
def login_user(request):
    user=authenticate(username=request.data.get('username'),password=request.data.get('password'))
    if user:
        serializer=UserSerializer(user)
        refresh=RefreshToken.for_user(user)
        token_data={
            'refresh':str(refresh),
            'access':str(refresh.access_token)

        }
        return Response({"user":serializer.data,"token":token_data},status=status.HTTP_200_OK)
    return Response({"details":"Invalid credentials"},status=status.HTTP_400_BAD_REQUEST)




@api_view(['GET'])
def logout_user(request):
    response=Response({"status":"logout"},status=status.HTTP_200_OK)
    response.delete_cookie('token')
    return Response


class Studentlist(APIView):
    def get(self,request,format=None):
        student=StudentModel.objects.all()
        student_obj=StudentSerializer(student,many=True)
        return Response(student_obj.data,status=status.HTTP_200_OK)
    

class Studentadd(APIView):
     permission_classes=[IsAuthenticated]
     authentication_classes=[JWTAuthentication]
     def get(self,request,format=None):
        student=StudentModel.objects.all()
        student_obj=StudentSerializer(student,many=True)
        return Response(student_obj.data,status=status.HTTP_200_OK)
     def post(self,request,format=None):
         student_obj=StudentSerializer(data=request.data)
         if student_obj.is_valid():
             student_obj.save()
             return Response(student_obj.data,status=status.HTTP_201_CREATED)
         return Response(student_obj.errors,status=status.HTTP_400_BAD_REQUEST)
        
class Studentupdate(APIView):
     def get(self,request,format=None,studentid=None):
        student=StudentModel.objects.get(id=studentid) 
        student_obj=StudentSerializer(student) 
        return Response(student_obj.data,status=status.HTTP_200_OK)
     def patch(self,request,studentid,format=None):
        student=StudentModel.objects.get(id=studentid)
        student_obj=StudentSerializer(student,data=request.data,partial=True)
        if student_obj.is_valid():
            student_obj.save()
            return Response(student_obj.data,status=status.HTTP_202_ACCEPTED)
        return Response(student_obj.errors,status=status.HTTP_400_BAD_REQUEST)


class Taskadd(APIView):
    def get(self,request,format=None):
        task=Taskmodel.objects.all()
        task_obj=TaskSerializer(task,many=True)
        return Response(task_obj.data,status=status.HTTP_200_OK)
    def post(self,request,format=None):
        task_obj=TaskSerializer(data=request.data)
        print(request.user)
        if task_obj.is_valid():
            task_obj.save(user=request.user)
            return Response(task_obj.data,status=status.HTTP_201_CREATED)
        return Response(task_obj.errors,status=status.HTTP_400_BAD_REQUEST)



class Tasklist(APIView):
    def get(self,request,format=None):
        task=Taskmodel.objects.all()
        task_obj=TaskSerializer(task,many=True)
        return Response(task_obj.data,status=status.HTTP_200_OK)
 
@api_view(['GET'])
def gettask(request,task_id):
    product=Taskmodel.objects.get(id=task_id)
    if request.method=='GET':
        serializer=TaskSerializer(product)
        return Response(serializer.data,status=status.HTTP_200_OK)   
        
class Statusupdate(APIView):
     permission_classes=[IsAuthenticated]
     authentication_classes=[JWTAuthentication]
     def get(self,request,format=None,taskid=None):
        task=Taskmodel.objects.get(id=taskid) 
        task_obj=TaskSerializer(task) 
        return Response(task_obj.data,status=status.HTTP_200_OK)
     def patch(self,request,taskid,format=None):
        task=Taskmodel.objects.get(id=taskid)
        task_obj=TaskSerializer(task,data=request.data,partial=True)
        if task_obj.is_valid():
            task_obj.save()
            return Response(task_obj.data,status=status.HTTP_202_ACCEPTED)
        return Response(task_obj.errors,status=status.HTTP_400_BAD_REQUEST)  

class gettaskbylogin(APIView):
    permission_classes=[IsAuthenticated] 
    authentication_classes=[JWTAuthentication] 
    def get(self,request,format=None) :
        task=Taskmodel.objects.get(user=request.user) 
        task_obj=TaskSerializer(task) 
        return Response(task_obj.data,status=status.HTTP_200_OK) 
    
class gettasklistbylogin(APIView):
    permission_classes=[IsAuthenticated]
    authentication_classes=[JWTAuthentication]
    def get(self,request,format=None):
        task=Taskmodel.objects.filter(user=request.user)
        task_obj=TaskSerializer(task,many=True)
        return Response(task_obj.data,status=status.HTTP_200_OK)
