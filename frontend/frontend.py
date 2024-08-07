import pandas as pd
import requests
import streamlit as st

# Set page title
st.set_page_config(page_title="ConvFinQA")

# Title
st.title("ConvFinQA")


# Function to fetch IDs from the backend API
def fetch_ids():
    api_url = "http://127.0.0.1:8000/api/v1/all_ids"
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()
    else:
        st.error(f"Error fetching IDs: {response.status_code}")
        return []


# Fetch options for the dropdown menu
options = fetch_ids()

# Dropdown menu
selected_option = st.selectbox("Select an option", options)


# Function to merge and process tables
def merge_and_process_tables(table_ori, table):
    # Ensure table_ori and table are not empty
    if not table_ori or not table:
        st.error("Table data is incomplete.")
        return pd.DataFrame()

    # Extract headers from table_ori
    headers = table_ori[0] if table_ori else []
    if len(table_ori) > 1:
        headers.extend(table_ori[1])
    headers = [h for h in headers if h]  # Remove empty strings

    # Use data from the processed table
    data = table[1:]  # Skip the first row which contains headers

    # Create DataFrame
    df = pd.DataFrame(data)

    # Dynamically generate headers if there are more columns than headers
    if len(headers) < len(df.columns):
        headers += [f'Column {i + 1}' for i in range(len(headers), len(df.columns))]

    # Assign headers to the DataFrame
    df.columns = headers[:len(df.columns)]

    # Set the first column as index
    df.set_index(df.columns[0], inplace=True)

    # Return the processed DataFrame
    return df


# Function to make API call to fetch data based on selected option
def get_data_from_backend(option):
    api_url = f"http://127.0.0.1:8000/api/v1/data?option={option}"
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()
    else:
        st.error(f"Error fetching data: {response.status_code}")
        return None


# Make API call when option changes
if selected_option:
    data = get_data_from_backend(selected_option)

    if data and "table_ori" in data and "table" in data:
        merged_df = merge_and_process_tables(data["table_ori"], data["table"])
        if not merged_df.empty:
            st.table(merged_df)
        else:
            st.write("No data available for the selected option.")

# Add some space
st.write("")

# Additional text area for Post Text
post_text = st.text_area("Post Text", "Enter your post text here...")
