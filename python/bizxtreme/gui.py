"""Native Tkinter GUI for the BizXtreme Python runtime."""
from __future__ import annotations

import threading
import tkinter as tk
from tkinter import messagebox, scrolledtext, ttk

from .game_launcher import main as run_engine


class BizXtremeApp(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("BizXtreme — Python GUI")
        self.geometry("760x520")
        self.minsize(620, 420)
        self.mode = tk.StringVar(value="default")
        self.status = tk.StringVar(value="Ready")
        self._build()

    def _build(self) -> None:
        root = ttk.Frame(self, padding=16)
        root.pack(fill="both", expand=True)
        ttk.Label(root, text="BizXtreme", font=("TkDefaultFont", 22, "bold")).pack(anchor="w")
        ttk.Label(root, text="Python runtime control panel").pack(anchor="w", pady=(0, 12))
        controls = ttk.Frame(root)
        controls.pack(fill="x")
        ttk.Label(controls, text="Mode:").pack(side="left")
        ttk.Combobox(controls, textvariable=self.mode, values=("default", "tycoon"), state="readonly", width=16).pack(side="left", padx=8)
        self.start_btn = ttk.Button(controls, text="Start", command=self.start)
        self.start_btn.pack(side="left")
        ttk.Button(controls, text="Clear", command=self.clear).pack(side="left", padx=8)
        ttk.Label(root, textvariable=self.status).pack(anchor="w", pady=8)
        self.output = scrolledtext.ScrolledText(root, height=20, wrap="word", state="disabled")
        self.output.pack(fill="both", expand=True)

    def log(self, text: str) -> None:
        self.output.configure(state="normal")
        self.output.insert("end", text + "\n")
        self.output.see("end")
        self.output.configure(state="disabled")

    def clear(self) -> None:
        self.output.configure(state="normal")
        self.output.delete("1.0", "end")
        self.output.configure(state="disabled")

    def start(self) -> None:
        self.start_btn.configure(state="disabled")
        self.status.set("Running…")
        threading.Thread(target=self._worker, args=(self.mode.get(),), daemon=True).start()

    def _worker(self, mode: str) -> None:
        try:
            self.after(0, self.log, f"Starting BizXtreme ({mode})…")
            code = run_engine(mode)
            self.after(0, self.log, f"Completed with exit code {code}.")
            self.after(0, self.status.set, "Ready")
        except Exception as exc:
            self.after(0, self.log, f"ERROR: {exc}")
            self.after(0, self.status.set, "Error")
            self.after(0, messagebox.showerror, "BizXtreme error", str(exc))
        finally:
            self.after(0, self.start_btn.configure, {"state": "normal"})


def main() -> None:
    BizXtremeApp().mainloop()


if __name__ == "__main__":
    main()
