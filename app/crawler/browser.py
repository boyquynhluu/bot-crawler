from playwright.sync_api import sync_playwright


class Browser:

    def __init__(self):
        self.playwright = None
        self.browser = None
        self.page = None

    def start(self):

        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(
            headless=False
        )

        self.page = self.browser.new_page()

    def open(self, url: str):

        self.page.goto(
            url,
            wait_until="domcontentloaded"
        )

    def click(self, selector: str):

        self.page.click(selector)

    def wait_for_load_state(self, state: str = "load"):

        self.page.wait_for_load_state(state)

    def close(self):

        if self.browser:
            self.browser.close()

        if self.playwright:
            self.playwright.stop()
