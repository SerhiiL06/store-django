from .models import Category


def categories(self):
    categories = Category.objects.filter(parent=None)
    return {"categories": categories}
