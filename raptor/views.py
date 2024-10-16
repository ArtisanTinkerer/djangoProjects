from django.shortcuts import get_object_or_404, render
from django.http import Http404

from .models import Sighting


def sighting_list(request):
    sightings = Sighting.objects.all()

    return render(
        request,
        'raptor/sighting/list.html',
        {'sightings': sightings})

def sighting_detail(request, id):
    try:
        sighting = Sighting.objects.get(id=id)
    except Sighting.DoesNotExist:
        raise Http404("No Sighting found.")
    return render(
    request,
    'raptor/sighting/detail.html',
    {'sighting': sighting}
    )