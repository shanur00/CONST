import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import sqlite3
from sqlalchemy import create_engine

# Initialize session state for storing user input
if 'user' not in st.session_state:
    st.session_state.user = ""

# Database setup
def init_db():
    conn = sqlite3.connect('time_entries.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS time_entries (
            user TEXT,
            date TEXT,
            time_hours REAL
        )
    ''')
    conn.commit()
    conn.close()

def add_entry(user, date, time_hours):
    conn = sqlite3.connect('time_entries.db')
    c = conn.cursor()
    c.execute('INSERT INTO time_entries (user, date, time_hours) VALUES (?, ?, ?)', (user, date, time_hours))
    conn.commit()
    conn.close()

def get_entries(user):
    conn = sqlite3.connect('time_entries.db')
    df = pd.read_sql_query('SELECT date, time_hours FROM time_entries WHERE user = ?', conn, params=(user,))
    conn.close()
    return df

init_db()

st.title("Time Input Line Graph")

# User input
st.session_state.user = st.text_input("Enter your username", st.session_state.user)

if st.session_state.user:
    # Date input field
    selected_date = st.date_input("Select Date", value=datetime.date.today())
    
    # Input fields for time
    hours = st.number_input("Hours", min_value=0, max_value=23, step=1, value=0)
    minutes = st.number_input("Minutes", min_value=0, max_value=59, step=1, value=0)
    seconds = st.number_input("Seconds", min_value=0, max_value=59, step=1, value=0)
    
    # Button to add the input time and date to the list
    if st.button("Add Time"):
        time_in_hours = hours + minutes / 60 + seconds / 3600
        add_entry(st.session_state.user, selected_date.strftime('%Y-%m-%d'), time_in_hours)
    
    # Retrieve and display entries
    df = get_entries(st.session_state.user)
    
    st.write("### Time Entries")
    st.write(df)
    
    # Plot the line graph
    if len(df) > 1:
        fig, ax = plt.subplots()
        ax.plot(df["date"], df["time_hours"], marker='o')
        ax.set_xlabel("Date")
        ax.set_ylabel("Time (hours)")
        ax.set_title("Time Line Graph")
        
        # Set x-axis ticks to only the given dates
        ax.set_xticks(pd.to_datetime(df["date"]))
        ax.set_xticklabels(pd.to_datetime(df["date"]).strftime("%Y-%m-%d"))  # Format dates as strings
        
        fig.autofmt_xdate()  # Format the x-axis dates for better readability
        st.pyplot(fig)
    else:
        st.write("Add more time entries to see the line graph.")
else:
    st.write("Please enter a username to start.")
