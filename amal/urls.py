"""

This file contains urls for 
scraping data from Amazom and Aliaba

"""
import re

AMAZON_URL = "https://www.amazon.com/"
ALIBABA_URL = "https://www.alibaba.com/"

# CSS selector
AMAZON_SEARCH_TAB = "#twotabsearchtextbox" 
ALIBABA_SEARCH_TAB = "#J_SC_header > header > div.sc-hd-row.sc-hd-main > div.sc-hd-cell.sc-hd-searchbar-wrap > div > div > form > div.ui-searchbar-main > input"

AMAZON_ITEMS_PAGE = "https://www.amazon.com/dp/"
ALIBABA_ITEMS_PAGE = "https://www.alibaba.com/product-detail/"

#for scraping item code

AMAZON_ITEM_CODE_TAGS = {"tags": ["data-asin"],
                        "value": "data-asin",
                        "element": "div"}
ALIBABA_ITEM_CODE_TAGS = {"tags": ["data-domdot","data-spm-anchor-id"],
                            "value": "href",
                            "element":"a",
                            "refresh": "/html/body/div[1]/div[2]/div[2]/div[3]/div[1]/div[2]/div[1]/div[2]/div[7]/div[1]/div[10]/a",
                            "regex": re.compile(f"^{ALIBABA_ITEMS_PAGE}.*$")}

# Amazon item page x_path for details
class AmazonItemsPaths:
    PRODUCT_X_PATH = '//*[@id="productTitle"]'
    PRICE_X_PATH = '//*[@id="priceblock_ourprice"]'
    PRODUCT_PRICE_RATE_X_PATH = './/span[contains(concat(" ",normalize-space(@class)," ")," a-size-small ")][(count(preceding-sibling::*)+1) = 2]'
    PRODUCT_INFO_X_PATH = '//*[@id="feature-bullets"]/ul'

# Alibaba item page x_path for details
class AlibabaItemsPaths:
    PRODUCT_X_PATH = '//*[@class="ma-title"]'
    PRICE_X_PATH = '//*[@class="ma-ref-price"]'
    PRODUCT_PRICE_RATE_X_PATH = '//*[@class="ma-reference-price"]'
    PRODUCT_INFO_X_PATH = '//*[@id="J-rich-text-description"]'