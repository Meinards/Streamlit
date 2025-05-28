import streamlit as st
import matplotlib.pyplot as plt
import datetime
import math

def biorhythm(days, cycle):
    return math.sin(2 * math.pi * days / cycle)

st.title("🧠🫀💪 Bioritmu kalkulators")

birth_date = st.date_input("Dzimšanas datums")
target_date = st.date_input("Mērķa datums", datetime.date.today())

if birth_date and target_date:
    day_diff = (target_date - birth_date).days
    phys = biorhythm(day_diff, 23)
    emot = biorhythm(day_diff, 28)
    intel = biorhythm(day_diff, 33)

    st.subheader("Rezultāti")
    st.write(f"Fiziskais: {phys:.2f}")
    st.write(f"Emocionālais: {emot:.2f}")
    st.write(f"Intelektuālais: {intel:.2f}")

    days_range = range(-15, 16)
    dates = [target_date + datetime.timedelta(days=i) for i in days_range]
    phys_vals = [biorhythm(day_diff + i, 23) for i in days_range]
    emot_vals = [biorhythm(day_diff + i, 28) for i in days_range]
    intel_vals = [biorhythm(day_diff + i, 33) for i in days_range]
    total_vals = [p + e + i for p, e, i in zip(phys_vals, emot_vals, intel_vals)]

    best_index = total_vals.index(max(total_vals))
    best_day = dates[best_index]

    st.write(f"Labākā diena: {best_day} (Summārais bioritms: {total_vals[best_index]:.2f})")

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(dates, phys_vals, label='Fiziskais', color='red')
    ax.plot(dates, emot_vals, label='Emocionālais', color='blue')
    ax.plot(dates, intel_vals, label='Intelektuālais', color='green')
    ax.plot(dates, total_vals, label='Kopējais', color='purple', linestyle='--')
    ax.axhline(0, color='black', linestyle='--')
    ax.axvline(target_date, color='gray', linestyle=':', label='Mērķa diena')
    ax.axvline(best_day, color='gold', linestyle=':', label='Labākā diena')
    ax.set_title("Bioritmu grafiks")
    ax.legend()
    ax.grid(True)
    fig.autofmt_xdate()

    st.pyplot(fig)
