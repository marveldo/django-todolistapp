from rest_framework import serializers
from Tasks.models import Task,Profile

class Profileserializer(serializers.ModelSerializer):

    class Meta :
        model = Profile
        fields = '__all__'
        tasks = serializers.SerializerMethodField()

    def get_tasks(self,obj):
        tasks = obj.task_set.all()
        serializer = TaskSerializer(tasks, many= True)
        return serializer.data
        
class TaskSerializer(serializers.ModelSerializer):
    profile = Profileserializer(many = False)
    class Meta :
        model = Task
        fields = '__all__'
      