from playwright.sync_api import expect
from conftest import dbg, step

def test_filter_by_status(loaded_page) -> None:
    """
    Test Case 4: Verify the user can filter tasks by status "completed".

    Approval Criteria:
    - The filter dropdown accepts status selection.
    - Filtering by 'completed' when no completed tasks exist shows "No Todos".
    - The filter functionality works correctly to hide/show appropriate tasks.

    Steps:
    1. Add a new task.
    2. Select 'completed' filter from the status dropdown.
    3. Verify that incomplete tasks are hidden.
    4. Verify that "No Todos" message appears when no completed tasks exist.
    """
    
    # Step 1: Add a new incomplete task
    step("Add a new task")
    loaded_page.get_by_role("button", name="Add Task").click()
    title_input = loaded_page.get_by_label("Title")
    expect(title_input).to_be_visible()
    title_input.fill("Find cat")
    expect(title_input).to_have_value("Find cat")
    
    # Submit the task form
    loaded_page.locator("form").get_by_role("button", name="Add Task").click()

    # Confirm task was added
    expect(loaded_page.get_by_text("Task added successfully")).to_be_visible()
    task_item = loaded_page.get_by_text("Find cat")
    expect(task_item).to_be_visible()
    
    # Step 2: Filter by completed tasks
    step("Select 'completed' filter from the status dropdown")
    status_filter = loaded_page.locator('#status')
    expect(status_filter).to_be_visible()
    status_filter.select_option(value='complete')
    
    # Step 3: Verify incomplete task is hidden
    step("Verify that incomplete tasks are hidden")
    expect(loaded_page.get_by_text("Find cat")).not_to_be_visible()
    
    # Step 4: Verify "No Todos" message appears
    step("Verify that 'No Todos' message appears when no completed tasks exist")
    no_todos_message = loaded_page.get_by_text("No Todos")
    expect(no_todos_message).to_be_visible()
    
    dbg("Filter functionality working correctly, added task is hidden" +
    " and 'No Todos' message is displayed when filtering by completed status.")