from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone
from datetime import timedelta
from ...models import Question


class Command(BaseCommand):
    help = 'Delete all questions older than 1 week'

    def handle(self, *args, **kwargs):
        time_threshold = timezone.now() - timedelta(days=7)
        questions = Question.objects.filter(created_date__lt=time_threshold)
        questions.delete()

        self.stdout.write(self.style.SUCCESS('Successfully deleted questions older than 1 week'))