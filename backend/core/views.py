from django.views import generic
from django.core.urlresolvers import reverse_lazy

from .forms import CrediCardNumberForm
from .models import CreditCardNumber


class IndexView(generic.FormView):

    template_name = 'core/index.html'
    title = 'Home'
    success_url = reverse_lazy('core:index')
    form_class = CrediCardNumberForm

    def form_valid(self, form, **kwargs):
        cards = CreditCardNumber.objects.create_from_file(
            form.cleaned_data.get('_file')
        )

        context = self.get_context_data(**kwargs)
        context['cards'] = cards
        context['form'] = form

        return self.render_to_response(context)
