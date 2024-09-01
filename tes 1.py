import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import time

# Fungsi untuk membuat plot gelombang sinus
def plot_wave(amp, freq, phase, speed, duration):
    plt.ion()  # Mengaktifkan mode interaktif matplotlib
    fig, ax = plt.subplots()
    x = np.linspace(0, 10, 1000)
    for t in np.arange(0, duration, 0.1):
        y = amp * np.sin(2 * np.pi * freq * (x - speed * t) + phase)
        ax.clear()
        ax.plot(x, y)
        ax.set_ylim([-amp, amp])
        ax.set_xlim([0, 10])
        ax.set_title(f"t = {t:.2f} s")
        st.pyplot(fig)
        time.sleep(0.1)

# Input dari pengguna
st.title("Animasi Gelombang Sinus")
amp = st.slider("Amplitudo", 0.1, 5.0, 1.0)
freq = st.slider("Frekuensi", 0.1, 5.0, 1.0)
phase = st.slider("Fase", 0.0, 2 * np.pi, 0.0)
speed = st.slider("Kecepatan", 0.1, 5.0, 1.0)
duration = st.slider("Durasi (detik)", 1, 10, 5)

# Tombol untuk memulai animasi
if st.button("Mulai Animasi"):
    plot_wave(amp, freq, phase, speed, duration)
