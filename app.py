import streamlit as st
import math
from drainage import calculate_peak_runoff, calculate_pipe_diameter

st.set_page_config(page_title="Pune Drainage Calculator", layout="centered")
st.title("Pune Storm Drainage Calculator")

c = st.number_input("Runoff Coefficient (c)", value=0.85)
i = st.number_input("Rainfall Intensity mm/hr (Pune)", value=50.0)
area = st.number_input("Catchment Area in Hectares", value=10.0)
n = st.number_input("Manning's n (0.013 for concrete)", value=0.013)
s = st.number_input("Slope of Pipe (m/m)", value=0.01)

if st.button("Calculate"):
    q_peak = calculate_peak_runoff(c, i, area)
    dia = calculate_pipe_diameter(q_peak, n, s)
    st.success(f"Peak Runoff (Q): {q_peak:.3f} m³/s")
    st.success(f"Required Pipe Diameter: {dia:.3f} m ({dia*1000:.0f} mm)")