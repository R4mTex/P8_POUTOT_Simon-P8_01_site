
from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# driver.get("https://www.google.com")


class TestAuthentification(StaticLiveServerTestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
        chrome_driver_binary = r"C:\Users\spout\.wdm\drivers\chromedriver\win32\112.0.5615\chromedriver.exe"
        self.browser = webdriver.Chrome(chrome_driver_binary, chrome_options=options)
        #self.browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
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
        # Ouvrir le navigateur avec le webdriver
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
        # Ouvrir le navigateur avec le webdriver
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
