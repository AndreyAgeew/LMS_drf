from rest_framework import serializers

from course.models import Lesson


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
