import tkinter as tk
from tkinter import messagebox

# إنشاء النافذة الرئيسية للانشر MAZEN Launcher
root = tk.Tk()
root.title("MAZEN Launcher - Java & Bedrock Edition")
root.geometry("600x400")
root.configure(bg="#1e1e2e")

# عنوان اللانشر
title_label = tk.Label(
    root, 
    text="Welcome to MAZEN Launcher", 
    font=("Arial", 20, "bold"), 
    fg="#cdd6f4", 
    bg="#1e1e2e"
)
title_label.pack(pady=30)

# وظائف أزرار التشغيل
def launch_java():
    messagebox.showinfo("MAZEN Launcher", "Launching Minecraft Java Edition...")

def launch_bedrock():
    messagebox.showinfo("MAZEN Launcher", "Launching Minecraft Bedrock Edition...")

# زرار تشغيل الجافا
btn_java = tk.Button(
    root, 
    text="Play Java Edition", 
    font=("Arial", 14), 
    bg="#a6e3a1", 
    fg="#11111b", 
    width=20, 
    command=launch_java
)
btn_java.pack(pady=10)

# زرار تشغيل البيدروك
btn_bedrock = tk.Button(
    root, 
    text="Play Bedrock Edition", 
    font=("Arial", 14), 
    bg="#89b4fa", 
    fg="#11111b", 
    width=20, 
    command=launch_bedrock
)
btn_bedrock.pack(pady=10)

root.mainloop()
