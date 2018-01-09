from django.views.generic import TemplateView
from .models import (Sales, Client, Product)


class HomeView(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        context = {

        }
        return self.render_to_response(context)
