from django.shortcuts import render


def moodbot(request):
    return render(request, 'moodbot.html')
