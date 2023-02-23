from django.test import TestCase
from .forms import SignUpForm

# Create your tests here.
class SignUpFormTest(TestCase):
    """
    Tests for the user registration form
    """

    def testValidPassword(self):
        """
        Checks if a user can sign up using a valid password
        """
        form = SignUpForm(data={"username":'testUser', "email":"testEmail@email.com", "password1":"ekozumi###3474t", "password2":"ekozumi###3474t"})
        self.assertTrue(form.is_valid())

    def testInvalidPassword(self):
        """
        Checks that the form rejects invalid passwords
        """
        form = SignUpForm(data={"username":'testUser', "email":"testEmail@email.com", "password1":"password", "password2":"password"})
        self.assertFalse(form.is_valid())

    def testDuplicateUsers(self):
        """
        Checks that two users cant be created with the same username
        """
        form = SignUpForm(data={"username":'testUser', "email":"testEmail@email.com", "password1":"ekozumi###3474t", "password2":"ekozumi###3474t"})
        form.save()
        form2 = SignUpForm(data={"username":'testUser', "email":"testEmail@email.com", "password1":"ekozumi###3474t", "password2":"ekozumi###3474t"})
        self.assertFalse(form2.is_valid())
    
    def testEmptyUsernameField(self):
        """
        Checks that a username is required
        """
        form = SignUpForm(data={"username":'', "email":"testEmail@email.com", "password1":"ekozumi###3474t", "password2":"ekozumi###3474t"})
        self.assertFalse(form.is_valid())

    def testEmptyEmailField(self):
        """
        Checks that a email is required
        """
        form = SignUpForm(data={"username":'testUser', "email":"", "password1":"ekozumi###3474t", "password2":"ekozumi###3474t"})
        self.assertFalse(form.is_valid())

    def testEmptyPasswordField(self):
        """
        Checks that a password is required
        """
        form = SignUpForm(data={"username":'testUser', "email":"testEmail@email.com", "password1":"", "password2":""})
        self.assertFalse(form.is_valid())


class ViewResponseTest(TestCase):
    """
    Checks the HTTP response of webpages
    """

    def testLoginView(self):
        """
        Tests the login view
        """
        response = self.client.get('/ekozumi/')
        self.assertEqual(response.status_code, 200)
    
    def testRegistrationView(self):
        """
        test the register view
        """
        response = self.client.get('/ekozumi/register/')
        self.assertEqual(response.status_code, 200)
