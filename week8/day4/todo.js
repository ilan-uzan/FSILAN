const tasks = [];
let nextId = 0;

const form = document.getElementById('todoForm');
const input = document.getElementById('taskInput');
const listDiv = document.querySelector('.listTasks');

function renderTasks() {
  listDiv.innerHTML = '';
  tasks.forEach(task => {
    const taskDiv = document.createElement('div');
    taskDiv.className = 'task' + (task.done ? ' done' : '');
    taskDiv.setAttribute('data-task-id', task.task_id);

    // Delete button
    const delBtn = document.createElement('button');
    delBtn.className = 'delete-btn';
    delBtn.innerHTML = '<i class="fa-solid fa-xmark"></i>';
    delBtn.addEventListener('click', () => deleteTask(task.task_id));
    taskDiv.appendChild(delBtn);

    // Checkbox
    const checkbox = document.createElement('input');
    checkbox.type = 'checkbox';
    checkbox.checked = task.done;
    checkbox.addEventListener('change', () => doneTask(task.task_id, checkbox.checked));
    taskDiv.appendChild(checkbox);

    // Label
    const label = document.createElement('label');
    label.textContent = task.text;
    taskDiv.appendChild(label);

    listDiv.appendChild(taskDiv);
  });
}

function addTask(e) {
  e.preventDefault();
  const text = input.value.trim();
  if (!text) return;
  const task = { task_id: nextId++, text, done: false };
  tasks.push(task);
  input.value = '';
  renderTasks();
}

function doneTask(id, checked) {
  const task = tasks.find(t => t.task_id === id);
  if (task) {
    task.done = checked;
    renderTasks();
  }
}

function deleteTask(id) {
  const idx = tasks.findIndex(t => t.task_id === id);
  if (idx !== -1) {
    tasks.splice(idx, 1);
    renderTasks();
  }
}

form.addEventListener('submit', addTask);
renderTasks(); 