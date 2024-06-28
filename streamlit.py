import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import os

# File path to save CSV data
csv_file = 'time_entries.csv'

# Initialize session state for storing time entries
if 'times' not in st.session_state:
    st.session_state.times = []
if 'dates' not in st.session_state:
    st.session_state.dates = []

# Function to read CSV file
def read_csv():
    if os.path.exists(csv_file):
        df = pd.read_csv(csv_file, parse_dates=['Date'])
        return df
    return pd.DataFrame(columns=['Date', 'Time (hours)'])

# Function to write to CSV file
def write_csv(df):
    df.to_csv(csv_file, index=False)

# Read existing data
df = read_csv()

# Initialize session state with existing data
if len(df) > 0:
    st.session_state.dates = df['Date'].tolist()
    st.session_state.times = [datetime.time(int(t), int((t*60) % 60), int((t*3600) % 60)) for t in df['Time (hours)']]

st.title("Time Input Line Graph")

# Date input field
selected_date = st.date_input("Select Date", value=datetime.date.today())

# Input fields for time
hours = st.number_input("Hours", min_value=0, max_value=23, step=1, value=0)
minutes = st.number_input("Minutes", min_value=0, max_value=59, step=1, value=0)
seconds = st.number_input("Seconds", min_value=0, max_value=59, step=1, value=0)

# Button to add the input time and date to the list
if st.button("Add Time"):
    input_time = datetime.time(hour=hours, minute=minutes, second=seconds)
    st.session_state.times.append(input_time)
    st.session_state.dates.append(selected_date)
    
    # Convert times to fractional hours
    times_in_hours = [t.hour + t.minute / 60 + t.second / 3600 for t in st.session_state.times]
    
    # Update the DataFrame
    df = pd.DataFrame({
        "Date": st.session_state.dates,
        "Time (hours)": times_in_hours
    })
    
    # Write updated data to CSV
    write_csv(df)

# Convert times to fractional hours
times_in_hours = [t.hour + t.minute / 60 + t.second / 3600 for t in st.session_state.times]

# Convert data to a pandas DataFrame
df = pd.DataFrame({
    "Date": pd.to_datetime(st.session_state.dates),
    "Time (hours)": times_in_hours
})

st.write("### Time Entries")
st.write(df)

# Plot the line graph
if len(df) > 1:
    fig, ax = plt.subplots()
    ax.plot(df["Date"], df["Time (hours)"], marker='o')
    ax.set_xlabel("Date")
    ax.set_ylabel("Time (hours)")
    ax.set_title("Time Line Graph")
    
    # Set x-axis ticks to only the given dates
    ax.set_xticks(df["Date"])
    ax.set_xticklabels(df["Date"].dt.strftime("%Y-%m-%d"))  # Format dates as strings
    
    fig.autofmt_xdate()  # Format the x-axis dates for better readability
    st.pyplot(fig)
else:
    st.write("Add more time entries to see the line graph.")
