from app.crawler.browser import Browser


def Login(browser: Browser):
    try:
        # 1. Mở trang login
        browser.open("https://itviec.com/sign_in")

        if browser.locator("#submitBtn").count() > 0:
            # 2. Click Login with google
            browser.click("#submitBtn")

            # 3. Login with account
            browser.click('[data-email="vanductai.dhv@gmail.com"]')

            # 4. Chờ login hoàn tất
            browser.wait_for_load_state("networkidle")
        else:
            print("Đang được login!")

    except Exception as e:
        print(f"Login Failed!: {e}")
