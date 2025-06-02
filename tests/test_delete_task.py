from playwright.sync_api import expect
from conftest import dbg, step

def test_delete_task(loaded_page) -> None:
    """
    Test Case 3: Verify the user can delete an existing task.

    Approval Criteria:
    - The delete button (trash icon) is clickable.
    - Clicking the delete button removes the task from the list.
    - The task no longer appears in the task list after deletion.

    Steps:
    1. Add a new task 'Sell Guitar'.
    2. Click the trash icon to delete the task.
    3. Verify that the task was deleted successfully.
    """

    # Step 1: Add a new task 'Sell Guitar'
    step("Add a new task 'Sell Guitar'")
    loaded_page.get_by_role("button", name="Add Task").click()

    title_input = loaded_page.get_by_label("Title")
    expect(title_input).to_be_visible()
    title_input.fill("Sell Guitar")
    expect(title_input).to_have_value("Sell Guitar")

    loaded_page.locator("form").get_by_role("button", name="Add Task").click()
    expect(loaded_page.get_by_text("Task added successfully")).to_be_visible()
    task_item = loaded_page.get_by_text("Sell Guitar")
    expect(task_item).to_be_visible()

    # Step 2: Click the trash icon to delete the task
    step("Click the trash icon to delete the task")
    delete_button = loaded_page.locator("div[class*='todoItem_icon__']").first
    expect(delete_button).to_be_visible()
    delete_button.click()

    # Step 3: Verify that the task was deleted successfully
    step("Verify that the task was deleted successfully")
    expect(loaded_page.get_by_text("Todo Deleted Successfully")).to_be_visible()
    expect(loaded_page.get_by_text("Sell Guitar")).not_to_be_visible()

    dbg("Task 'Sell Guitar' was deleted successfully from the list.")
