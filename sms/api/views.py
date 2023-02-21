from rest_framework.viewsets import ModelViewSet,ViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from api.serializers import *
from main_app.models import *

class Subject_detail(ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

class Staff_add(ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class= StaffSerializer

    '''@action(detail = True , methods = ['post'])
    def add_staff(self,request):
        staff = Staff.get_object()
        serializer = StaffSerializer(data = request.data)
        if serializer.is_valid():
            staff.create(serializer.validated_data[serializer])
            staff.save()
            return Response({'status':'Data saved'})'''

    


class Admin_add(ModelViewSet):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer
    def create(self,validated_data):
        staff =  Staff.objects.create(**validated_data)
        return Staff.objects.create(**validated_data)
    

class Staffs_add(ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer 
    
    

class Course_add(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class Session_add(ModelViewSet):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer

class Custom_add(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer



    '''def create(self,validated_data):
        staff =  Staff.objects.create(**validated_data)
        return staff'''



