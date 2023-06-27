from django.test import TestCase
from. models import Contact
from rest_framework.test import APIClient, APITestCase
from rest_framework import status


class ContactTestCase(APITestCase):
    """
    Test suite for Contact
    """

    def setUp(self) -> None:
        self.client = APIClient()
        self.data = {
            "name": "Kaka Mbweha",
            "message": "Test message from Kilo Mombasa. Do you copy? Over.",
            "email": "kakambweha@anon.co.ke",
        }
        self.url = "/contact/"
        # return super().setUp()

    def test_create_contact(self):
        """
        test ContactViewSet create method
        """
        data = self.data
        response = self.client.post(self.url, data)
        print(f"response: {response.status_code}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Contact.objects.count(), 1)
        self.assertEqual(Contact.objects.get().title, "Kaka Mbweha")

    def test_create_contact_without_name(self):
        """
        test ContactViewSet create method, name  is not in data
        """
        data = self.data
        data.pop("name")
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_contact_when_name_is_blank(self):
        """
        test ContactViewSet create method, name  is blank
        """
        data = self.data
        data["name"] = ""
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_contact_without_message(self):
        """
        test ContactViewSet create method, message  is not in data
        """
        data = self.data
        data.pop("message")
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_contact_when_message_is_blank(self):
        """
        test ContactViewSet create method, message  is blank
        """
        data = self.data
        data["message"] = ""
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_contact_without_email(self):
        """
        test ContactViewSet create method, email  is not in data
        """
        data = self.data
        data.pop("email")
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_contact_when_email_is_blank(self):
        """
        test ContactViewSet create method, email  is blank
        """
        data = self.data
        data["email"] = ""
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_contact_when_email_equals_non_email(self):
        """
        test ContactViewSet create method, email equals non-email value
        """
        data = self.data
        data["email"] = "not an email"
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)