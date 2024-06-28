# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt

# st.title("ChronoGraph")

# # File uploader to allow the user to upload a CSV file
# uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

# if uploaded_file is not None:
#     # Read the uploaded CSV file
#     df = pd.read_csv(uploaded_file, parse_dates=['Date'])

#     # Check if the necessary columns are present in the CSV file
#     if 'Date' in df.columns and 'Time (hours)' in df.columns:
#         st.write("### Time Entries")
#         st.write(df)

#         # Plot the line graph
#         if len(df) > 1:
#             fig, ax = plt.subplots()
#             ax.plot(df["Date"], df["Time (hours)"], marker='o')
#             ax.set_xlabel("Date")
#             ax.set_ylabel("Time (hours)")
#             ax.set_title("Time Line Graph")
            
#             # Set x-axis ticks to only the given dates
#             ax.set_xticks(df["Date"])
#             ax.set_xticklabels(df["Date"].dt.strftime("%Y-%m-%d"))  # Format dates as strings
            
#             fig.autofmt_xdate()  # Format the x-axis dates for better readability
#             st.pyplot(fig)
#         else:
#             st.write("The CSV file must contain more than one entry to plot the graph.")
#     else:
#         st.write("The CSV file must contain 'Date' and 'Time (hours)' columns.")
# else:
#     st.write("Please upload a CSV file.")

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image

# Set the Streamlit layout to wide mode
st.set_page_config(layout="wide")

# Set a title and a subheader
st.title("ChronoGraph")
st.subheader("Visualize Your Time Data Easily")

# Sidebar for instructions and logo
st.sidebar.title("Instructions")
st.sidebar.info(
    """
    1. Upload a CSV file containing your time data.
    2. Ensure the file has 'Date' and 'Time (hours)' columns.
    3. View the table and the line graph.
    """
)

# Optionally, you can add a logo to the sidebar
# logo = Image.open("path/to/your/logo.png")
# st.sidebar.image(logo, use_column_width=True)

# File uploader to allow the user to upload a CSV file
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # Read the uploaded CSV file
    df = pd.read_csv(uploaded_file, parse_dates=['Date'])

    # Check if the necessary columns are present in the CSV file
    if 'Date' in df.columns and 'Time (hours)' in df.columns:
        st.write("### Time Entries")
        st.dataframe(df, width=1000, height=300)  # Enhanced display of the DataFrame

        # Plot the line graph
        if len(df) > 1:
            # Set Seaborn style for better aesthetics
            sns.set(style="whitegrid")

            fig, ax = plt.subplots(figsize=(12, 6))
            sns.lineplot(x="Date", y="Time (hours)", data=df, marker='o', ax=ax)
            ax.set_xlabel("Date", fontsize=14)
            ax.set_ylabel("Time (hours)", fontsize=14)
            ax.set_title("Time Line Graph", fontsize=16)
            
            # Set x-axis ticks to only the given dates
            ax.set_xticks(df["Date"])
            ax.set_xticklabels(df["Date"].dt.strftime("%Y-%m-%d"), rotation=45, ha='right')  # Format dates as strings
            
            # Adjust layout for better readability
            fig.tight_layout()
            st.pyplot(fig)
        else:
            st.write("The CSV file must contain more than one entry to plot the graph.")
    else:
        st.write("The CSV file must contain 'Date' and 'Time (hours)' columns.")
else:
    st.write("Please upload a CSV file.")
