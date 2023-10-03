import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from course.models import Course, Lesson
from course.serializers.lesson import LessonSerializer
from users.models import User


@pytest.mark.django_db
class TestLessonViews:
    @pytest.fixture
    def client(self):
        return APIClient()

    @pytest.fixture
    def user(self):
        return User.objects.create(email='testuser@example.com',
                                   password='testpassword', role='moderator')

    @pytest.fixture
    def super_user(self):
        super_user = User.objects.create(
            email='testadmin@example.com',
            password='testpassword',
            first_name='Admin',
            last_name='LMS',
            is_staff=True,
            is_superuser=True
        )
        return super_user

    @pytest.fixture
    def course(self):
        return Course.objects.create(title='Test Course', description='Test Description')

    @pytest.fixture
    def lesson(self, course):
        return Lesson.objects.create(title='Test Lesson', description='Test Lesson Description', course=course)

    def test_list_lessons(self, client, user, lesson):
        url = reverse('course:lesson-list')
        client.force_authenticate(user=user)
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK

    def test_create_lesson(self, client, super_user, course):
        url = reverse('course:lesson-create')
        client.force_authenticate(user=super_user)
        data = {
            'title': 'New Lesson',
            'description': 'New Lesson Description',
            'course': course.id,
            'url': 'https://www.youtube.com/testlesson'
        }
        response = client.post(url, data)
        assert response.status_code == status.HTTP_201_CREATED
        assert Lesson.objects.filter(title='New Lesson').exists()

    def test_retrieve_lesson(self, client, user, lesson):
        url = reverse('course:lesson-detail', kwargs={'pk': lesson.id})
        client.force_authenticate(user=user)
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert LessonSerializer(lesson).data == response.data

    def test_update_lesson(self, client, user, lesson):
        url = reverse('course:lesson-update', kwargs={'pk': lesson.id})
        client.force_authenticate(user=user)
        data = {'title': 'Updated Lesson'}
        response = client.patch(url, data)
        assert response.status_code == status.HTTP_200_OK
        assert Lesson.objects.get(id=lesson.id).title == 'Updated Lesson'

    def test_delete_lesson(self, client, super_user, lesson):
        url = reverse('course:lesson-delete', kwargs={'pk': lesson.id})
        client.force_authenticate(user=super_user)
        response = client.delete(url)
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert not Lesson.objects.filter(id=lesson.id).exists()
