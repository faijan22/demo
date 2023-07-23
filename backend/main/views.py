import random
from main.models import StoreCityAndCapitals
from rest_framework.response import Response 
from rest_framework.decorators import api_view
from rest_framework import status
@api_view(['GET'])
def getRandomCapitalCity(request):
    # Fetch the countries data from database
    countriesData = StoreCityAndCapitals.objects.all().values_list()

    # Pick a random country and its capital
    country_data = random.choice(countriesData)
   
    return Response({'country': country_data[1]})
@api_view(['POST'])
def checkCapital(request):
    data = request.data
    guessed_capital = data.get('capital')
    country = data.get('country')
    try:
        actual_capital = StoreCityAndCapitals.objects.get(name=country)
    except:
        return Response({'error':'Invalid country'}, stauts=status.HTTP_400_BAD_REQUEST)
    if guessed_capital.lower() == actual_capital.capital.lower():
        message = "Correct! You guessed the capital correctly!"
        found = True
    else:
        message = f"Oops! The correct capital is '{actual_capital.capital}' ."
        found = False
    return Response({'details':message, 'found':found})
