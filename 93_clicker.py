import pyautogui
import random
import math
import time
import tkinter as tk
from tkinter import simpledialog

class ClickerApp:
    def __init__(self, root, clicks, interval):
        self.root = root
        self.clicks = clicks
        self.interval = interval
        self.root.attributes("-fullscreen", True)
        self.root.attributes("-alpha", 0.3)
        self.root.configure(bg='white')
        self.canvas = tk.Canvas(root, width=root.winfo_screenwidth(), height=root.winfo_screenheight(), highlightthickness=0)
        self.canvas.pack()

        self.center_x = root.winfo_screenwidth() // 2
        self.center_y = root.winfo_screenheight() // 2
        self.radius = 100

        self.circle = self.canvas.create_oval(self.center_x - self.radius, self.center_y - self.radius, self.center_x + self.radius, self.center_y + self.radius, outline="red", width=2)
        self.drag_data = {"x": 0, "y": 0}

        self.canvas.tag_bind(self.circle, "<ButtonPress-1>", self.on_circle_press)
        self.canvas.tag_bind(self.circle, "<ButtonRelease-1>", self.on_circle_release)
        self.canvas.tag_bind(self.circle, "<B1-Motion>", self.on_circle_motion)

        self.root.bind("<space>", self.start_clicking)
        self.root.bind("<q>", self.exit_app)

    def on_circle_press(self, event):
        self.drag_data["x"] = event.x
        self.drag_data["y"] = event.y

    def on_circle_release(self, event):
        self.drag_data["x"] = 0
        self.drag_data["y"] = 0

    def on_circle_motion(self, event):
        delta_x = event.x - self.drag_data["x"]
        delta_y = event.y - self.drag_data["y"]
        self.canvas.move(self.circle, delta_x, delta_y)
        self.drag_data["x"] = event.x
        self.drag_data["y"] = event.y
        self.center_x += delta_x
        self.center_y += delta_y

    def random_point_in_circle(self):
        angle = random.uniform(0, 2 * math.pi)
        r = self.radius * math.sqrt(random.uniform(0, 1))
        x = int(self.center_x + r * math.cos(angle))
        y = int(self.center_y + r * math.sin(angle))
        return x, y

    def click_in_circle(self, clicks, interval):
        for _ in range(clicks):
            x, y = self.random_point_in_circle()
            pyautogui.click(x, y)
            time.sleep(1/interval)

    def start_clicking(self, event):
        self.root.destroy()
        self.click_in_circle(self.clicks, self.interval)

    def exit_app(self, event):
        self.root.destroy()

def get_user_input():
    input_root = tk.Tk()
    input_root.withdraw()

    clicks = simpledialog.askinteger("Input", "tedad click ha ra mosha khas konid", minvalue=1, maxvalue=10000)
    interval = simpledialog.askfloat("Input", "sorat click ha ra moshakhas konid (bar sania)", minvalue=0.01, maxvalue=100.0)

    input_root.destroy()
    return clicks, interval

if __name__ == "__main__":
    clicks, interval = get_user_input()
    
    root = tk.Tk()
    app = ClickerApp(root, clicks, interval)
    root.mainloop()