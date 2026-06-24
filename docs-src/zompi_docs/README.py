from zompi.page import BasePage
import zompi.contrib

class Page(BasePage):
    PAGE_TITLE = "Docs in sviluppo!"

    def __init__(self):
        return zompi.contrib.markdown('')

    def __str__(self):
        return BasePage.page(zompi.contrib.DOC, 'Markdown')