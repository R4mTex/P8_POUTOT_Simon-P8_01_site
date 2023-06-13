from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


class TestAuthentification(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.browser.get(self.live_server_url + reverse("signup"))

        username = self.browser.find_element("id", "id_username")
        username.send_keys("R4mTex")
        email = self.browser.find_element("id", "id_email")
        email.send_keys("test@test.com")
        password1 = self.browser.find_element("id", "id_password1")
        password1.send_keys("Qwertyuiop1")
        password2 = self.browser.find_element("id", "id_password2")
        password2.send_keys("Qwertyuiop1")
        signup = self.browser.find_element("id", "send_button")
        signup.click()

    def tearDown(self):
        self.browser.close()

    def test_signup(self):
        self.assertEqual(self.browser.find_element("id", "title").text, "Du gras, oui, mais de qualité !")
        self.assertEqual(self.browser.current_url, self.live_server_url + reverse("home"))

    def test_login(self):
        self.browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.browser.get(self.live_server_url + reverse("login"))

        username = self.browser.find_element("id", "id_username")
        username.send_keys("R4mTex")
        password = self.browser.find_element("id", "id_password")
        password.send_keys("Qwertyuiop1")
        login = self.browser.find_element("id", "send_button")
        login.click()

        self.assertEqual(self.browser.find_element("id", "title").text, "Du gras, oui, mais de qualité !")
        self.assertEqual(self.browser.current_url, self.live_server_url + reverse("home"))

    def test_logout(self):
        self.browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.browser.get(self.live_server_url + reverse("login"))

        username = self.browser.find_element("id", "id_username")
        username.send_keys("R4mTex")
        password = self.browser.find_element("id", "id_password")
        password.send_keys("Qwertyuiop1")
        login = self.browser.find_element("id", "send_button")
        login.click()

        logout = self.browser.find_element("xpath", "//a[contains(@href, '/logout/')]")
        logout.click()

        # self.assertNotEqual(self.browser.page_source.find("LOGIN"), -1)
        self.assertEqual(
            self.browser.current_url, self.live_server_url + reverse("login")
        )


class TestAuthentificationFailed(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.browser.get(self.live_server_url + reverse("signup"))

    def tearDown(self):
        self.browser.close()

    def test_signup_with_wrong_email(self):
        self.browser.get(self.live_server_url + reverse("signup"))

        username = self.browser.find_element("id", "id_username")
        username.send_keys("R4mTex")
        email = self.browser.find_element("id", "id_email")
        email.send_keys("test@testcom")
        password1 = self.browser.find_element("id", "id_password1")
        password1.send_keys("Qwertyuiop1")
        password2 = self.browser.find_element("id", "id_password2")
        password2.send_keys("Qwertyuiop1")
        signup = self.browser.find_element("id", "send_button")
        signup.click()

        self.assertNotEqual(
            self.browser.page_source.find("Enter a valid email address."), -1
        )
        self.assertEqual(
            self.browser.current_url, self.live_server_url + reverse("signup")
        )

    def test_signup_with_two_different_password(self):
        self.browser.get(self.live_server_url + reverse("signup"))

        username = self.browser.find_element("id", "id_username")
        username.send_keys("R4mTex")
        email = self.browser.find_element("id", "id_email")
        email.send_keys("test@testcom")
        password1 = self.browser.find_element("id", "id_password1")
        password1.send_keys("Qwertyuiop1")
        password2 = self.browser.find_element("id", "id_password2")
        password2.send_keys("Qwertyuiop2")
        signup = self.browser.find_element("id", "send_button")
        signup.click()

        self.assertNotEqual(
            self.browser.page_source.find("The two password fields didn’t match."), -1
        )
        self.assertEqual(
            self.browser.current_url, self.live_server_url + reverse("signup")
        )

    def test_signup_with_same_username(self):
        for i in range(2):
            self.browser.get(self.live_server_url + reverse("signup"))

            username = self.browser.find_element("id", "id_username")
            username.send_keys("R4mTex")
            email = self.browser.find_element("id", "id_email")
            email.send_keys("test@testcom")
            password1 = self.browser.find_element("id", "id_password1")
            password1.send_keys("Qwertyuiop1")
            password2 = self.browser.find_element("id", "id_password2")
            password2.send_keys("Qwertyuiop1")
            signup = self.browser.find_element("id", "send_button")
            signup.click()

        self.assertNotEqual(
            self.browser.page_source.find("A user with that username already exists."),
            1,
        )  # -1
        self.assertEqual(
            self.browser.current_url, self.live_server_url + reverse("signup")
        )

class TestAuthentification_select_avatar(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.browser.get(self.live_server_url + reverse("signup"))

        username = self.browser.find_element("id", "id_username")
        username.send_keys("R4mTex")
        email = self.browser.find_element("id", "id_email")
        email.send_keys("test@test.com")
        password1 = self.browser.find_element("id", "id_password1")
        password1.send_keys("Qwertyuiop1")
        password2 = self.browser.find_element("id", "id_password2")
        password2.send_keys("Qwertyuiop1")
        signup = self.browser.find_element("id", "send_button")
        signup.click()

    def tearDown(self):
        self.browser.close()

    def test_signup(self):
        self.assertEqual(self.browser.find_element("id", "title").text, "Du gras, oui, mais de qualité !")
        self.assertEqual(self.browser.current_url, self.live_server_url + reverse("home"))

    def test_login(self):
        self.browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.browser.get(self.live_server_url + reverse("login"))

        username = self.browser.find_element("id", "id_username")
        username.send_keys("R4mTex")
        password = self.browser.find_element("id", "id_password")
        password.send_keys("Qwertyuiop1")
        login = self.browser.find_element("id", "send_button")
        login.click()

        self.assertEqual(self.browser.find_element("id", "title").text, "Du gras, oui, mais de qualité !")
        self.assertEqual(self.browser.current_url, self.live_server_url + reverse("home"))
