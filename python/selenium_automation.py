"""Utility helpers for Selenium-based automation flows.

Usage example
-------------
>>> from python import selenium_automation
>>> selenium_automation.create_driver(factory=lambda: object())
object()
"""

from __future__ import annotations

from typing import Any, Callable, Mapping

try:  # pragma: no cover - optional dependency
    from selenium import webdriver
    from selenium.webdriver.common.by import By
except Exception:  # pragma: no cover
    webdriver = None  # type: ignore
    By = None  # type: ignore

__all__ = ["create_driver", "login_and_capture"]


def create_driver(*, browser: str = "chrome", headless: bool = True, factory: Callable[[], Any] | None = None) -> Any:
    """Return a Selenium WebDriver instance for ``browser``."""

    if factory is not None:
        return factory()
    if webdriver is None:
        raise RuntimeError("Selenium must be installed to create a driver")
    if browser.lower() == "chrome":
        options = webdriver.ChromeOptions()
        if headless:
            options.add_argument("--headless=new")
        return webdriver.Chrome(options=options)
    if browser.lower() == "firefox":
        options = webdriver.FirefoxOptions()
        if headless:
            options.add_argument("-headless")
        return webdriver.Firefox(options=options)
    raise ValueError(f"Unsupported browser: {browser}")


def login_and_capture(
    driver: Any,
    *,
    url: str,
    username: str,
    password: str,
    selectors: Mapping[str, str],
) -> str:
    """Perform a login flow and return page HTML."""

    if By is None:
        raise RuntimeError("Selenium must be installed to use login helpers")
    driver.get(url)
    driver.find_element(By.CSS_SELECTOR, selectors["username"]).send_keys(username)
    driver.find_element(By.CSS_SELECTOR, selectors["password"]).send_keys(password)
    driver.find_element(By.CSS_SELECTOR, selectors["submit"]).click()
    return driver.page_source
