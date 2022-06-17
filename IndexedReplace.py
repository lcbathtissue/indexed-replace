target_file = input("Enter the name of the file you want to modify:")
target_str = input("Enter the text you want to replace with line numbers:")

with open(target_file, "r", encoding="utf-8") as tar_file:
    file_contents = tar_file.read().split("\n")

target_file_str_assembly = ""
for line_num, line in enumerate(file_contents):
    mutated_line = line.replace(target_str, f"#{line_num + 1}")
    target_file_str_assembly = target_file_str_assembly + mutated_line + "\n"

target_file_str_assembly = target_file_str_assembly[:-1]
target_file = "modified_" + target_file

with open(target_file, "w", encoding="utf-8") as tar_file:
    tar_file.write(target_file_str_assembly)

print(f"Finished!\nChanged saved to {target_file}")
