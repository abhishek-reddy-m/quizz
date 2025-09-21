from django.test import TestCase
from django.contrib.auth import get_user_model
from my_app.models import Quiz, QuizCategory

User = get_user_model()

class QuizModelTest(TestCase):
    def setUp(self):
        self.examiner = User.objects.create_user(
            username="examiner", password="password", is_examiner=True
        )
        self.category = QuizCategory.objects.create(name="Test Category")

    def test_remaining_property(self):
        quiz = Quiz.objects.create(
            name="Test Quiz",
            subject=self.category,
            description="A test quiz",
            total_time=60,
            total_questions=20,
            examiner=self.examiner,
        )
        self.assertEqual(quiz.remaining, 20)
