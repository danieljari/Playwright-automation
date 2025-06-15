import pytest
from typing import Generator
from playwright.sync_api import (
    sync_playwright,
    Playwright,
    Browser,
    BrowserContext,
    Page,
)
from datetime import datetime
import inspect
import time


# Settings

HEADLESS = False # Set to True for headless mode 
USE_REMOTE = False  # Set to True to run tests against remote URL, False for local development server
REMOTE_URL = "https://wc-react-todo-app.netlify.app"
LOCAL_URL = "http://localhost:3000"
SLOW_MOTION_DELAY = 1000  # milliseconds between actions when not headless
STEP_DELAY = 1.0  # seconds to pause after each step when not headless


# Debug helpers

def dbg(message: str) -> None:
    """Print debug message with timestamp and function name."""
    now = datetime.now().strftime("%H:%M:%S")
    # Get the name of the function that called this step (1 level up the stack)
    caller = inspect.stack()[1]
    function_name = caller.function
    print(f"[{now}] [{function_name}] {message}")
    
    if not HEADLESS:
        time.sleep(STEP_DELAY)

def step(message: str) -> None:
    """Print step message with counter."""
    # Look if the function step() has an attribute 'counter'
    if not hasattr(step, "counter"):
        step.counter = 1
    else:
        step.counter += 1
    
    now = datetime.now().strftime("%H:%M:%S")
    # Get the name of the function that called this step (1 level up the stack)
    caller = inspect.stack()[1]
    function_name = caller.function
    
    print(f"[{now}] [{function_name}] Step {step.counter}: {message}")
    
    if not HEADLESS:
        time.sleep(STEP_DELAY)


# Fixtures

@pytest.fixture(autouse=True)
def reset_step_counter() -> Generator[None, None, None]:
    """Fixture to Reset step counter before each test."""
    # Does the function step() has an attribute 'counter'?
    if hasattr(step, "counter"):
        del step.counter
    yield

@pytest.fixture(scope="session")
def playwright_instance() -> Generator[Playwright, None, None]:
    """Fixture to start and stop Playwright engine."""
    dbg("Starting Playwright engine")
    # Ensure Playwright is initialized before tests run
    pw = sync_playwright().start()  
    yield pw
    dbg("Stopping Playwright engine")
    pw.stop()

@pytest.fixture(scope="session")
def browser_instance(playwright_instance: Playwright) -> Generator[Browser, None, None]:
    """Fixture to launch and close browser."""
    dbg("Launching browser")
    browser_options = {"headless": HEADLESS}
    if not HEADLESS:
        browser_options["slow_mo"] = SLOW_MOTION_DELAY
    
    # Send two variables to browser_options
    browser = playwright_instance.chromium.launch(**browser_options)
    yield browser
    dbg("Closing browser")
    browser.close()

@pytest.fixture(scope="session")
def browser_context(browser_instance: Browser) -> Generator[BrowserContext, None, None]:
    """Fixture to create and close isolated browser context."""
    dbg("Creating browser context")

    # New seperated profile with its own cache, cookies, and localStorage
    context = browser_instance.new_context()
    yield context
    dbg("Closing browser context")
    context.close()

@pytest.fixture()
def test_page(browser_context: BrowserContext) -> Generator[Page, None, None]:
    """Fixture to open and close browser page."""
    dbg("Opening new page")
    page = browser_context.new_page()
    yield page
    dbg("Closing page")
    page.close()

@pytest.fixture()
def loaded_page(test_page: Page) -> Generator[Page, None, None]:
    """Fixture to navigate page to base URL and clear localStorage."""
    base_url = REMOTE_URL if USE_REMOTE else LOCAL_URL
    dbg(f"Navigating to: {base_url}")
    test_page.goto(base_url)
    test_page.evaluate("localStorage.clear()")
    test_page.reload()
    dbg("Cleared localStorage for clean test state")
    
    yield test_page