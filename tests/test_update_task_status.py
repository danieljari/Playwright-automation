from playwright.sync_api import expect
from conftest import dbg, step

def test_update_task_status(loaded_page) -> None:
    """
    Test Case 2: Verify the user can mark a task as completed and unmark it.

    Approval Criteria:
    - Completed task appears with CSS - text-decoration-line: line-through
    - Completed task has checkbox with opacity 1
    - Unmarked task returns to normal text without line-through
    - Unmarked task has checkbox with opacity 0

    Steps:
    1. Add a new task.
    2. Click the task's checkbox.
    3. Verify the task is marked as completed and has opacity 1.
    4. Click the checkbox again to unmark the task
    5. Verify the task is not marked and has opacity 0.
    """

    # Step 1: Add a new task
    step("Add a new task")
    loaded_page.get_by_role("button", name="Add Task").click()
    title_input = loaded_page.get_by_label("Title")
    expect(title_input).to_be_visible()

    # Enter 'Sell cat' as a title
    title_input.fill("Sell cat")
    expect(title_input).to_have_value("Sell cat")

     # Press the 'Add Task' button in the pop-up
    loaded_page.locator("form").get_by_role("button", name="Add Task").click()
    expect(loaded_page.get_by_text("Task added successfully")).to_be_visible()
    
    # Confirm task was added
    task_item = loaded_page.get_by_text("Sell cat")
    expect(task_item).to_be_visible()

    # Step 2: Click the task's checkbox
    step("Click the task's checkbox")
    task_container = loaded_page.locator("div").filter(has_text="Sell cat")
    checkbox = task_container.locator("div[class*='svgBox']")
    expect(checkbox).to_be_visible()
    

    # Step 3: Verify the task is marked as checked and has line-through
    checkbox.click()
    step("Verify the task is marked as completed")
    path = checkbox.locator("svg > path")
    opacity = path.get_attribute("opacity")
    expect(path).to_have_attribute("opacity", "1")
    expect(task_item).to_have_css("text-decoration-line", "line-through")

    # Step 4: Click the checkbox again to unmark the task
    step("Click the checkbox again to unmark the task")
    checkbox.click()

    # Step 5: Verify the task is not marked and has no line-through
    step("Verify the task is unmarked and has no line-through")
    opacity = path.get_attribute("opacity")
    expect(path).to_have_attribute("opacity", "0")
    expect(task_item).not_to_have_css("text-decoration-line", "line-through")

    dbg("Updated status of a task works as expected.")