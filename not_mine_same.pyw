import datetime, time, keyboard, os, winsound, subprocess, secrets, threading
from apscheduler.schedulers.background import BackgroundScheduler
from tkinter import Tk, Label
from PIL import Image, ImageTk
from playsound import playsound

class MediaPlayer:
    def __init__(self):
        self.scheduler = BackgroundScheduler()
        self.scheduler.start()
        self.setup_schedule()
        self.running = True

    def play_audio(self, action):
        def play():
            #playsound(os.path.join("aud", f"{action}.wav"))
            if secrets.randbelow(10) in {1, 2}:
                extra = "A.wav" if secrets.randbelow(2) else "laggy_A.wav"
                #playsound(os.path.join("aud", extra))
        threading.Thread(target=play, daemon=True).start()

    def play_shit(self):
        def play():
            winsound.Beep(1000, 1500)
            playsound(os.path.join("aud", "laggy_A.wav"))
        threading.Thread(target=play, daemon=True).start()

    def show_media(self, directory, count):
        def display():
            root = Tk()
            root.overrideredirect(True)
            num = secrets.randbelow(count) + 1
            path = os.path.join("img", directory, f"{num}.png")
            
            with Image.open(path) as img:
                max_size = (800, 600)
                img.thumbnail(max_size, Image.Resampling.LANCZOS)
                tk_image = ImageTk.PhotoImage(img)
                
                label = Label(root, image=tk_image)
                label.pack()
                
                label.bind("<Button-1>", lambda e: [setattr(root, 'x', e.x), setattr(root, 'y', e.y)])
                label.bind("<B1-Motion>", 
                            lambda e: root.geometry(f"+{e.x_root - root.x}+{e.y_root - root.y}"))
                label.bind("<Button-3>", lambda e: root.destroy())
                
                root.update_idletasks()
                w, h = img.size
                x = (root.winfo_screenwidth() - w) // 2
                y = (root.winfo_screenheight() - h) // 2
                root.geometry(f"{w}x{h}+{x}+{y}")
                root.attributes("-topmost", True)
                
                label.image = tk_image
                root.mainloop()

        threading.Thread(target=display, daemon=True).start()

    def play_video(self):
        def play():
            num = secrets.randbelow(27) + 1
            vid_path = os.path.join("vid", f"{num}.mp4")
            vlc_path = r"C:\Program Files (x86)\VideoLAN\VLC\vlc.exe"
            
            proc = subprocess.Popen([vlc_path, vid_path, "--play-and-exit"])
            proc.wait(timeout=120)
            
            if secrets.randbelow(10) == 1:
                self.show_media("", 10)
            elif secrets.randbelow(9) == 2:
                self.show_media("jc", 9)

        threading.Thread(target=play, daemon=True).start()

    def check_time(self):
        now = datetime.datetime.now()
        current = (now.strftime("%A"), now.strftime("%H:%M"))
        
        time_mapping = {
            **{(day, "18:00"): "hour" for day in [
                "Monday", "Tuesday", "Wednesday", 
                "Thursday", "Friday", "Saturday", "Sunday"
            ]},
            **{(day, "19:00"): "interview" for day in [
                "Monday", "Tuesday", "Wednesday",
                "Thursday", "Friday", "Saturday", "Sunday"
            ]},
            **{(day, "20:00"): "school" for day in [
                "Monday", "Tuesday", "Wednesday",
                "Thursday", "Friday", "Saturday", "Sunday"
            ]},
            **{(day, "22:00"): "call" for day in [
                "Monday", "Tuesday", "Wednesday",
                "Thursday", "Friday", "Saturday", "Sunday"
            ]},
            **{(day, "22:50"): "shower" for day in [
                "Monday", "Tuesday", "Wednesday",
                "Thursday", "Friday", "Saturday", "Sunday"
            ]},
            **{(day, "23:00"): "zapis" for day in [
                "Monday", "Tuesday", "Wednesday",
                "Thursday", "Friday", "Saturday", "Sunday"
            ]},
            **{(day, "23:30"): "sleep" for day in [
                "Monday", "Tuesday", "Wednesday",
                "Thursday", "Friday", "Saturday", "Sunday"
            ]}
        }
        
        if current in time_mapping:
            winsound.Beep(1000, 1500)
            self.play_audio(time_mapping[current])

    def setup_schedule(self):
        self.scheduler.add_job(
            self.check_time,
            'interval',
            minutes=1,
            next_run_time=datetime.datetime.now()
        )

    def run(self):
        keyboard.add_hotkey("ctrl+alt+i", self.play_video)
        keyboard.add_hotkey("ctrl+alt+o", self.play_shit)
        try:
            while self.running:
                time.sleep(1)
        except KeyboardInterrupt:
            self.shutdown()

    def shutdown(self):
        self.running = False
        self.scheduler.shutdown()
        keyboard.unhook_all_hotkeys()

if __name__ == "__main__":
    player = MediaPlayer()
    player.run()
