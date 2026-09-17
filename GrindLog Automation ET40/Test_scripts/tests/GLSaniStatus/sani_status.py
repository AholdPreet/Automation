from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import pytest, os, time
from utils.device_key_actions import DeviceKeyAction
from utils.screenshot_util import ScreenshotUtil
from utils.swipe_util import SwipeUtil 
from sani_status_locator import GrindLogSaniStatusLocator as locator
from utils.auth.signin_launcher_helper import SigninLauncherHelper
from utils.data_util import DataUtil
import configparser
from pathlib import Path

#Device : ET40- raj grind log
class TestGrindLogLogin : 

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)
        #path = DataUtil.load_json("grind_log.json")
        # device_config = configparser.ConfigParser()
        # device_config.read(Path(__file__).resolve().parents[1] / "device.properties")
        path = DataUtil.load_json(
                        os.path.join(
                            os.path.dirname(__file__),
                            "test_data",
                            "grind_log.json"
                        )
                    )
        self.test_data = path["test_data"]
        self.cred_data = path["cred_data"]
        self.application = self.test_data["application_name"][0]
        #self.application_data = self.test_data[self.application]
        
    # def test_signin_launcher(self):
    #     DeviceKeyAction.press_home_btn(self.driver)
    #     SigninLauncherHelper(self.driver).sign_in(
    #         username= self.cred_data['username'],
    #         password= self.cred_data['password'],
    #         test_file=__file__
    #     )
    #     print("Login successful")
    
    def test_open_app_drawer(self):
        try :
        #     btn = self.wait.until(
        #         EC.element_to_be_clickable(
        #             (
        #                 AppiumBy.XPATH,
        #                 locator.APP_DRAWER_LOCATOR
        #             )
        #         )
        #     )
        #     print(f"\nButton clicked : {btn.text}")
        #     btn.click()
        #     ele = self.wait.until(
        #         EC.visibility_of_element_located(
        #             (
        #                 AppiumBy.XPATH,
        #                 locator.ALL_APPLICATION_TEXT_LOCATOR
        #             )
        #         )
        #     )
        #     print(f"\nText : {ele.text}")
        #     ScreenshotUtil.take_screenshot(
        #         driver= self.driver,
        #         file_name= "APP_DRAWER_open_screenshot",
        #         test_file= __file__
            SwipeUtil.swipe_up(self.driver)
            self.wait.until(EC.element_to_be_clickable(
                (
                    AppiumBy.XPATH,
                    locator.SEARCH_BOX_LOCATOR
                )
            )).click()
        except Exception as e :
            ScreenshotUtil.take_screenshot(
                driver= self.driver,
                file_name= "Failed_to_open_APP_DRAWER_screenshot",
                test_file= __file__
            )
            raise AssertionError(f"Failed_to_open_app_drawer : {e}")
    
    def test_serach_application(self):
        try :
            application_name = self.application
            self.wait.until(
                EC.visibility_of_element_located(
                    (
                        AppiumBy.XPATH,
                        locator.SEARCH_BOX_LOCATOR
                    )   
                )      
            ).send_keys(application_name)
            self.wait.until(
                EC.visibility_of_element_located(
                    (
                        AppiumBy.XPATH,
                        f'//android.widget.TextView[contains(@text,"{application_name}")]'
                    )
                )
            )
            print(f"\n{application_name} : is present")
            ScreenshotUtil.take_screenshot(
                driver=self.driver,
                file_name=f"{application_name}_found_screenshot",
                test_file=__file__
            )
        except Exception as e :
            print(f"\n{application_name} : is not found")
            ScreenshotUtil.take_screenshot(
                driver=self.driver,
                file_name=f"{application_name}_not_found_screenshot",
                test_file=__file__
            )
            raise AssertionError (f"{application_name} : is not found : {e}")

    def test_open_grind_log(self):
        try:
            application_name = self.application
            self.wait.until(
                EC.visibility_of_element_located(
                    (
                        AppiumBy.XPATH,
                        f'//android.widget.TextView[contains(@text,"{application_name}")]'
                    )
                )
            ).click()
            print(f"\n{application_name} : is opening")
            time.sleep(10)
            ScreenshotUtil.take_screenshot(
                driver=self.driver,
                file_name=f"{application_name}_open_screenshot",
                test_file=__file__
            )
        except Exception as e:
            print(f"\n{application_name} : is not opening")
            ScreenshotUtil.take_screenshot(
                driver=self.driver,
                file_name=f"{application_name}_not_opening_screenshot",
                test_file=__file__
            )
            raise AssertionError (f"{application_name} : is not opening : {e}")

    def test_grind_log_login(self):
        try:
            username = self.wait.until(
                EC.visibility_of_element_located(
                    (
                        AppiumBy.XPATH,
                        locator.USERNAME_LOCATORS
                    )
                )
            )
            print(f"\nEnter username : {self.cred_data['username']}")
            username.send_keys(self.cred_data['username'])
            password = self.wait.until(
                EC.visibility_of_element_located(
                    (
                        AppiumBy.XPATH,
                        locator.PASSWORD_LOCATORS,
                    )
                )
            )
            print(f"\nEnter password : {self.cred_data['password']}")
            password.send_keys(self.cred_data['password'])
            submit_btn = self.wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.XPATH,
                        locator.Login_LOCATORS
                    )
                )
            )
            print("\nSubmit button clicked successfully.")
            ScreenshotUtil.take_screenshot(
                driver=self.driver,
                file_name=f"login_screenshot",
                test_file=__file__
            )
            time.sleep(5)
            submit_btn.click()
        except Exception as e :
            print("Fail to login")
            ScreenshotUtil.take_screenshot(
                driver=self.driver,
                file_name="Fail_to_login_screenshot",
                test_file=__file__
            )
            raise AssertionError (f"Fail to login : {e}")

    def test_verify_grind_log_menu_content(self) :
        try :
            elements = self.wait.until(
                EC.presence_of_all_elements_located(
                    (
                        AppiumBy.XPATH,
                        locator.MENU_CONTENT_LOCATORS
                    )
                )
            )
            for ele in elements :
                print(ele.get_attribute("contentDescription"))
            ScreenshotUtil.take_screenshot(
                driver=self.driver,
                file_name=f"_menu_content_screenshot",
                test_file=__file__
            )
        except Exception as e :
            print("Fail to varify menu content")
            ScreenshotUtil.take_screenshot(
                driver=self.driver,
                file_name="Fail_to_varify_menu_content_screenshot",
                test_file=__file__
            )
            raise AssertionError (f"Fail to varify menu content : {e}")


    def test_sani_status(self):
            try :
                logout_btn = self.wait.until(
                    EC.element_to_be_clickable(
                        (
                            AppiumBy.XPATH,
                            locator.SanitizationStatus_LOCATOR
                        )
                    )
                )
                print(f"\nSanitization Status clicked successfully.")
                logout_btn.click()
                time.sleep(5)
                ScreenshotUtil.take_screenshot(
                    driver=self.driver,
                    file_name=f"sanitization_status_screenshot",
                    test_file=__file__
                )
            except Exception as e :
                print("Fail to click sanitization status")
                ScreenshotUtil.take_screenshot(
                    driver=self.driver,
                    file_name="Fail_to_click_sanitization_status_screenshot",
                    test_file=__file__
                )
                raise AssertionError (f"Fail to click sanitization status : {e}")


    def test_sani_status_exit(self):
                try :
                    logout_btn = self.wait.until(
                        EC.element_to_be_clickable(
                            (
                                AppiumBy.XPATH,
                                locator.Sani_Status_Exit_LOCATOR
                            )
                        )
                    )
                    print(f"\nSanitization Status exit button clicked successfully.")
                    logout_btn.click()
                    time.sleep(5)
                    ScreenshotUtil.take_screenshot(
                        driver=self.driver,
                        file_name=f"sanitization_status_exit_button_screenshot",
                        test_file=__file__
                    )
                except Exception as e :
                    print("Fail to click sanitization status exit button")
                    ScreenshotUtil.take_screenshot(
                        driver=self.driver,
                        file_name="Fail_to_click_sanitization_status_screenshot",
                        test_file=__file__
                    )
                    raise AssertionError (f"Fail to click sanitization status exit button : {e}")

    def test_grind_log_logout(self):
        try :
            logout_btn = self.wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.XPATH,
                        locator.GRIND_LOG_LOGOUT_LOCATORS
                    )
                )
            )
            print(f"\nlogout button clicked successfully.")
            logout_btn.click()
            time.sleep(5)
            ScreenshotUtil.take_screenshot(
                driver=self.driver,
                file_name=f"logout_button_screenshot",
                test_file=__file__
            )
        except Exception as e :
            print("Fail to click logout button")
            ScreenshotUtil.take_screenshot(
                driver=self.driver,
                file_name="Fail_to_click_logout_button_screenshot",
                test_file=__file__
            )
            raise AssertionError (f"Fail to click logout button : {e}")

    def test_navigate_back_to_home_screen(self):
        try :
            DeviceKeyAction.press_home_btn(self.driver)
            DeviceKeyAction.press_back_btn(self.driver)
            ScreenshotUtil.take_screenshot(
                driver= self.driver,
                file_name= "Navigate_back_HOME_Screenshot",
                test_file=__file__
            )
        except Exception as e :
            ScreenshotUtil.take_screenshot(
                driver= self.driver,
                file_name= "Failed_to_navigate_back_to_HOME_Screenshot",
                test_file=__file__
            )
            raise AssertionError(f"Failed to navigate back to home screen : {e}")
    
    # def test_signout_launcher(self):
    #     try :
    #         self.wait.until(
    #             EC.visibility_of_element_located(
    #                 (
    #                     AppiumBy.XPATH,
    #                     locator.LOGOUT_Btn_LOCATOR
    #                 )
    #             )
    #         ).click()
    #         time.sleep(5)
    #         ScreenshotUtil.take_screenshot(
    #             driver= self.driver,
    #             file_name= "Logout_Screenshot",
    #             test_file=__file__
    #         )
    #         print("Logout successful")
    #     except Exception as e :
    #         ScreenshotUtil.take_screenshot(
    #             driver= self.driver,
    #             file_name= "Failed_to_click_logout_btn_Screenshot",
    #             test_file=__file__
    #         )
    #         raise AssertionError (f"Failed to click LOGOUT BUTTON : {e}")

