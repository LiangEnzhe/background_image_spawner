import datetime, time, keyboard, os, winsound, gc, subprocess, secrets
from tkinter import Tk, Label
from PIL import Image, ImageTk
from playsound import playsound

def play_audio(action):
    playsound(os.path.join(os.getcwd(),"aud", f"{action}.wav"))
    match secrets.randbelow(10):
        case 1:
            playsound(os.path.join(os.getcwd(),"aud", "A.wav"))
        case 2:
            playsound(os.path.join(os.getcwd(),"aud", "laggy_A.wav"))

def show_image():
    root = Tk()
    root.overrideredirect(True)
    num = secrets.randbelow(5) + 1
    image_path = os.path.join(os.getcwd(), "img", f"{num}.png")
    original_image = Image.open(image_path)

    max_width, max_height = 800, 600
    scale_factor = min(max_width / original_image.width, max_height / original_image.height)
    new_size = (int(original_image.width * scale_factor), int(original_image.height * scale_factor))
    resized_image = original_image.resize(new_size, Image.Resampling.LANCZOS)

    tk_image = ImageTk.PhotoImage(resized_image)
    label = Label(root, image=tk_image)
    label.pack()

    def start_drag(event): root.x, root.y = event.x, event.y
    def move_window(event): root.geometry(f"+{event.x_root - root.x}+{event.y_root - root.y}")
    label.bind("<Button-1>", start_drag)
    label.bind("<B1-Motion>", move_window)

    label.bind("<Button-3>", lambda e: root.destroy())

    root.update_idletasks()
    screen_width, screen_height = root.winfo_screenwidth(), root.winfo_screenheight()
    x, y = (screen_width - new_size[0]) // 2, (screen_height - new_size[1]) // 2
    root.geometry(f"{new_size[0]}x{new_size[1]}+{x}+{y}")

    root.attributes("-topmost", True)
    label.image = tk_image
    root.mainloop()        

def show_christ():
    root = Tk()
    root.overrideredirect(True)
    num = secrets.randbelow(8) + 1
    image_path = os.path.join(os.getcwd(), "img", "jc", f"{num}.png")
    original_image = Image.open(image_path)

    max_width, max_height = 800, 600
    scale_factor = min(max_width / original_image.width, max_height / original_image.height)
    new_size = (int(original_image.width * scale_factor), int(original_image.height * scale_factor))
    resized_image = original_image.resize(new_size, Image.Resampling.LANCZOS)

    tk_image = ImageTk.PhotoImage(resized_image)
    label = Label(root, image=tk_image)
    label.pack()

    def start_drag(event): root.x, root.y = event.x, event.y
    def move_window(event): root.geometry(f"+{event.x_root - root.x}+{event.y_root - root.y}")
    label.bind("<Button-1>", start_drag)
    label.bind("<B1-Motion>", move_window)

    label.bind("<Button-3>", lambda e: root.destroy())

    root.update_idletasks()
    screen_width, screen_height = root.winfo_screenwidth(), root.winfo_screenheight()
    x, y = (screen_width - new_size[0]) // 2, (screen_height - new_size[1]) // 2
    root.geometry(f"{new_size[0]}x{new_size[1]}+{x}+{y}")

    root.attributes("-topmost", True)
    label.image = tk_image
    root.mainloop() 

def play_video():
    num = secrets.randbelow(22) + 1 
    subprocess.Popen([
        r"C:\Program Files (x86)\VideoLAN\VLC\vlc.exe",
        os.path.join(os.getcwd(),"vid", f"{num}.mp4"),
        "--play-and-exit"])
    time.sleep(120)
    match secrets.randbelow(10):
        case 1:
            show_image()
        case 2:
            show_christ()

def check_time():
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M")
    current_day = now.strftime("%A")  
    match (current_day, current_time):
        case (_, "18:00"):
            action = "hour"
        case (_, "19:00"):
            action = "interview"        
        case (_, "20:00"):
            action = "school"
        case (_, "22:00"):
            action = "call"
        case (_, "22:50"):
            action = "shower"
        case (_, "23:00"):
            action = "zapis"
        case (_, "23:30"):
            action = "sleep"
        case _:
            return
    winsound.Beep(1000, 1500)
    play_audio(action)

def main():
    keyboard.add_hotkey("ctrl+alt+i", play_video)
    while True:
        check_time()
        time.sleep(60)

if __name__ == "__main__":
    main()
