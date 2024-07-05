from rest_framework import serializers
from .models import User,BookModel,StudentModel,Taskmodel

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'
    def create(self,validated_data):
        user=User.objects.create_user(**validated_data)  
        return user  

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=BookModel
        fields='__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=StudentModel  
        fields='__all__'      

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model=Taskmodel
        fields=['task_name','task_title','due_date','status']