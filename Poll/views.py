from django.shortcuts import render

def poll(request):
    return render(request, 'poll.html')