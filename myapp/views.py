from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import HttpResponse
from .models import cons
from .models import comment
from .models import location
from .models import location_two
from .models import TrackDatas



# Create your views here.

def index(request):


    com = comment.objects.all()

    return render(request, 'index.html', {'com':com})

def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')



def track(request):
    if request.method == "POST":
        tracking_id = request.POST.get('tracking_id')
        print (tracking_id)
        try:
            tracking_data = TrackDatas.objects.get(track_Number=tracking_id)
            return render(request, "test.html", {"tracking_data": tracking_data})
        except TrackDatas.DoesNotExist:
            messages.error(request, f'Invalid Tracking ID')
            return redirect("index:track")

    return render(request, 'track.html')


def test(request):

    return render(request, 'test.html')

def result(request):
    loc = location.objects.all()



    return render(request, 'result.html', {'loc':loc})

# location two

def details_two(request):
    loc_two = location_two.objects.all()

    return render(request, 'id_one.html', {'loc_two':loc_two})