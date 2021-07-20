from faker import Faker
from django.core.management.base import BaseCommand

from postings.models import Messages


class Command(BaseCommand):
    help = "Generates test data"

    def handle(self, *args, **kwargs):
        self.stdout.write("Creating new data...")
        # Create new posts
        fake = Faker()
        for _ in range(20):
            post = Messages()
            post.username = fake.name()
            post.message = fake.text(max_nb_chars=160)
            post.save()
