# 🧩 Postman Collection Extractor

**A Python tool to convert Postman collection JSON files into clean Excel reports with cURL commands, request types, headers, and bodies.**  
Ideal for developers, testers, and security professionals to analyze or document API endpoints efficiently.

---

## 🚀 Features

✅ Extracts all API requests (including nested folders and subfolders)  
✅ Generates **cURL commands** for each request  
✅ Outputs everything into a structured **Excel (.xlsx)** file  
✅ Automatically detects files ending with `collection.json`  
✅ Works on multiple Postman collection files in a folder  
✅ Handles headers and body information (in JSON format)  
✅ Supports any folder structure and nested collections  

---

## 🧠 Why Use This Tool?

When working with large or complex Postman collections, manually reviewing APIs is slow and error-prone.  
This tool automates the process and helps you:
- Document APIs quickly  
- Share endpoints in readable format  
- Map endpoints for security testing or audits  
- Generate cURL commands for independent testing  

---

## 🗂️ Folder Structure

```
postman-collection-extractor/
│
├── postman_extractor.py        # Main Python script
├── README.md                   # Documentation (this file)
├── LICENSE                     # MIT License
└── requirements.txt             # Dependencies
```

---

## ⚙️ Installation

### 1️⃣ Clone or Download This Repository

#### Option 1: Clone (recommended)
```bash
git clone https://github.com/<your-username>/postman-collection-extractor.git
cd postman-collection-extractor
```

#### Option 2: Download ZIP
- Click on **Code → Download ZIP**
- Extract the ZIP file into a local folder.

---

### 2️⃣ Install Dependencies

You must have **Python 3.8+** installed.

Then install the required packages:
```bash
pip install -r requirements.txt
```

**`requirements.txt` includes:**
```
pandas
openpyxl
```

---

## ▶️ How to Run

Run the script using Python:

```bash
python postman_extractor.py
```

You’ll be prompted for the folder path where your Postman collection files are stored:

```
🔍 Enter the folder path where Postman collections are stored:
Folder path: C:\Users\Dipanjan\Documents\Postman_Collections
```

The tool will:
1. Scan the folder for files containing “collection” and ending in `.json`
2. Extract all API requests recursively
3. Generate cURL commands for each request
4. Export everything into a single Excel file

---

## 📘 Output

After successful execution, you’ll see:

```
✅ Processed: MyAPI.postman_collection.json
🎉 All collections processed successfully!
📘 Output file created: Postman_Collections_Report.xlsx
```

An Excel file named `Postman_Collections_Report.xlsx` will appear in the same folder.

---

## 📊 Excel Report Example

| SL No | Directory / Sub-directory | Request Type | URL | Curl | Others |
|-------|----------------------------|--------------|-----|------|--------|
| 1 | Auth/Login | POST | https://api.example.com/login | curl -X POST 'https://api.example.com/login' -H 'Content-Type: application/json' -d '{"username":"admin","password":"pass"}' | headers and body in JSON |
| 2 | Users/GetAll | GET | https://api.example.com/users | curl -X GET 'https://api.example.com/users' | headers and body in JSON |

---

## 🧩 Example Folder Input

```
Postman_Collections/
│
├── MyAPI.postman_collection.json
├── InternalAPIs.postman_collection.json
└── ExternalAPIs.postman_collection.json
```

Output:
```
Postman_Collections/
└── Postman_Collections_Report.xlsx
```

---

## 🧰 How It Works (Internally)

1. The script scans the folder for `.json` files matching “collection”.  
2. Each collection is parsed recursively using:
   - `extract_requests()` → extracts endpoints, headers, and body
   - `generate_curl()` → builds a cURL command
3. Everything is compiled into a **Pandas DataFrame**.
4. The final report is written using **OpenPyXL** to Excel.

---

## 🪄 Example Use Cases

- 📚 **API Documentation** → Share endpoints with your team in Excel form  
- 🧪 **Security Testing** → Feed cURL commands to Burp Suite or other tools  
- 🧠 **Learning Aid** → Understand how Postman stores request structure  
- 🧾 **Compliance Reports** → Maintain endpoint audit trail  

---

## 💡 Tips

- Works with Postman v2.1 and v2.0 collection formats  
- You can process multiple collections in one run  
- For nested folders, it automatically builds path hierarchies like:
  ```
  Root/Subfolder1/Subfolder2/RequestName
  ```
- You can rename the Excel file if needed after generation

---

## ⚠️ Troubleshooting

| Issue | Possible Cause | Solution |
|-------|----------------|-----------|
| ❌ “Invalid folder path” | Path entered incorrectly | Ensure full absolute path (e.g., `C:\Projects\Postman`) |
| ⚠️ “No Postman collection files found” | Files not named with “collection.json” | Rename or verify files (Postman default export ends with `.postman_collection.json`) |
| ❌ Excel not opening properly | OpenPyXL not installed | Run `pip install openpyxl` |

---
