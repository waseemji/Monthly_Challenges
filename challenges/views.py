from urllib import response
from django.shortcuts import redirect, render
from django.http import HttpResponse,HttpResponseNotAllowed, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# Create your views here.

challenge_text = {
    "january" : "the challenge for january",
    "february" : "February we'll do this",
    "march" : "March is here",
    "april" : "Thaths april",
    "may" : "May is here",
    "june" : "what should we do in june",
    "july" : " Exaaams are here",
    "august" : " College katham ho gaya",
    "september": "Blaank",
    "october" : "Gandhi Jayanthi",
    "november" : "November aagaya",
    "december" : " 2022 is over"
}

def index(request):
    redirect_url = ""
    months = list(challenge_text.keys())
    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        redirect_url += f"<li><a href = '{month_path}'>{capitalized_month}</a></li>"
    response = f"<ul>{redirect_url}</ul>"
    return HttpResponse(response)

def monthly_number_challenge(request,month):
    months = list(challenge_text.keys())
    redirect_month = months[month-1]
    if month>12:
        return HttpResponseNotFound("<h1>Enter a valid month</h1>")
    redirect_path = reverse("month-challenge", args = [redirect_month]) # /challenges/january
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request,month):
    try:
        challenge = challenge_text[month]
        response_data = f"<h1>{challenge}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>Enter a valid month</h1>")