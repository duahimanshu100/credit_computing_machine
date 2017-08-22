from django.http.response import Http404, HttpResponseRedirect
from .models import PrivateUrl
from app.views import manage_group

dict_private_urls_view = {
    'manage_credit_score':manage_group,
    'user_credit':manage_group,

}

def privateurl_view(request, action, token):
    obj = PrivateUrl.objects.get_or_none(action, token)
    ok = False
    if not obj or not obj.is_available():
        # fail or expired
        raise Http404
    elif dict_private_urls_view.get(action):
        view = dict_private_urls_view.get(action)
        return view(request,obj.id)
        # sucess case
    if not ok:
        raise Http404
    return HttpResponseRedirect('/')


