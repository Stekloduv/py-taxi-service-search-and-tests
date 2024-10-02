from django.contrib.auth import get_user_model
from django.test import TestCase

from taxi.models import Manufacturer, Driver, Car


class ModelTests(TestCase):

    def test_manufacturer_str(self):
        manufacturer = Manufacturer.objects.create(name="test")
        self.assertEqual(str(manufacturer), "test ")

    def test_driver_str(self):
        driver = get_user_model().objects.create(
            username="test",
            email="test@test.com",
            password="test123321",
            first_name="test_first_name",
            last_name="test_last_name",
        )
        self.assertEqual(
            str(driver),
            f"{driver.username} "
            f"({driver.first_name} "
            f"{driver.last_name})")

    def test_driver_root_address(self):
        driver = get_user_model().objects.create(
            username="test",
            email="test@test.com",
            password="test123321",
            first_name="test_first_name",
            last_name="test_last_name",
        )
        self.assertEqual(driver.get_absolute_url(), "/drivers/1/")

    def test_car_str(self):
        manufacturer = Manufacturer.objects.create(name="test")
        car = Car.objects.create(model="test", manufacturer=manufacturer)
        self.assertEqual(str(car), "test")
