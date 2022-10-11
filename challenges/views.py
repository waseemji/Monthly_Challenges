from urllib import response
from django.shortcuts import redirect, render
from django.http import HttpResponse,HttpResponseNotAllowed, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse
from django.template.loader import render_to_string
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
    "november" : None,
    "december" : None
}

def index(request):
    # redirect_url = ""
    months = list(challenge_text.keys())
    # for month in months:
    #     capitalized_month = month.capitalize()
    #     month_path = reverse("month-challenge", args=[month])
    #     redirect_url += f"<li><a href = '{month_path}'>{capitalized_month}</a></li>"
    # response = f"<ul>{redirect_url}</ul>"
    # return HttpResponse(response)
    return render(request,"challenges/index.html",{
        "months":months
    })

def monthly_number_challenge(request,month):
    months = list(challenge_text.keys())
    if month>12:
        raise Http404('404.html')
    redirect_month = months[month-1]
    redirect_path = reverse("month-challenge", args = [redirect_month]) # /challenges/january
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request,month):
    try:

        challenge = challenge_text[month]
        return render(request,"challenges/challenges.html",{
            "text":challenge,
            "title":month
        })
        # response_data = render_to_string("challenges/challenges.html")
        # # response_data = f"<h1>{challenge}</h1>"
        # return HttpResponse(response_data)
    except:
        raise Http404('404.html')
        # response_data = render_to_string('404.html')
        # return HttpResponseNotFound(response_data)