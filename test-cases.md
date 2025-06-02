
# Test Cases - Consafe QA role. 

---

# Test Case 1: Add a new task (Button click)

**Objective**: Verify the user can add a new task.

**Approval Criteria**:
- The input field accepts text.
- Pressing the 'Add Task' button adds the task to the list.
- The task appears in the task list with the chosen label.

**Limitations**:
- Requires the todo-app page to be loaded before the test begins.
- This test does not validate submitting tasks via the Enter key: only button clicks are covered.

**Steps**:
1. Press the button 'Add Task'.
2. Enter 'Buy milk' as a title in the input field.
3. Press the button 'Add Task' in the pop-up window.
4. Verify that the task was added successfully.

**Validation**:
- The new task appears in the task list with the text "Buy milk".

---

### Test Case 2: Update status of a task

**Objective**: Verify the user can mark a task as completed and unmark it.

**Approval Criteria**:
- Completed task appears with CSS - text-decoration-line: line-through
- Completed task has checkbox with opacity 1
- Unmarked task returns to normal text without line-through
- Unmarked task has checkbox with opacity 0

**Limitations**:
- Requires the todo-app page to be loaded before the test begins.
- Requires at least one already existing task.

**Steps**:
1. Add a new task.
2. Click the task's checkbox.
3. Verify the task is marked as completed and has opacity 1.
4. Click the checkbox again to unmark the task
5. Verify the task is not marked and has opacity 0.

**Validation**:
- The task appears with strikethrough styling when completed and has opacity 1.
- The task is restored to normal text when unchecked and has opacity 0.

---

### Test Case 3: Delete a task

**Objective**: Verify the user can delete an existing task.

**Approval Criteria**:
- The delete button (trash icon) is clickable.
- Clicking the delete button removes the task from the list.
- The task no longer appears in the task list after deletion.

**Limitations**:
- Requries todo-app page to be loaded.
- Requires one existing task.

**Steps**:
1. Add a new task 'Sell Guitar'.
2. Click the trash icon to delete the task.
3. Verify that the task was deleted successfully.

**Validation**:
- The task is removed from the list.

---

### Test Case 4: Filter tasks by status (Completed)

**Objective**: Verify the user can filter tasks by status "completed".

**Approval Criteria**:
- The filter dropdown accepts status selection.
- Filtering by 'completed' when no completed tasks exist shows "No Todos".
- The filter functionality works correctly to hide/show appropriate tasks.

**Limitations**:
- Requries todo-app page to be loaded.
- Requires at least two tasks (one completed, one active).

**Steps**:
1. Add a new task.
2. Select 'completed' filter from the status dropdown.
3. Verify that incomplete tasks are hidden.
4. Verify that "No Todos" message appears when no completed tasks exist.

**Validation**:
- Filtering by status "completed" shows "No Todos" if uncompleted task is added.

---

### Test Case 5: Tasks persist on reload (LocalStorage)

**Objective**: Verify tasks are saved in LocalStorage and persist after page reload.

**Approval Criteria**:
- Task remains after reload.

**Limitations**:
- Requries todo-app page to be loaded.
- Only one task added.
- Browser must support LocalStorage.

**Steps**:
1. Add a task named "Feed the cat".
2. Reload the page.

**Validation**:
- "Feed the cat" is still visible in the task list.

