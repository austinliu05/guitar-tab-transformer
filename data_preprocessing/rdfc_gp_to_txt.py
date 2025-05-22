import os
import subprocess

# import pprint
# import re

script_path = "/home/claudehu/Desktop/repo/guitar-tab-transformer/backend/tab-processing/simplified_dadagp.py"

input_folder = "/home/claudehu/Desktop/data/music/gps/rdcf"

output_folder = "/home/claudehu/Desktop/data/music/text/rdcf"

os.makedirs(output_folder, exist_ok=True)

error_files = {}
for gp_file in os.listdir(input_folder):
    input_path = os.path.join(input_folder, gp_file)
    output_path = os.path.join(output_folder, f"{os.path.splitext(gp_file)[0]}.txt")

    command = ["python", script_path, "encode", input_path, output_path]
    print(f"\n=== Processing {gp_file} ===")
    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            cwd=os.path.dirname(script_path),
            check=True,
        )
        print("STDOUT:")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        error_files[gp_file] = e.stderr
        # py_error = re.findall(r"^\s*(\w+Error|Exception):\s*(.*)$", e.stderr, re.MULTILINE)
        # error_files[gp_file] = py_error[-1] if py_error else "Unknown error"
        # print(f"❌ Error processing {gp_file}")


print("\n=== Summary ===")
print(f"{len(error_files)} files encountered errors:")
if error_files:
    for file, error in error_files.items():
        print(f"\t{file}")
        print(error)
