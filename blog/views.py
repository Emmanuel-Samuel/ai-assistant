# import nessary libraries
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import requests

# Create your views here.
bot = ChatBot('Alicia', read_only=False, logic_adapters=['chatterbot.logic.BestMatch'])

list_trainer = ListTrainer(bot)

list_of_responses = [
    "What's your name?", #1
    "I'm a chatbot named Alicia",
    "What is your favorite food?", #3
    "I love pizza",
    "How old are you?", #5
    "I'm ageless",
    "Do you have children?",
    "No",
    "Do you like sports?",
    "No, i don't",
    "Are you human?",
    "No, i'm a bot",
    "Who made you?",
    "My Creator is Emmanuel=",
    "Which languages can you speak?",
    "Only English language"
]

# trains chatbot
list_trainer.train(list_of_responses)

# returns homepage index.html
def index(request):
    return render(request, 'blog/index.html')

# returns chatbot response
def getresponse(request):
    usermessage = request.GET.get('usermessage')
    chatbot_response = bot.get_response(usermessage)
    return HttpResponse(chatbot_response)

# get user weather details based on location
def getweather(request):
    lat_ = str(request.GET.get('lat'))
    long_ = str(request.GET.get('long'))
    response = requests.get("https://api.openweathermap.org/data/2.5/weather?lat="+lat_+"&lon="+long_+"&units=metric&appid=8464b43e2a6b93d8596e6cd611df2ce0")
    jsonresponse = response.json()
    name = jsonresponse['name']
    temp = jsonresponse['main']['temp']
    humid = jsonresponse['main']['humidity']
    description = jsonresponse['weather'][0]['description']
    return JsonResponse(jsonresponse)

# get news info for the user
def getnews(request):
    response = requests.get("https://saurav.tech/NewsAPI/everything/cnn.json")
    jsonresponse = response.json()
    return JsonResponse(jsonresponse)

