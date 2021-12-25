from decimal import Decimal
from django.test import RequestFactory
from django.contrib.auth import get_user_model
from mainapp.models import Category, Notebook, CartProduct, Cart, Customer
from mainapp.utils import recalc_cart
from mainapp.views import (
    BaseView,
    AddToCartView,
    DeleteFromCartView,
)
from PIL import Image
from django.core.files.base import File
from io import BytesIO
from django.contrib.messages.storage.fallback import FallbackStorage
import pytest
from django.conf import settings
from django.test import Client


User = get_user_model()


@pytest.fixture
def get_image_file_prod():
    name = "notebook.jpg"
    ext = "jpeg"
    size = (700, 700)
    color = (256, 0, 0)
    file_obj = BytesIO()
    image = Image.new("RGB", size=size, color=color)
    image.save(file_obj, ext)
    file_obj.seek(0)
    return File(file_obj, name=name)


@pytest.fixture
def user(db):
    user = User.objects.create(username="testuser", password="password")
    return user


@pytest.fixture
def customer(db, user):
    customer = Customer.objects.create(
        user=user, phone="7777777", address="Test_Address"
    )
    return customer


@pytest.fixture
def category(db):
    category = Category.objects.create(name="Ноутбуки", slug="notebooks")
    return category


@pytest.fixture
def notebook(db, get_image_file_prod, category):
    image = get_image_file_prod
    notebook = Notebook.objects.create(
        category=category,
        title="Test Notebook",
        slug="test-slug",
        image=image,
        price=Decimal("50000.00"),
        diagonal="17.3",
        display_type="IPS",
        processor_freq="3.4 GHz",
        ram="6 Gb",
        video="GeForce RTX",
    )
    return notebook


@pytest.fixture
def cart(db, customer):
    cart = Cart.objects.create(owner=customer)
    return cart


@pytest.fixture
def cart_product(db, customer, cart, notebook):
    cart_product = CartProduct.objects.create(
        user=customer, cart=cart, content_object=notebook
    )
    return cart_product


@pytest.mark.parametrize("expected", [1, Decimal("70000.0")])
def test_add_to_cart_without_cls(cart, cart_product, expected):
    cart.products.add(cart_product)
    recalc_cart(cart)
    assert cart.products.count(), cart.final_price == expected


@pytest.mark.parametrize("expected", [302, "/cart/"])
def test_response_from_add_to_cart_view(user, notebook, expected):
    factory = RequestFactory()
    request = factory.get("")
    setattr(request, "session", "session")
    messages = FallbackStorage(request)
    setattr(request, "_messages", messages)
    request.user = user
    response = AddToCartView.as_view()(request, ct_model="notebook", slug="test-slug")
    assert response.status_code, response.url == expected


@pytest.mark.parametrize("expected", [302, "/cart/"])
def test_response_from_delete_from_cart_view(user, notebook, cart_product, expected):
    factory = RequestFactory()
    request = factory.get("")
    setattr(request, "session", "session")
    messages = FallbackStorage(request)
    setattr(request, "_messages", messages)
    request.user = user
    response = DeleteFromCartView.as_view()(
        request, ct_model="notebook", slug="test-slug"
    )
    assert response.status_code, response.url == expected


def test_response_from_base_view(user):
    factory = RequestFactory()
    request = factory.get("")
    request.user = user
    response = BaseView.as_view()(request)
    assert response.status_code == 200


def test_categorydetail_view(category):
    c = Client()
    response = c.get("/category/notebooks/")
    assert response.status_code == 200
