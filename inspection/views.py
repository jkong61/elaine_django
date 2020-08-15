from inspection.models import PrePostJobInspection
import json
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse, Http404
from django.urls import reverse_lazy
from core.models import PipeworkInstance, SlingInstance, SkidInstance, TMMDEInstance
from .forms import GenericInspectionForm
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.core import serializers
from django.views.generic.edit import FormView
from django.core.exceptions import SuspiciousOperation

# Create your views here.
class InspectionCreateView(FormView):
    form_class = GenericInspectionForm
    template_name = 'inspection/add.html'
    login_url = reverse_lazy('login')

    def form_valid(self, form):
        print(self.request.POST)
        return super().form_valid(form)

    def form_invalid(self, form):
        print(self.request.POST)
        return super().form_invalid(form)


class AJAXInspectionEndPoint(TemplateView, LoginRequiredMixin):
    login_url = reverse_lazy('login')

    @method_decorator(csrf_protect)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, *args, **kwargs):
        raise Http404

    def post(self, *args, **kwargs):
        if self.request.is_ajax and self.request.method == "POST":
            json_data = json.loads(self.request.body)
            try:
                id = json_data['data'][:2]
                if(id == 'sk'):
                    query = SkidInstance
                elif(id == 'sl'):
                    query = SlingInstance
                elif(id == 'pw'):
                    query = PipeworkInstance
                elif(id == 'tm'):
                    query = TMMDEInstance
                else:
                    raise KeyError
            except KeyError:
                raise SuspiciousOperation("Invalid JSON")
            data = [{'id': item.id, 'str': str(item)} for item in query.objects.all()]
            return JsonResponse({'data': data}, status=200)
        return JsonResponse({"result": "POST Fail"}, status=400)
