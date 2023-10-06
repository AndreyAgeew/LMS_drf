from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from course.models import Course
from course.paginators.course import CoursePaginator
from course.serializers.course import CourseSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from jobs.sending_course_update import send_email_course_update
from permissions import IsOwner, IsModerator


class CourseViewSet(ModelViewSet):
    """
        ViewSet для взаимодействия с моделью курса.

        Attributes:
            queryset (QuerySet): Набор объектов курсов, включая предварительно загруженные связанные уроки.
            serializer_class (CourseSerializer): Сериализатор, используемый для преобразования объектов курса в JSON и наоборот.
            pagination_class (CoursePaginator): Плагинатор, для отображения курсов на странице.
    """
    queryset = Course.objects.prefetch_related('lesson_set').all()
    serializer_class = CourseSerializer
    pagination_class = CoursePaginator

    def get_permissions(self):
        """Права доступа"""
        if self.action == 'retrieve':
            permission_classes = [IsOwner | IsModerator | IsAdminUser]
        elif self.action == 'create':
            permission_classes = [IsAdminUser]
        elif self.action == 'destroy':
            permission_classes = [IsOwner | IsAdminUser]
        elif self.action == 'update':
            permission_classes = [IsOwner | IsModerator | IsAdminUser]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def perform_update(self, serializer):
        instance = serializer.save()

        send_email_course_update.delay(instance.pk)

        return Response(serializer.data, status=status.HTTP_200_OK)
