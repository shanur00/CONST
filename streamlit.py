import streamlit as st
import pandas as pd
import plotly.express as px

st.title("ChronoGraph")

# File uploader to allow the user to upload a CSV file
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # Read the uploaded CSV file
    df = pd.read_csv(uploaded_file, parse_dates=['Date'])

    # Check if the necessary columns are present in the CSV file
    if 'Date' in df.columns and 'Time (hours)' in df.columns:
        st.write("### Time Entries")
        st.write(df)

        # Plot the 3D scatter plot
        if len(df) > 1:
            fig = px.scatter_3d(
                df, x='Date', y='Time (hours)', z='Time (hours)',
                title='3D Time Line Graph',
                labels={'Date': 'Date', 'Time (hours)': 'Time (hours)'}
            )

            # Format dates for better readability
            fig.update_layout(scene=dict(
                xaxis=dict(title='Date', tickformat='%Y-%m-%d'),
                yaxis=dict(title='Time (hours)'),
                zaxis=dict(title='Time (hours)')
            ))
            
            # Display the plot
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.write("The CSV file must contain more than one entry to plot the graph.")
    else:
        st.write("The CSV file must contain 'Date' and 'Time (hours)' columns.")
else:
    st.write("Please upload a CSV file.")





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
