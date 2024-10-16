import json
import random
import os
import string

def generate_random_string(length=10):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

    def generate_json_example():
        example = {
            "string": generate_random_string(),
            "number": random.uniform(-1000, 1000),
            "integer": random.randint(-100, 100),
            "float": random.uniform(0, 10),
            "boolean_true": True,
            "boolean_false": False,
            "null_value": None,
            "array": [random.randint(1, 100) for _ in range(5)],
            "nested_object": {
                "name": generate_random_string(),
                "value": random.randint(1, 100)
                },
                "array_of_objects": [
                {"id": i, "name": generate_random_string()} for i in range(1, 4)
                ],
                "object_with_array": {
                    "name": generate_random_string(),
                    "values": [random.randint(1, 100) for _ in range(3)]
                    },
                    "string_with_escapes": f"Line 1\nLine 2\tTabbed\rCarriage Return {generate_random_string()}",
                    "string_with_unicode": f"Unicode: \u00A9 \u2665 \u203C {generate_random_string()}",
                    "empty_object": {},
                    "empty_array": [],
                    "nested_arrays": [
                    [random.randint(1, 10) for _ in range(3)] for _ in range(3)
                    ],
                    "mixed_array": [
                    random.randint(1, 100),
                    generate_random_string(),
                    random.uniform(0, 10),
                    random.choice([True, False]),
                    None,
                    {"key": generate_random_string()}
                ]
            }

            return example

            def write_json_to_file(data, filename):
                with open(filename, 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent=2, ensure_ascii=False)
                    print(f"JSON example has been written to {filename}")

                    def generate_multiple_json_files(num_files, output_directory):
                        os.makedirs(output_directory, exist_ok=True)

                        for i in range(num_files):
                            json_example = generate_json_example()
                            filename = os.path.join(output_directory, f"json_example_{i+1}.json")
                            write_json_to_file(json_example, filename)

                            if __name__ == "__main__":
                                num_files = int(input("Enter the number of JSON files to generate: "))
                                output_directory = input("Enter the output directory path: ")

                                generate_multiple_json_files(num_files, output_directory)
                                print(f"Generated {num_files} JSON files in {output_directory}")
