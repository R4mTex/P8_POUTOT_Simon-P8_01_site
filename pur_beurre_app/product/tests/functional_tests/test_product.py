from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class TestHome(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.browser.get(self.live_server_url + reverse("signup"))

    def tearDown(self):
        self.browser.close()

    def signup(self):
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

    def login(self):
        self.browser.get(self.live_server_url + reverse("login"))

        username = self.browser.find_element("id", "id_username")
        username.send_keys("R4mTex")
        password = self.browser.find_element("id", "id_password")
        password.send_keys("Qwertyuiop1")
        login = self.browser.find_element("id", "send_button")
        login.click()

    def test_home_with_logged_user(self):
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

        self.browser.get(self.live_server_url + reverse("favorite-product", kwargs={'id_user': 1}))
        self.assertEqual(
            self.browser.current_url,
            self.live_server_url + reverse("favorite-product", kwargs={'id_user': 1}),
        )

    def test_home_with_not_logged_user(self):
        self.browser.get(self.live_server_url + reverse("favorite-product", kwargs={'id_user': 1}))
        self.assertEqual(
            self.browser.current_url,
            self.live_server_url + reverse("login") + "?next=/favorite-product/1/",
        )
