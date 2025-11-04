const taskList = document.getElementById("task-list");
const taskForm = document.getElementById("task-form");
const taskTitle = document.getElementById("task-title");

// ======== TASKBOARD ==========

// Загружает задачи
async function loadTasks() {
    const res = await fetch("/api/tasks/");
    const tasks = await res.json();
    taskList.innerHTML = "";
    tasks.forEach(t => renderTask(t));
}

function renderTask(task) {
    const li = document.createElement("li");
    li.innerHTML = `
        <input type="checkbox" ${task.completed ? "checked" : ""} onchange="toggleTask(${task.id}, this.checked)">
        <span>${task.title}</span>
        <button onclick="deleteTask(${task.id})">🗑</button>
    `;
    taskList.appendChild(li);
}

// Добавление задачи
taskForm.addEventListener("submit", async (e) => {
    e.preventDefault();
    const res = await fetch("/api/tasks/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ title: taskTitle.value })
    });
    const newTask = await res.json();
    renderTask(newTask);
    taskTitle.value = "";
});

async function toggleTask(id, completed) {
    await fetch(`/api/tasks/${id}/`, {
        method: "PATCH",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ completed })
    });
}

async function deleteTask(id) {
    await fetch(`/api/tasks/${id}/`, { method: "DELETE" });
    loadTasks();
}

loadTasks();

// ======== LOCAL STORAGE CLICK COUNTER ==========
let count = localStorage.getItem("clickCount") || 0;
document.getElementById("clicks").textContent = count;

document.getElementById("click-btn").addEventListener("click", () => {
    count++;
    localStorage.setItem("clickCount", count);
    document.getElementById("clicks").textContent = count;
});

document.getElementById("reset-btn").addEventListener("click", () => {
    count = 0;
    localStorage.setItem("clickCount", 0);
    document.getElementById("clicks").textContent = 0;
});
