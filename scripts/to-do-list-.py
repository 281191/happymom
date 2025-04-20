// Simple Todo List Manager

class TodoList {
  constructor() {
    this.todos = []; // Initialize empty array to store todos
  }

  addTodo(task) {
    this.todos.push({ task, completed: false }); // Add new task as incomplete
    console.log(`Added: ${task}`); // Confirm addition
  }

  completeTodo(index) {
    if (index >= 0 && index < this.todos.length) { // Check valid index
      this.todos[index].completed = true; // Mark as complete
      console.log(`Completed: ${this.todos[index].task}`);
    }
  }

  listTodos() {
    console.log("Your Todos:"); // Header for the list
    this.todos.forEach((todo, i) => { // Loop through all todos
      console.log(`${i + 1}. [${todo.completed ? 'X' : ' '}] ${todo.task}`);
    });
  }
}

// Example usage
const myList = new TodoList();
myList.addTodo("Learn JavaScript");
myList.addTodo("Build a project");
myList.completeTodo(0);
myList.listTodos();
