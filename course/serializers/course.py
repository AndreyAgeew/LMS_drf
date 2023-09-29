from rest_framework import serializers

from course.models import Course
from course.serializers.lesson import LessonSerializer


class CourseSerializer(serializers.ModelSerializer):
    num_lessons = serializers.SerializerMethodField()
    lessons = LessonSerializer(many=True, read_only=True, source='lesson_set')

    class Meta:
        model = Course
        fields = '__all__'

    def get_num_lessons(self, obj):
        return obj.lesson_set.count()
