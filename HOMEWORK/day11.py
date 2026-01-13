import json
from datetime import datetime
from tracker import create_record

# Step 1: Create a list of travel records
records = [
    travel("Paris", "Loved the Eiffel Tower!", "05-06-2022"),
    create_record("Tokyo", "Amazing sushi experience.", "12-09-2023"),
    create_record("New York", "Times Square was dazzling.", "25-12-2024")
]

# Step 2: Convert date strings to readable format
for record in records:
    date_obj = datetime.strptime(record["date"], "%d-%m-%Y")
    record["date"] = date_obj.strftime("%B %d, %Y")

# Step 3: Convert list of records into JSON string
json_string = json.dumps(records, indent=4)
print("JSON Output:\n", json_string)

# Step 4: Parse JSON back to Python object
parsed_records = json.loads(json_string)

print("\nParsed Records:")
for rec in parsed_records:
    print(rec)