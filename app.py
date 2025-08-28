# app.py
import streamlit as st
import pandas as pd
import numpy as np
import time
from math import sqrt

st.set_page_config(page_title="AI Fall Detection", layout="wide")

st.title("🚨 AI Fall Detection System")

# Sidebar controls
st.sidebar.header("Controls")
simulate_fall = st.sidebar.button("Simulate Fall")
simulate_walk = st.sidebar.button("Simulate Normal Movement")

# Initialize status
status_placeholder = st.empty()
chart_placeholder = st.empty()

# Mock Data Generator
def generate_data(fall=False):
    data = []
    for _ in range(20):
        if fall:
            # big spikes for fall
            x = np.random.uniform(15, 25)
            y = np.random.uniform(15, 25)
            z = np.random.uniform(5, 15)
        else:
            # normal walking
            x = np.random.uniform(0, 1)
            y = np.random.uniform(0, 1)
            z = np.random.uniform(9, 10)
        data.append([x, y, z])
    return data

# Main Loop Simulation
if simulate_fall:
    mock_data = generate_data(fall=True)
elif simulate_walk:
    mock_data = generate_data(fall=False)
else:
    mock_data = generate_data(fall=False)

magnitudes = []

for x, y, z in mock_data:
    mag = sqrt(x**2 + y**2 + z**2)
    magnitudes.append(mag)
    
    # Update chart
    chart_placeholder.line_chart(magnitudes)
    
    # Update status
    if mag > 25:
        status_placeholder.error("🚨 Fall Detected! Alert Sent!")
    else:
        status_placeholder.success("✅ Normal Movement")
    
    time.sleep(0.2)



