function addTask(){
	var taskInput = document.getElementById("taskInput");
    var taskText = taskInput.value.trim();

    if (taskText !== "") {
        var taskList = document.getElementById("taskList");
        var newTaskItem = document.createElement("li");
        
        newTaskItem.classList.add("taskItem");
        newTaskItem.innerHTML = taskText + '<span class="deleteButton" onclick="deleteTask(this)">❌</span>';
        taskList.appendChild(newTaskItem);
        taskInput.value = "";
    }
}

function deleteTask(taskElement) {
    	var taskList = document.getElementById("taskList");
    	taskList.removeChild(taskElement.parentNode);
    }