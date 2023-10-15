from django.contrib.auth.models import User
from django.http import Http404
from django.views.generic import ListView

from .models import Work, Profile

WORKS_PER_PAGE = 6


class IndexView(ListView):
    model = Work
    template_name = 'work/index.html'
    paginate_by = WORKS_PER_PAGE
    profile = None

    def get_queryset(self):
        """Set profile attribute."""
        try:
            self.profile = Profile.objects.select_related('user').get(
                user=User.objects.get(username='admin')
            )
        except Exception:
            raise Http404

        return Work.objects.all()

    def get_context_data(self, **kwargs):
        """Add profile model to context."""
        context = super().get_context_data(**kwargs)
        context['profile'] = self.profile
        return context
