from .models import CategoryChoices


def common_data(request):
    return {
        'categories_navbar': CategoryChoices.choices
    }