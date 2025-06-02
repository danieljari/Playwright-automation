from playwright.sync_api import expect
from conftest import dbg, step

def test_local_storage(loaded_page) -> None:
    """
    Test Case 5: Verify tasks persist on page reload (LocalStorage).
    
    Approval Criteria:
    - The input field accepts text for task creation.
    - Task is successfully added to the list.
    - Task remains visible after page reload.
    - LocalStorage functionality works correctly.

    Steps:
    1. Add a new task
    2. Reload the page.
    3. Verify that the task persists after reload.
    """
    # Step 1: Add a new task
    step("Add a new task")
    loaded_page.get_by_role("button", name="Add Task").click()
    
    # Enter 'Feed the cat' as a title
    title_input = loaded_page.get_by_label("Title")
    expect(title_input).to_be_visible()
    title_input.fill("Feed the cat")
    expect(title_input).to_have_value("Feed the cat")
    
    # Press the 'Add Task' button in the pop-up
    loaded_page.locator("form").get_by_role("button", name="Add Task").click()
    expect(loaded_page.get_by_text("Task added successfully")).to_be_visible()

    # Confirm task was added
    task_item = loaded_page.get_by_text("Feed the cat")
    expect(task_item).to_be_visible()
    dbg("Task 'Feed the cat' was added successfully to the list.")
    
    # Step 2: Reload the page
    step("Reload the page")
    loaded_page.reload()
    
    # Step 3: Verify task persists after reload
    step("Verify that the task persists after reload")
    task_item_after_reload = loaded_page.get_by_text("Feed the cat")
    expect(task_item_after_reload).to_be_visible()
    dbg("Task 'Feed the cat' persisted after page reload - LocalStorage working correctly")