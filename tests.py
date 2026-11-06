
from django.test import TestCase
from django.urls import reverse

from it_company.models import ContactRequest


class HomePageTest(TestCase):

    def test_home_page_status_code(self):
        response = self.client.get(reverse("home"))

        self.assertEqual(response.status_code, 200)


class ContactFormTest(TestCase):

    def test_contact_form_creates_request(self):
        response = self.client.post(
            reverse("home"),
            {
                "name": "Test User",
                "email": "test@example.com",
                "phone": "0501234567",
                "message": "Testing contact form",
            },
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(ContactRequest.objects.count(), 1)




    def test_contact_form_invalid_email(self):
        response = self.client.post(
            reverse("home"),
            {
                "name": "Test User",
                "email": "invalid-email",
                "phone": "0501234567",
                "message": "Testing invalid email",
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(ContactRequest.objects.count(), 0)



    def test_contact_form_empty_fields(self):
        response = self.client.post(
            reverse("home"),
            {
                "name": "",
                "email": "",
                "phone": "",
                "message": "",
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(ContactRequest.objects.count(), 0)
        
        

class AdminSecurityTest(TestCase):

    def test_admin_requires_login(self):
        response = self.client.get("/admin/")

        self.assertEqual(response.status_code, 302)
        self.assertIn("/admin/login/", response.url)



from django.test import Client


class ContactCSRFTest(TestCase):

    def test_post_without_csrf_is_rejected(self):
        client = Client(enforce_csrf_checks=True)

        response = client.post(
            reverse("home"),
            {
                "name": "Test User",
                "email": "test@example.com",
                "phone": "0501234567",
                "message": "CSRF test",
            },
        )

        self.assertEqual(response.status_code, 403)
        self.assertEqual(ContactRequest.objects.count(), 0)
