import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link1 = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"



@pytest.fixture(scope="function",autouse=True)
def test_name(request):
    print("Starting test " + request.node.name)
    yield
    print("Ending test " + request.node.name)

class TestMain():
    @pytest.fixture(scope="class", autouse=True)
    def tests(self):
        print("Starting all tests")
        yield
        print("Ending all tests")
    @pytest.fixture(scope="function")
    def browser(self):
        print("\nstart browser for test..")
        browser = webdriver.Chrome()
        yield browser
        print("\nquit browser..")
        browser.quit()
    def form_test(self, browser, link):
        browser.get(link)
        firstname = browser.find_elements(By.XPATH, "//input[@placeholder='Input your first name']")
        lastname = browser.find_elements(By.XPATH, "//input[@placeholder='Input your last name']")
        email = browser.find_elements(By.XPATH, "//input[@placeholder='Input your email']")
        phone = browser.find_elements(By.XPATH, "//input[@placeholder='Input your phone:']")
        adress = browser.find_elements(By.XPATH, "//input[@placeholder='Input your address:']")
        assert len(firstname) == 1, "First name input not found"
        firstname[0].send_keys("Rapolas")
        assert len(lastname) == 1, "Last name input not found"
        lastname[0].send_keys("Kubaitis")
        assert len(email) == 1, "Email input not found"
        email[0].send_keys("email.com")
        assert len(phone) == 1, "Phone input not found"
        phone[0].send_keys("123")
        assert len(adress) == 1, "Adress input not found"
        adress[0].send_keys("home 123")
        browser.find_element_by_class_name("btn").click()
        assert browser.find_element_by_tag_name('h1').text == "Congratulations! You have successfully registered!"
    def test1(self, browser):
        self.form_test(browser, link1)
    def test2(self, browser):
        self.form_test(browser, link2)








