from django.db import models
from mainapp.models import *


def recalc_cart(cart):
    cart_data = cart.products.aggregate(models.Sum("final_price"), models.Count("id"))
    if cart_data.get("final_price__sum"):
        cart.final_price = cart_data["final_price__sum"]
    else:
        cart.final_price = 0
    cart.total_products = cart_data["id__count"]
    cart.save()


def get_models_for_count(*model_names):
    return [models.Count(model_name) for model_name in model_names]


def get_product_url(obj, viewname):
    ct_model = obj.__class__._meta.model_name
    return reverse(viewname, kwargs={"ct_model": ct_model, "slug": obj.slug})
