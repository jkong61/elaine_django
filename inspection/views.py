from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse, Http404
from django.urls import reverse_lazy
from .models import CalibrationInspection
import json
from .forms import GenericInspectionForm
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import FormView

# Create your views here.
class InspectionCreateView(FormView):
    form_class = GenericInspectionForm
    template_name = 'inspection/add.html'
    login_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
    # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add Inspection'
        context['header'] = 'Add Inspection Certificate'
        return context

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

    # @method_decorator(csrf_protect ,name='dispatch')
    def post(self, *args, **kwargs):
        if self.request.is_ajax and self.request.method == "POST":
            # decode method required to decode the request body
            raw_json_data = self.request.body
            # print(json.loads(raw_json_data))
            return JsonResponse({"result": "POST OK"}, status=200)
        return JsonResponse({"result": "POST Fail"}, status=400)
