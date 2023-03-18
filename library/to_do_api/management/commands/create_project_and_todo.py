from mixer.backend.django import mixer
from django.core.management.base import BaseCommand

from todo.models import Project, Todo


class Command(BaseCommand):
    help = 'Create project and todo'

    def handle(self, *args, **options):
        for i in range(5):
            mixer.blend(Project)
            mixer.blend(Todo)
        print('done')

