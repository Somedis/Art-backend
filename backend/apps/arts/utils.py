from django.db.models import Count

from category.models import Category


class DataMixin:

    paginate_by = 21

    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Category.objects.annotate(Count('arts'))

        context['cats'] = cats

        if 'cat_selected' not in context:
            context['cat_selected'] = 0

        return context
