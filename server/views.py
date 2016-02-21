import requests

from django.http import JsonResponse
from django.shortcuts import render
from models import EcoregionSpecies, Genus, Species


def index(request):
    return render(request, 'tagalong/index.html')


def species(request, eco_code):
    specs = EcoregionSpecies.objects.filter(ecoregion_code=eco_code)
    imgs = {}
    imgs['imgs'] = []

    for s in specs:
        spec = Species.objects.get(species_id=s.species_id)
        gen = Genus.objects.get(genus_id=spec.genus_id)

        url = 'http://api.gbif.org/v1/species/match?'
        gn = 'genus=' + gen.genus
        sp = '&name=' + spec.species

        r = requests.get(url + gn + sp)
        gbif = r.json()

        try:
            print gbif['usageKey']

            url = 'http://api.gbif.org/v1/species/'
            uri = str(gbif['usageKey']) + '/media'
            r = requests.get(url + uri)
            try:
                imgs['imgs'].append(r.json()['results'][0]['identifier'])
            except:
                pass
        except:
            pass

        if len(imgs['imgs']) > 6:
            break

    return JsonResponse(imgs)
