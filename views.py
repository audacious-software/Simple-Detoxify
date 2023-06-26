import json

from detoxify import Detoxify

from django.conf import settings
from django.http import HttpResponse
from django.utils.text import slugify
from django.views.decorators.csrf import csrf_exempt

DETOXIFY_MODELS = (
    'original',
    'unbiased',
    'multilingual',
)

TORCH_DIR = settings.MEDIA_ROOT + 'torch/' # Ignored?

@csrf_exempt
def simple_detoxify_score(request): # pylint: disable=too-many-branches
    scores = {}

    content = request.POST.get('s', request.GET.get('s', ''))

    if content != '':
        for model in DETOXIFY_MODELS:
            model_scores = Detoxify(model).predict(content)
            
            for key in model_scores:
                model_scores[key] = float(model_scores[key])

            scores[slugify(model).replace('-', '_')] = model_scores

    return HttpResponse(json.dumps(scores, indent=2), content_type='application/json', status=200)
