import pandas as pd
import requests

# Replace with your LM Studio API key
API_KEY = 'lm-studio'
EMBEDDINGS_API_URL = 'http://localhost:1234/v1/embeddings'


def format_table(table):
    table_text = ""
    # Extract headers
    headers = table[0]
    # Extract data rows
    data_rows = table[1:]
    # Create DataFrame
    df = pd.DataFrame(data_rows, columns=headers)
    # Convert DataFrame to text
    for i, row in df.iterrows():
        row_text = " | ".join([str(item) for item in row])
        table_text += row_text + "\n"
    return table_text.strip()


# Function to generate embeddings using LM Studio API
def generate_embeddings(text):
    headers = {
        'Content-Type': 'application/json',
    }
    data = {
        'input': text,
    }
    response = requests.post(EMBEDDINGS_API_URL, json=data, headers=headers)
    if response.status_code == 200:
        response_json = response.json()
        print("Full API Response:", response_json)  # Debugging line
        if 'embedding' in response_json:
            return response_json['embedding']
        else:
            raise KeyError("Key 'embedding' not found in API response")
    else:
        raise Exception(f"Error: {response.status_code} - {response.text}")


# Example data
pre_text = """
26 | 2009 annual report in fiscal 2008, revenues in the credit union systems and services business segment increased 14% (14%) from fiscal 2007.
All revenue components within the segment experienced growth during fiscal 2008.
License revenue generated the largest dollar growth in revenue as Episys AE, our flagship core processing system aimed at larger credit unions, experienced strong sales throughout the year.
Support and service revenue, which is the largest component of total revenues for the credit union segment, experienced 34 percent growth in EFT support and 10 percent growth in in-house support.
Gross profit in this business segment increased $9344 in fiscal 2008 compared to fiscal 2007, due primarily to the increase in license revenue, which carries the highest margins.
Liquidity and capital resources we have historically generated positive cash flow from operations and have generally used funds generated from operations and short-term borrowings on our revolving credit facility to meet capital requirements.
We expect this trend to continue in the future.
"""

post_text = """
Year ended June 30, cash provided by operations increased $25,587 to $206,588 for the fiscal year ended June 30, 2009 as compared to $181,001 for the fiscal year ended June 30, 2008.
This increase is primarily attributable to a decrease in receivables compared to the same period a year ago of $21,214.
This decrease is largely the result of fiscal 2010 annual software maintenance billings being provided to customers earlier than in the prior year, which allowed more cash to be collected before the end of the fiscal year than in previous years.
Further, we collected more cash overall related to revenues that will be recognized in subsequent periods in the current year than in fiscal 2008.
Cash used in investing activities for the fiscal year ended June 2009 was $59,227 and includes $3,027 in contingent consideration paid on prior year's acquisitions.
Cash used in investing activities for the fiscal year ended June 2008 was $102,148 and includes payments for acquisitions of $48,109, plus $1,215 in contingent consideration paid on prior year's acquisitions.
Capital expenditures for fiscal 2009 were $31,562 compared to $31,105 for fiscal 2008.
Cash used for software development in fiscal 2009 was $24,684 compared to $23,736 during the prior year.
Net cash used in financing activities for the current fiscal year was $94,675 and includes the repurchase of 3,106 shares of our common stock for $58,405, the payment of dividends of $26,903 and $13,489 net repayment on our revolving credit facilities.
Cash used in financing activities was partially offset by proceeds of $3,773 from the exercise of stock options and the sale of common stock (through the employee stock purchase plan) and $348 excess tax benefits from stock option exercises.
During fiscal 2008, net cash used in financing activities for the fiscal year was $101,905 and includes the repurchase of 4,200 shares of our common stock for $100,996, the payment of dividends of $24,683 and $429 net repayment on our revolving credit facilities.
Cash used in financing activities was partially offset by proceeds of $20,394 from the exercise of stock options and the sale of common stock and $3,809 excess tax benefits from stock option exercises.
Beginning during fiscal 2008, US financial markets and many of the largest US financial institutions have been shaken by negative developments in the home mortgage industry and the mortgage markets, and particularly the markets for subprime mortgage-backed securities.
Since that time, these and other such developments have resulted in a broad, global economic downturn.
While we, as is the case with most companies, have experienced the effects of this downturn, we have not experienced any significant issues with our current collection efforts, and we believe that any future impact to our liquidity will be minimized by cash generated by recurring sources of revenue and due to our access to available lines of credit.
"""

table_data = [
    ["", "Year ended June 30, 2009", "2008", "2007"],
    ["Net income", "$103,102", "$104,222", "$104,681"],
    ["Non-cash expenses", "74,397", "70,420", "56,348"],
    ["Change in receivables", "21,214", "-2,913", "-28,853"],
    ["Change in deferred revenue", "21,943", "5,100", "24,576"],
    ["Change in other assets and liabilities", "-14,068", "4,172", "17,495"],
    ["Net cash from operating activities", "$206,588", "$181,001", "$174,247"]
]

# Convert table data to text
table_text = format_table(table_data)

# Combine narrative text and table text
combined_text = pre_text + " " + post_text + " " + table_text

# Generate embeddings
try:
    embeddings = generate_embeddings(combined_text)
    print("Embeddings generated successfully.")
    print(embeddings)
except KeyError as e:
    print(f"Failed to generate embeddings: {e}")
except Exception as e:
    print(f"Failed to generate embeddings: {e}")
