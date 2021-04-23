from users.models import JProfile, Classification
from django.db.models import Q


def num_user(request):
    num_progressivism = JProfile.objects.filter(political_orientation='progressivism').count()
    num_centrism = JProfile.objects.filter(Q(political_orientation='centrism') | Q(political_orientation='default')).count()
    num_conservatism = JProfile.objects.filter(political_orientation='conservatism').count()

    classification_progressivism = Classification.objects.get(political_orientation='progressivism')
    RateOfIncrease_progressivism = round(((num_progressivism/classification_progressivism.numberOfUser)-1)*100,2)

    classification_centrism = Classification.objects.get(political_orientation='centrism')
    RateOfIncrease_centrism = round(((num_centrism/classification_centrism.numberOfUser)-1)*100,2)

    classification_conservatism = Classification.objects.get(political_orientation='conservatism')
    RateOfIncrease_conservatism = round(((num_conservatism/classification_conservatism.numberOfUser)-1)*100,2)

    context = {
        'num_progressivism' : num_progressivism,
        'num_centrism' : num_centrism,
        'num_conservatism' : num_conservatism,
        'RateOfIncrease_progressivism' : RateOfIncrease_progressivism,
        'RateOfIncrease_centrism' : RateOfIncrease_centrism,
        'RateOfIncrease_conservatism' : RateOfIncrease_conservatism
    }

    return context
