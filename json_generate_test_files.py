import json
import random
import os

def generate_json_files(num_files, output_dir):
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Base structure
    base_structure = {
        "first_name": "",
        "last_name": "",
        "email": [],
        "gender": "",
        "color": "",
        "remarks": [],
        "associations": {
            "individual": [],
            "country": [],
            "document": [],
            "organization": []
        }
    }

    # Possible variations
    variations = [
        {"add": "age", "type": "int"},
        {"add": "phone", "type": "str"},
        {"add": "address", "type": "str"},
        {"remove": "color"},
        {"remove": "remarks"},
        {"add": "occupation", "type": "str"},
        {"add": "hobbies", "type": "list"},
        {"remove": "associations.document"},
        {"add": "associations.city", "type": "list"},
        {"add": "marital_status", "type": "str"}
    ]

    # Generate files
    for i in range(num_files):
        # Start with the base structure
        data = base_structure.copy()
        
        # Apply random variations
        num_variations = random.randint(1, 3)
        applied_variations = random.sample(variations, num_variations)
        
        for variation in applied_variations:
            if "add" in variation:
                if variation["type"] == "int":
                    data[variation["add"]] = random.randint(18, 80)
                elif variation["type"] == "str":
                    data[variation["add"]] = f"Sample_{variation['add']}_{i}"
                elif variation["type"] == "list":
                    data[variation["add"]] = [f"Item_{j}" for j in range(random.randint(1, 3))]
            elif "remove" in variation:
                keys = variation["remove"].split('.')
                if len(keys) == 1:
                    data.pop(keys[0], None)
                elif len(keys) == 2:
                    data[keys[0]].pop(keys[1], None)

        # Fill in the data
        data["first_name"] = f"FirstName_{i}"
        data["last_name"] = f"LastName_{i}"
        data["email"] = [f"email{i}@example.com", f"email{i}_alt@example.com"]
        data["gender"] = random.choice(["Male", "Female", "Other"])
        if "color" in data:
            data["color"] = random.choice(["Red", "Blue", "Green", "Yellow", "Purple"])
        if "remarks" in data:
            data["remarks"] = [f"Remark {j} for person {i}" for j in range(random.randint(1, 3))]
        
        for assoc_type in data["associations"]:
            data["associations"][assoc_type] = [f"{assoc_type[:3]}_{random.randint(10000, 99999)}" for _ in range(random.randint(1, 5))]

        # Write to file
        filename = os.path.join(output_dir, f"{i+1:05d}.json")
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)

    print(f"{num_files} JSON files have been generated in {output_dir}")

# Usage
output_directory = r"C:\Users\kroy2\Documents\python\projects\json_generate_test_files\data"
generate_json_files(50, output_directory)