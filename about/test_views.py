from django.urls import reverse
from django.test import TestCase
from .forms import CollaborateForm
from .models import About

class TestAboutViews(TestCase):

    def setUp(self):
        """Creates about me content"""
        self.about = About(title="About Me",
            content = "Some content")
        self.about.save()

    def test_render_about_display_page_with_collaborate_form(self):
        """Verifies get request for about me containing a collaboration form"""
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"About Me", response.content)
        self.assertIn(b"Some content", response.content)
        self.assertIsInstance(response.context['collaborate_form'], CollaborateForm)

    def test_successful_collaborate_submission(self):
        """Test for submitting a collaboration request"""
        post_data = {
            'name': 'name_test',
            'email': 'a@b.com',
            'message': 'message_test'
        }
        response = self.client.post(reverse('about'), post_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b'Collaboration request received! I endeavour to respond within 2 working days.',
            response.content
        )
