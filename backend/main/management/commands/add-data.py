from django.core.management.base import BaseCommand
from main.models import StoreCityAndCapitals
import requests
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

class Command(BaseCommand):
    help = "it will store the city and capital names in database."

    def handle(self, *args, **options):
        # create super user if running the script for the first time
        try:
            user = User.objects.get(username='admin')
            print(f'superuser already exist with username {user.username}')
        except User.DoesNotExist:
            User.objects.create(username='admin', password=make_password('admin'), is_staff=True, is_superuser=True).save()
            self.stdout.write(self.style.SUCCESS('\nsuperuser created with username & password "admin" ✅ \n'))

        # Make a request to the API to get the country and capital data
        StoreCityAndCapitals.objects.all().delete()
        api_url = "https://countriesnow.space/api/v0.1/countries/capital"
        response = requests.get(api_url)
        data = response.json()
        countries = data['data']
        for country in countries:
            try:
                StoreCityAndCapitals.objects.create(
                    name = country['name'],
                    capital = country['capital']
                ).save()
            except Exception as e:
                self.style.ERROR(e)
        self.stdout.write(
            self.style.SUCCESS('Successfully added data to database ✅ \n')
        )
        self.stdout.write(
            self.style.SUCCESS('starting server ... \n')
        )