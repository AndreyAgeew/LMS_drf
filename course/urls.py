from rest_framework import routers

from course.views.course import CourseViewSet

app_name = 'curse'

router = routers.SimpleRouter()
router.register('course', CourseViewSet)
urlpatterns = [] + router.urls
