from django.test import TestCase
from.models import Answer, Question

# Create your tests here.

class QuestionTestCase(TestCase):
    def setUp(self) -> None:
        first_question = Question.objects.create(question="this is first question")
        Answer.objects.create(question=first_question, answer="first answer")

    def test_question_get_answered(self):
        first_question = Answer.objects.get(question__question="this is first question")
        self.assertEqual(first_question.answer, "first answer")
