import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from io import BytesIO

# Set the Streamlit layout to wide mode
# st.set_page_config(layout="default")

# Function to plot graphs
def plot_graphs(df):
    if len(df) > 1:
        # Convert 'Date' column to string for proper plotting
        df['Date'] = df['Date'].dt.strftime('%Y-%m-%d')
        
        # Calculate the average time
        avg_time = df["Time (hours)"].mean()

        # Create figure and axes
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10), sharex=True)

        # Set background color for the axes
        ax1.set_facecolor('#faf4ed')
        ax2.set_facecolor('#faf4ed')

        # Plotting the bar chart using Seaborn
        sns.barplot(x="Date", y="Time (hours)", data=df, ax=ax1, color='#69b3a2', alpha=0.7)
        ax1.set_ylabel("Time (hours)")
        ax1.set_title("Time Data Visualization")

        # Plotting the line graph using Matplotlib
        line = ax2.plot(df["Date"], df["Time (hours)"], marker='o', color='red', label='Line Graph')
        ax2.axhline(y=avg_time, color='green', linestyle='-', label='Average Time')
        ax2.set_xlabel("Date")
        ax2.set_ylabel("Time (hours)")
        ax2.legend()

        # Formatting x-axis dates
        ax2.set_xticks(df["Date"])
        ax2.set_xticklabels(df["Date"], rotation=45, ha='right')

        # Adjust layout
        fig.tight_layout()
        
        # Save the plot to a BytesIO object
        buf = BytesIO()
        fig.savefig(buf, format="png")
        buf.seek(0)
        
        # Display the plots
        st.pyplot(fig)
        
        # Provide a download link
        st.download_button(
            label="Download graph as PNG",
            data=buf,
            file_name="graph.png",
            mime="image/png"
        )
    else:
        st.write("The CSV file must contain more than one entry to plot the graphs.")

# Streamlit app title and sidebar
st.title("ChronoGraph")
st.sidebar.title("Instructions")

# Sidebar content
st.sidebar.info(
    """
    1. Upload a CSV file containing your time data.
    2. Ensure the file has 'Date' and 'Time (hours)' columns.
    3. View the table and the visualizations.
    """
)

# File uploader to allow the user to upload a CSV file
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

# Main section to display content
if uploaded_file is not None:
    # Read the uploaded CSV file
    df = pd.read_csv(uploaded_file, parse_dates=['Date'])

    # Check if the necessary columns are present in the CSV file
    if 'Date' in df.columns and 'Time (hours)' in df.columns:
        st.write("### Time Entries")
        st.dataframe(df, width=1000, height=300)

        # Plot the graphs
        plot_graphs(df)
    else:
        st.write("The CSV file must contain 'Date' and 'Time (hours)' columns.")

elif st.button("Use Sample Data"):
    # Use sample data for demonstration
    sample_data = {
        "Date": pd.date_range('2023-01-01', periods=10),
        "Time (hours)": [2.5, 3.0, 1.75, 4.0, 2.25, 3.5, 2.0, 1.0, 3.75, 2.75]
    }
    df = pd.DataFrame(sample_data)
    
    st.write("### Sample Time Entries")
    st.dataframe(df, width=1000, height=300)

    # Plot the graphs
    plot_graphs(df)

else:
    st.write("Please upload a CSV file or use sample data.")



# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

# # Set the Streamlit layout to wide mode
# # st.set_page_config(layout="default")

# # Function to plot graphs
# def plot_graphs(df):
#     if len(df) > 1:
#         # Convert 'Date' column to string for proper plotting
#         df['Date'] = df['Date'].dt.strftime('%Y-%m-%d')
        
#         # Calculate the average time
#         avg_time = df["Time (hours)"].mean()

#         # Create figure and axes
#         fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10), sharex=True)

#          # Set background color for the axes
#         ax1.set_facecolor('#faf4ed')
#         ax2.set_facecolor('#faf4ed')

#         # Plotting the bar chart using Seaborn
#         sns.barplot(x="Date", y="Time (hours)", data=df, ax=ax1, color='#69b3a2', alpha=0.7)
#         ax1.set_ylabel("Time (hours)")
#         ax1.set_title("Time Data Visualization")

#         # Plotting the line graph using Matplotlib
#         ax2.plot(df["Date"], df["Time (hours)"], marker='o', color='red', label='Line Graph')
#         ax2.axhline(y=avg_time, color='green', linestyle='-', label='Average Time')
#         ax2.set_xlabel("Date")
#         ax2.set_ylabel("Time (hours)")
#         ax2.legend()

#         # Formatting x-axis dates
#         ax2.set_xticks(df["Date"])
#         ax2.set_xticklabels(df["Date"], rotation=45, ha='right')

#         # Adjust layout
#         fig.tight_layout()
        
#         # Display the plots
#         st.pyplot(fig)
#     else:
#         st.write("The CSV file must contain more than one entry to plot the graphs.")

# # Streamlit app title and sidebar
# st.title("ChronoGraph")
# st.sidebar.title("Instructions")

# # Sidebar content
# st.sidebar.info(
#     """
#     1. Upload a CSV file containing your time data.
#     2. Ensure the file has 'Date' and 'Time (hours)' columns.
#     3. View the table and the visualizations.
#     """
# )

# # File uploader to allow the user to upload a CSV file
# uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

# # Main section to display content
# if uploaded_file is not None:
#     # Read the uploaded CSV file
#     df = pd.read_csv(uploaded_file, parse_dates=['Date'])

#     # Check if the necessary columns are present in the CSV file
#     if 'Date' in df.columns and 'Time (hours)' in df.columns:
#         st.write("### Time Entries")
#         st.dataframe(df, width=1000, height=300)

#         # Plot the graphs
#         plot_graphs(df)
#     else:
#         st.write("The CSV file must contain 'Date' and 'Time (hours)' columns.")

# elif st.button("Use Sample Data"):
#     # Use sample data for demonstration
#     sample_data = {
#         "Date": pd.date_range('2023-01-01', periods=10),
#         "Time (hours)": [2.5, 3.0, 1.75, 4.0, 2.25, 3.5, 2.0, 1.0, 3.75, 2.75]
#     }
#     df = pd.DataFrame(sample_data)
    
#     st.write("### Sample Time Entries")
#     st.dataframe(df, width=1000, height=300)

#     # Plot the graphs
#     plot_graphs(df)

# else:
#     st.write("Please upload a CSV file or use sample data.")



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
