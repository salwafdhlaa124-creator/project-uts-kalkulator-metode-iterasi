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
                lbl_status.config(text=f"Sukses! Akar ditemukan: {x_baru:.6f} (Iterasi ke-{i})", fg="#047857")
                buat_grafik(g_str, riwayat_x, x_baru)
                return
            
            x_sekarang = x_baru

        lbl_status.config(text=f"Maksimum iterasi tercapai. Akar terakhir: {x_sekarang:.6f}", fg="#b45309")
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
    xmin = min(riwayat) - 1
    xmax = max(riwayat) + 1
    
    xs = [xmin + i * (xmax - xmin) / 100 for i in range(101)]
    try:
        ys = [eval(g_str, {"x": x, "math": math, "sqrt": math.sqrt, "sin": math.sin, "cos": math.cos, "exp": math.exp}) for x in xs]
    except:
        ys = xs

    ax.plot(xs, ys, label="y = g(x)", color="#2563eb", linewidth=2.2)
ax.plot(xs, xs, label="y = x", color="#ef4444", linestyle="--", linewidth=1.5)
    ax.plot(akar, akar, 'go', markersize=9, label=f"Akar ({akar:.4f})")
    
    ax.set_title("Grafik Konvergensi Metode Iterasi", fontsize=10, fontweight="bold", color="#1e3a8a")
    ax.set_xlabel("Nilai x", fontsize=9)
    ax.set_ylabel("Nilai y", fontsize=9)
    ax.legend(loc="upper left", frameon=True, facecolor="#f0fdf4")
    ax.grid(True, linestyle=":", alpha=0.6)
    canvas.draw()

# ==================== TAMPILAN GUI TKINTER BERWARNA ====================
root = tk.Tk()
root.title("Kalkulator Metode Iterasi Titik Tetap - Komnum C")
root.geometry("1150x700")
root.configure(bg="#bae6fd")  # Latar belakang utama biru cerah (tidak polos)

# Header Atas (Simpel & Elegan dengan warna Navy/Biru Tua)
header_frame = tk.Frame(root, bg="#1e3a8a", pady=10)
header_frame.pack(fill=tk.X)
tk.Label(header_frame, text="Kalkulator Metode Iterasi Titik Tetap", font=("Segoe UI", 14, "bold"), bg="#1e3a8a", fg="#fef08a").pack()

# Layout Utama
main_layout = tk.Frame(root, bg="#bae6fd")
main_layout.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)

# Kolom Kiri (Input & Tabel)
left_col = tk.Frame(main_layout, bg="#bae6fd")
left_col.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))

# Card Input Parameter (Nuansa Soft Blue/Cyan yang cerah)
input_card = tk.LabelFrame(left_col, text=" ⚙️ Parameter Input ", font=("Segoe UI", 10, "bold"), bg="#e0f2fe", fg="#1e3a8a", padx=15, pady=12, bd=2, relief="groove")
input_card.pack(fill=tk.X, pady=(0, 10))

tk.Label(input_card, text="Persamaan g(x):", bg="#e0f2fe", fg="#1e293b", font=("Segoe UI", 9, "bold")).grid(row=0, column=0, sticky="w", pady=6)

opsi_persamaan = [
    "math.sqrt(2 + x)",
    "math.exp(-x)",
    "math.cos(x)",
    "(x + 2/x) / 2"
]
combo_g = ttk.Combobox(input_card, values=opsi_persamaan, width=26, font=("Segoe UI", 10))
combo_g.grid(row=0, column=1, pady=6, padx=10)
combo_g.set("") # Dikosongkan agar user pilih sendiri

tk.Label(input_card, text="Tebakan Awal (x0):", bg="#e0f2fe", fg="#1e293b", font=("Segoe UI", 9, "bold")).grid(row=1, column=0, sticky="w", pady=6)
entry_x0 = tk.Entry(input_card, width=28, font=("Segoe UI", 10), relief="solid", bd=1)
entry_x0.grid(row=1, column=1, pady=6, padx=10) # Kosong

tk.Label(input_card, text="Toleransi Error:", bg="#e0f2fe", fg="#1e293b", font=("Segoe UI", 9, "bold")).grid(row=2, column=0, sticky="w", pady=6)
