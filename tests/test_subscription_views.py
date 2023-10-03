import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from course.models import Course, Subscription


@pytest.mark.django_db
class TestSubscriptionViews:
    @pytest.fixture
    def client(self):
        return APIClient()

    @pytest.fixture
    def user(self):
        return get_user_model().objects.create_user(username='testuser', password='testpassword')

    @pytest.fixture
    def course(self):
        return Course.objects.create(title='Test Course', description='Test Description')

    @pytest.fixture
    def subscription(self, user, course):
        return Subscription.objects.create(user=user, course=course)

    def test_subscribe_course(self, client, user, course):
        url = reverse('course:subscribe-course', kwargs={'course_id': course.id})
        client.force_authenticate(user=user)
        response = client.post(url)
        assert response.status_code == status.HTTP_201_CREATED
        assert Subscription.objects.filter(user=user, course=course).exists()

    def test_unsubscribe_course(self, client, user, subscription):
        url = reverse('course:unsubscribe-course', kwargs={'course_id': subscription.course.id})
        client.force_authenticate(user=user)
        response = client.delete(url)
        assert response.status_code == status.HTTP_200_OK
        assert not Subscription.objects.filter(id=subscription.id).exists()
