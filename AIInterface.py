# AIInterface.py
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from model import Model
from visualization import plot_data, show_drawing_with_feedback

class AIInterface:
    def __init__(self, root):
        self.root = root
        self.root.title("AI Feedback Tool")  # Titel på fönstret
        self.model = Model()  # Initialisera modellen
        self.initialize_ui()  # Initialisera användargränssnittet

    def initialize_ui(self):
        # Initialisera UI-komponenter
        self.setup_canvas()  # Ställ in canvas för ritning
        self.setup_feedback_controls()  # Konfigurera feedbackkontroller
        self.setup_model_controls()  # Konfigurera kontroller för modell

    def setup_canvas(self):
        # Ställer in canvas för teckning
        self.canvas_frame = tk.Frame(self.root, borderwidth=2, relief="groove")
        self.canvas_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.canvas = tk.Canvas(self.canvas_frame, width=400, height=400, bg="white")
        self.canvas.pack(padx=10, pady=10)
        self.canvas.bind("<Button-1>", self.start_draw)
        self.canvas.bind("<B1-Motion>", self.continue_draw)
        ttk.Button(self.canvas_frame, text="Rensa", command=self.clear_canvas).pack(side=tk.BOTTOM, pady=5)

    def setup_feedback_controls(self):
        # Konfigurerar kontroller för feedback
        self.feedback_frame = tk.Frame(self.root, borderwidth=2, relief="groove")
        self.feedback_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        ttk.Label(self.feedback_frame, text="Är teckningen tillräckligt bra?").pack()
        for text, command in [("Ja", lambda: self.process_feedback(True)), ("Nej", lambda: self.process_feedback(False)), ("Avsluta", self.root.destroy)]:
            ttk.Button(self.feedback_frame, text=text, command=command).pack(side=tk.LEFT, padx=5, pady=5)

    def setup_model_controls(self):
        # Lägger till GUI-kontroller för att spara och ladda modellen
        ttk.Button(self.feedback_frame, text="Spara Modell", command=self.save_model).pack(fill=tk.X, padx=10, pady=2)
        ttk.Button(self.feedback_frame, text="Ladda Modell", command=self.load_model).pack(fill=tk.X, padx=10, pady=2)

    def process_feedback(self, feedback):
        # Hanterar feedback från användaren
        loss, accuracy = self.model.train_on_batch(self.current_drawing(), self.determine_label(feedback))
        print(f"Feedback mottagen: {'Positiv' if feedback else 'Negativ'}")
        self.show_training_progress()

    def save_model(self):
        # Implementera logiken för att spara modellen här
        filename = filedialog.asksaveasfilename(defaultextension=".model")
        if filename:
            self.model.save_model(filename)

    def load_model(self):
        # Implementera logiken för att ladda en modell här
        filename = filedialog.askopenfilename(filetypes=[("Model files", "*.model")])
        if filename:
            self.model.load_model(filename)

    def start_draw(self, event):
        # Startar en ny teckning
        self.last_x, self.last_y = event.x, event.y

    def continue_draw(self, event):
        # Fortsätter teckna baserat på musrörelse
        self.canvas.create_line(self.last_x, self.last_y, event.x, event.y, width=2, fill="black")
        self.last_x, self.last_y = event.x, event.y

    def clear_canvas(self):
        # Rensar canvas
        self.canvas.delete("all")

    def show_training_progress(self):
        # Hämta förlust och noggrannhet från modellen och visa träningsframsteg
        loss_history, accuracy_history = self.model.get_training_history()
        plot_data(loss_history, accuracy_history, title='Träningsframsteg')

    def current_drawing(self):
        # Implementera logik för att hämta den nuvarande ritningen från canvas
        return None  # Ersätt med riktig logik

    def determine_label(self, feedback):
        # Implementera logik för att bestämma etiketten baserat på feedback
        return None  # Ersätt med riktig logik

    def display_generated_drawing(self):
        # Generera en bild med modellen och visa den
        drawing = self.model.generate_drawing()
        show_drawing_with_feedback(drawing)

if __name__ == "__main__":
    root = tk.Tk()
    app = AIInterface(root)
    root.mainloop()


