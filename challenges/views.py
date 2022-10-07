from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotAllowed, HttpResponseNotFound, HttpResponseRedirect
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

def monthly_number_challenge(request,month):
    months = list(challenge_text.keys())
    try:
        return HttpResponseRedirect("/challenges/" + months[month-1])
    except:
        return HttpResponseNotFound("Enter a valid month")


def monthly_challenge(request,month):
    try:
        return HttpResponse(challenge_text[month])
    except:
        return HttpResponseNotFound("Enter a valid month")