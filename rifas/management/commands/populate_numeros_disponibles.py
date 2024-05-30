from django.core.management.base import BaseCommand
from rifas.models import NumeroDisponible

class Command(BaseCommand):
    help = 'Populate the NumeroDisponible table with initial data'

    def handle(self, *args, **kwargs):
        for i in range(1, 100):
            NumeroDisponible.objects.get_or_create(numero=i)
        self.stdout.write(self.style.SUCCESS('Successfully populated NumeroDisponible table'))