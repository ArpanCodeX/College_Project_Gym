import tkinter as tk
def create_exercise_section(parent):
    exercise_data = {
        "Biceps": ["Barbell Curl", "Dumbbell Curl", "Hammer Curl"],
        "Triceps": ["Tricep Dips", "Overhead Extension", "Tricep Pushdown"],
        "Chest": ["Bench Press", "Push-ups", "Chest Fly"],
        "Shoulder": ["Shoulder Press", "Lateral Raise", "Front Raise"],
        "Back": ["Pull-ups", "Deadlift", "Bent-over Row"],
        "Leg": ["Squats", "Lunges", "High Knees", "Jumping Jacks", "Crawling"],
        "Cardio": ["Running", "Cycling", "Jump Rope"],
        "Abs": ["Crunches", "Planks", "Leg Raises"]
    }

    labels = {}
    row_index = 0

    for muscle, exercises in exercise_data.items():
        btn = tk.Button(parent, text=muscle, font=("Arial", 14, "bold"),
                     bg="#57a1f8", fg="white", padx=10, pady=5, bd=0,
                     command=lambda m=muscle: toggle_exercises(m))
        btn.grid(row=row_index, column=0, sticky="w", padx=20, pady=10)

        lbl = tk.Label(parent, text="\n".join(exercises), justify="left",
                    font=("Arial", 12), bg="white", fg="#333")
        lbl.grid(row=row_index, column=1, sticky="w", padx=20, pady=10)
        lbl.grid_remove()

        labels[muscle] = lbl
        row_index += 1

    def toggle_exercises(muscle):
        lbl = labels[muscle]
        if lbl.winfo_viewable():
            lbl.grid_remove()
        else:
            lbl.grid()
def open_main_window():
    root = tk.Tk()
    root.title("Gym Management")

    create_exercise_section(root)

    root.mainloop()
open_main_window()

