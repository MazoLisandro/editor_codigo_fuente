import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import PhotoImage
import os

# Función para abrir archivos
def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Python Files", "*.py"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, 'r') as file:
            text_area.delete(1.0, tk.END)  # Borrar contenido actual
            text_area.insert(tk.END, file.read())  # Cargar el contenido del archivo
            update_status(f"Archivo abierto: {file_path}")

# Función para cargar el icono si está disponible
def cargar_icono():
    if os.path.exists("open_icon.png"):  # Verifica si el archivo existe
        return tk.PhotoImage(file="open_icon.png")
    else:
        print("El archivo 'open_icon.png' no se encuentra. Se usará la versión sin icono.")
        return None  # No cargar la imagen si no está disponible

# Crear la ventana principal
root = tk.Tk()
root.title("Editor de Código Moderno")
root.geometry("800x600")

# Establecer el color de fondo de la ventana
root.config(bg="#f4f4f9")

# Establecer el estilo para ttk
style = ttk.Style()
style.configure("Modern.TFrame", background="#f4f4f9")
style.configure("Modern.TButton", background="#4CAF50", foreground="white", font=("Helvetica", 12))
style.configure("Modern.TLabel", background="#f4f4f9", font=("Helvetica", 14))

# Crear un marco dentro de la ventana
frame = ttk.Frame(root, padding="10 10 10 10", style="Modern.TFrame")
frame.pack(fill=tk.BOTH, expand=True)

# Etiqueta de bienvenida
label = ttk.Label(frame, text="Editor de Código", style="Modern.TLabel")
label.pack(pady=20)

# Panel dividido (PanedWindow)
paned_window = ttk.PanedWindow(frame, orient=tk.HORIZONTAL)
paned_window.pack(fill=tk.BOTH, expand=True)

# Panel izquierdo: área de texto
text_area = tk.Text(paned_window, wrap=tk.WORD, font=("Courier New", 12), bg="#2e2e2e", fg="white", insertbackground='white')
paned_window.add(text_area)

# Panel derecho: botón para abrir archivo
right_panel = ttk.Frame(paned_window)

# Intentar cargar el icono si está disponible
open_icon = cargar_icono()

# Crear el botón de abrir archivo
if open_icon:
    open_button = ttk.Button(right_panel, text="Abrir Archivo", image=open_icon, compound="left", style="Modern.TButton", command=open_file)
else:
    open_button = ttk.Button(right_panel, text="Abrir Archivo", style="Modern.TButton", command=open_file)

open_button.pack(pady=10)
paned_window.add(right_panel)

# Menú superior
menu_bar = tk.Menu(root)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Abrir", command=open_file)
file_menu.add_command(label="Salir", command=root.quit)
menu_bar.add_cascade(label="Archivo", menu=file_menu)
root.config(menu=menu_bar)

# Barra de estado en la parte inferior
status_bar = ttk.Label(root, text="Listo", relief=tk.SUNKEN, anchor=tk.W, font=("Helvetica", 10), background="#f4f4f9")
status_bar.pack(side=tk.BOTTOM, fill=tk.X)

# Función para actualizar la barra de estado
def update_status(text):
    status_bar.config(text=text)

# Iniciar la aplicación
root.mainloop()
