import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import math

def hitung():
    try:
        g_str = combo_g.get().strip()
        x0_str = entry_x0.get().strip()
        tol_str = entry_tol.get().strip()
        max_iter_str = entry_iter.get().strip()

        # Validasi jika ada form yang kosong
        if not g_str or not x0_str or not tol_str or not max_iter_str:
            raise ValueError("Semua parameter input wajib diisi terlebih dahulu!")

        x0 = float(x0_str)
        tol = float(tol_str)
        max_iter = int(max_iter_str)

        # Bersihkan tabel sebelumnya
         for row in tree.get_children():
            tree.delete(row)

        # Proses Metode Iterasi Titik Tetap (x_baru = g(x))
        x_sekarang = x0
        riwayat_x = [x0]

        for i in range(1, max_iter + 1):
            x_baru = eval(g_str, {"x": x_sekarang, "math": math, "sqrt": math.sqrt, "sin": math.sin, "cos": math.cos, "exp": math.exp})
            error = abs(x_baru - x_sekarang)
            
            tag = 'even' if i % 2 == 0 else 'odd'
            tree.insert("", "end", values=(i, f"{x_sekarang:.6f}", f"{x_baru:.6f}", f"{error:.6e}"), tags=(tag,))
            riwayat_x.append(x_baru)
            
            if error < tol:
                lbl_status.config(text=f"✨ Sukses! Akar ditemukan: {x_baru:.6f} (Iterasi ke-{i})", fg="#047857")
                buat_grafik(g_str, riwayat_x, x_baru)
                return
            
            x_sekarang = x_baru

        lbl_status.config(text=f"⚠️ Maksimum iterasi tercapai. Akar terakhir: {x_sekarang:.6f}", fg="#b45309")
        buat_grafik(g_str, riwayat_x, x_sekarang)

    except Exception as e:
        messagebox.showerror("Error", f"Terjadi kesalahan input atau rumus:\n{e}")

def reset_form():
    combo_g.set("")
    entry_x0.delete(0, tk.END)
    entry_tol.delete(0, tk.END)
    entry_iter.delete(0, tk.END)
for row in tree.get_children():
        tree.delete(row)
    lbl_status.config(text="Status: Silakan isi parameter di atas dan klik 'Hitung Akar'", fg="#1e3a8a")
    ax.clear()
    ax.set_facecolor('#ffffff')
    ax.set_title("Grafik Konvergensi Metode Iterasi", fontsize=10, fontweight="bold", color="#1e3a8a")
    ax.grid(True, linestyle=":", alpha=0.5)
    canvas.draw()

def buat_grafik(g_str, riwayat, akar):
    ax.clear()
    
