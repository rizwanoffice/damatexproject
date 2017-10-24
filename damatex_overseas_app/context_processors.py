from .models import Category

def category(request):
    return {
        'active_categories': Category.objects.all(),
        'request': request,
    }