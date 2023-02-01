from django import template
from menu.models import Menu, Category, Products
register = template.Library()


@register.inclusion_tag('menu/menu.html', takes_context=True)
def show_top_menu(context):
    menu_items = Menu.objects.all()
    category = Category.objects.all()
    products = Products.objects.all()
    return {
        "menu_items": menu_items,
        "category": category,
        "products": products,
    }

