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

    def toggle_exercises(selected_muscle):
        for muscle, lbl in labels.items():
            if muscle == selected_muscle:
                if lbl.winfo_viewable():
                    lbl.grid_remove()
                else:
                    lbl.grid()
            else:
                lbl.grid_remove()

    row_index = 0
    for muscle, exercises in exercise_data.items():
        btn = tk.Button(
            parent,
            text=muscle,
            font=("Arial", 14, "bold"),
            bg="#57a1f8",
            fg="white",
            padx=10,
            pady=5,
            bd=0,
            command=lambda m=muscle: toggle_exercises(m)
        )
        btn.grid(row=row_index, column=0, sticky="w", padx=20, pady=5)

        exercise_text = "\n".join(f"> {ex}" for ex in exercises)
        lbl = tk.Label(
            parent,
            text=exercise_text,
            justify="left",
            font=("Arial", 12),
            bg="white",
            fg="#333"
        )
        lbl.grid(row=row_index, column=1, sticky="w", padx=20, pady=5)
        lbl.grid_remove()

        labels[muscle] = lbl
        row_index += 1

    # Add spacing below last item so buttons don't overlap
    spacer = tk.Label(parent, text="", bg="white")
    spacer.grid(row=row_index, column=0, columnspan=2, pady=10)

    # Bottom button frame
    button_frame = tk.Frame(parent, bg="white")
    button_frame.grid(row=row_index+1, column=0, columnspan=2, pady=30)

    btn = tk.Button(
        button_frame,
        text="Exit",
        font=("Arial", 12, "bold"),
        bg="#dd0000",
        fg="white",
        padx=20,
        pady=5,
        command=parent.quit
    )
    btn.pack(side="left", padx=20)



# Run the main window
def open_main_window():
    root = tk.Tk()
    root.title("Gym Management")
    root.geometry("925x500+300+200")
    root.configure(bg="white")

    create_exercise_section(root)

    root.mainloop()