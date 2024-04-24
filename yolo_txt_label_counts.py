import os

def count_rows_in_txt_files(directory):
    total_rows = 0
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.txt'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    total_rows += sum(1 for line in f)
    return total_rows

directory_path = 'person_val_test/valid/labels'
total_rows = count_rows_in_txt_files(directory_path)
print(f"Total number of rows in all .txt files: {total_rows}")
