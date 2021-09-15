from question.models import Inquirer
from django.urls import path, include

from question import views

from rest_framework.routers import SimpleRouter

router = SimpleRouter()

router.register(r'inquirers',views.InquirerViewSet)
router.register(r'questions',views.QuestionsViewSet)
router.register(r'answers', views.AnswerViewSet)
router.register(r'user-answers',views.UserAnswerViewSet)
router.register(r'users',views.UserViewSet)
router.register(r'user-inquirers', views.UserInquirerViewSet)


urlpatterns = [
    #path('questionList/', views.QuestionList.as_view()),
    path('inquirers/<int:id>/questions',views.question_list),
    path('inquirers/active',views.get_active_inquirers),
    # path('user-answer/<int:id>', views.put_answers)
]

urlpatterns+= router.urls

