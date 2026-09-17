class GrindLogLoginLocator :

    APP_DRAWER_LOCATOR = '//android.widget.TextView[@text="App Drawer"]'

    ALL_APPLICATION_TEXT_LOCATOR = '//android.widget.TextView[@text="All Applications"]'

    SEARCH_BOX_LOCATOR = '//android.widget.EditText[@resource-id="com.android.launcher3:id/search_container_all_apps"]'

    USERNAME_LOCATORS = '//android.widget.EditText[@resource-id="ctl00_MainContent_UserSignon"]'

    PASSWORD_LOCATORS = '//android.widget.EditText[@resource-id="ctl00_MainContent_Password"]'

    Login_LOCATORS = '//android.widget.Button[@resource-id="ctl00_MainContent_LoginButton"]'
    #Login_LOCATORS = '//android.widget.Button[@resource-id="ctl00_Toolbar_TitleBarButtons1_Submit"]'

    SUBMIT_Btn_LOCATORS = '//android.widget.Button[@resource-id="ctl00_Toolbar_TitleBarButtons1_Submit"]'

    MENU_CONTENT_LOCATORS = '//*[@resource-id="ctl00_MainContent_MenuTable1"]//*[@content-desc]'

    # GRIND_LOG_LOGOUT_LOCATORS = '//android.widget.Button[@resource-id="ctl00_Toolbar_TitleBarButtons1_Menu"]'
    GRIND_LOG_LOGOUT_LOCATORS = '//android.widget.TextView[@text="Exit"]'

    LOGOUT_Btn_LOCATOR = '//android.view.View[@content-desc="Logout"]'