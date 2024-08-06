#!/usr/bin/env python
# coding: utf-8

# # Text to Jason file

# In[1]:


pip install pandas openpyxl


# In[2]:


import json

# Specify the path to your text file
txt_file_path = r'C:\Users\MSI\Desktop\New Text Document (3).txt'

# Read the content of the text file
with open(txt_file_path, 'r', encoding='utf-8') as file:
    text_data = file.read()

# Convert the text data into a dictionary
data = {
    "comment": text_data
}

# Write the dictionary to a JSON file
json_file_path = r'E:\AI\Toxic comment detection with API\test.json'
with open(json_file_path, 'w', encoding='utf-8') as json_file:
    json.dump(data, json_file, ensure_ascii=False, indent=4)

print(f"Text file converted to JSON and saved as {json_file_path}.")


# In[ ]:


import pandas as pd
import json

# Load the Excel file
excel_file_path = 'input.xlsx'
df = pd.read_excel(excel_file_path)

# Convert the DataFrame to a list of dictionaries
data = df.to_dict(orient='records')

# Write the list of dictionaries to a JSON file
json_file_path = 'output.json'
with open(json_file_path, 'w', encoding='utf-8') as json_file:
    json.dump(data, json_file, ensure_ascii=False, indent=4)

print(f"Excel file converted to JSON and saved as {json_file_path}.")

