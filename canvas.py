import tkinter as tk

class GridExample(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        
        # Create a 3x3 grid
        for i in range(3):
            for j in range(3):
                label = tk.Label(self, text=f"Row {i+1}, Col {j+1}", padx=20, pady=10, relief=tk.SOLID, borderwidth=1)
                label.grid(row=i, column=j, padx=5, pady=5)
    
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Grid Example with Borders")
    
    # Create the GridExample widget
    grid_example = GridExample(root)
    grid_example.pack(padx=20, pady=20)
    
    root.mainloop()