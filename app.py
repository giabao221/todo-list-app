# Danh sách để lưu các công việc
tasks.append({"name": task_name, "completed": False})
def add_task(task_name):
    """Thêm một công việc mới vào danh sách."""
    tasks.append(task_name)
    print(f"Đã thêm công việc: '{task_name}'")
# - -- Điểm bắt đầu của chương trình ---
if __name__ == "__main__":
    print("Chào mừng đến với ứng dụng To-Do List!")
    add_task("Học bài Git và GitHub")
    add_task("Làm bài tập thực hành ở nhà")
    list_tasks()
def list_tasks():
    """In ra tất cả các công việc hiện có."""
    if not tasks:
        print("Danh sách công việc đang trống.")
    else:
        print("Danh sách công việc:")
        for i, task in enumerate(tasks, start=1):
            status = "[x]" if task["completed"] else "[ ]"
            print(f"{i}. {status} {task['name']}")
def complete_task(task_index):
    """Đánh dấu một công việc là hoàn thành."""
    if 0 <= task_index < len(tasks):
        tasks[task_index]["completed"] = True
        print(f"✅ Đã hoàn thành: {tasks[task_index]['name']}")
    else:
        print("❌ Chỉ số công việc không hợp lệ.")