import json
import os
import re
import pandas as pd

# ====== Helper Functions ======

def generate_curl(request):
    """Generate cURL command for each request."""
    method = request.get("method", "")
    url = request.get("url", {}).get("raw", "")
    headers = request.get("header", [])
    body = request.get("body", {})

    curl = f"curl -X {method} '{url}'"
    for h in headers:
        curl += f" -H '{h['key']}: {h['value']}'"
    if body and "raw" in body:
        curl += f" -d '{body['raw']}'"

    return curl


def extract_requests(item, result, parent_path=""):
    """
    Recursively extract all requests from a Postman collection,
    preserving folder/subfolder structure.
    """
    if "item" in item:
        for sub_item in item["item"]:
            sub_name = sub_item.get("name", "")
            new_path = f"{parent_path}/{sub_name}" if parent_path else sub_name
            extract_requests(sub_item, result, new_path)
    else:
        request = item.get("request", {})
        if request:
            entry = {
                "Request Type": request.get("method", ""),
                "URL": request.get("url", {}).get("raw", ""),
                "Curl": generate_curl(request),
                "Directory / Sub-directory": parent_path if parent_path else "Root",
                "Others": json.dumps({
                    "headers": request.get("header", []),
                    "body": request.get("body", {})
                }, indent=2)
            }
            result.append(entry)


def process_collection(collection_path):
    """Process a single Postman collection JSON file."""
    with open(collection_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    requests = []
    extract_requests(data, requests)
    for i, req in enumerate(requests, start=1):
        req["SL No"] = i

    # Reorder columns: SL No, Directory/Sub-directory, Request Type, URL, Curl, Others
    df = pd.DataFrame(requests, columns=["SL No", "Directory / Sub-directory", "Request Type", "URL", "Curl", "Others"])
    return df


# ====== Main Program ======
def main():
    print("🔍 Enter the folder path where Postman collections are stored:")
    folder_path = input("Folder path: ").strip()

    if not os.path.isdir(folder_path):
        print("❌ Invalid folder path. Please try again.")
        return

    # Regex to detect possible Postman collections (commonly end with .postman_collection.json)
    pattern = re.compile(r".*collection.*\.json$", re.IGNORECASE)

    collection_files = [
        os.path.join(folder_path, f)
        for f in os.listdir(folder_path)
        if pattern.match(f)
    ]

    if not collection_files:
        print("⚠️ No Postman collection files found in the folder.")
        return

    output_file = os.path.join(folder_path, "Postman_Collections_Report.xlsx")

    with pd.ExcelWriter(output_file, engine="openpyxl") as writer:
        for file_path in collection_files:
            try:
                df = process_collection(file_path)
                sheet_name = os.path.splitext(os.path.basename(file_path))[0][:30]  # Excel sheet name limit
                df.to_excel(writer, index=False, sheet_name=sheet_name)
                print(f"✅ Processed: {os.path.basename(file_path)}")
            except Exception as e:
                print(f"❌ Failed to process {file_path}: {e}")

    print(f"\n🎉 All collections processed successfully!")
    print(f"📘 Output file created: {output_file}")


if __name__ == "__main__":
    main()
