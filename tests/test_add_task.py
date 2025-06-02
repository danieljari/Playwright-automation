from playwright.sync_api import expect
from conftest import dbg, step

def test_add_task(loaded_page) -> None:
    """
    Test Case 1: Verify the user can add a new task.

    Approval Criteria:
    - The input field accepts text.
    - Pressing the 'Add Task' button adds the task to the list.
    - The task appears in the task list with the chosen label.

    Steps:
    1. Press the button 'Add Task'.
    2. Enter 'Buy milk' as a title in the input field.
    3. Press the button 'Add Task' in the pop-up window.
    4. Verify that the task was added successfully.
    """

    # Step 1: Press the button 'Add Task'
    step("Press the button 'Add Task'")
    loaded_page.get_by_role("button", name="Add Task").click()

    # Step 2: Enter 'Buy milk' as a title
    step("Enter 'Buy milk' as a title in the input field.")
    title_input = loaded_page.get_by_label("Title")
    expect(title_input).to_be_visible()
    title_input.fill("Buy milk")
    expect(title_input).to_have_value("Buy milk")

    # Step 3: Press the 'Add Task' button in the pop-up
    step("Submit the task form")
    loaded_page.locator("form").get_by_role("button", name="Add Task").click()

    # Confirm task was added
    step("Verify that the task was added successfully")
    expect(loaded_page.get_by_text("Task added successfully")).to_be_visible()
    task_item = loaded_page.get_by_text("Buy milk")
    expect(task_item).to_be_visible()

    dbg("Task 'Buy milk' was added successfully to the list.")