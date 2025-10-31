# 🧩 Postman Collection Extractor — Convert API Collections to Excel Reports

This Python tool automates the extraction of API details from Postman collection JSON files and converts them into a structured Excel report.  
It’s designed for **developers, testers, and security professionals** who want to quickly review or document API endpoints.

---

## 🚀 Features

✅ Extracts all API requests from Postman collections (including nested folders)  
✅ Generates **cURL commands** for each request  
✅ Supports multiple collection files in a single folder  
✅ Creates a clean **Excel report (.xlsx)** with the following columns:
- SL No  
- Directory / Sub-directory  
- Request Type  
- URL  
- Curl  
- Others (Headers & Body in JSON format)

✅ Automatically detects files ending with `collection.json`  
✅ Handles subfolders and nested API structures recursively

---

## 🧰 Requirements

Install the dependencies using:

```bash
pip install -r requirements.txt
