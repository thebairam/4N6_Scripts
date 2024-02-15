import hashlib
import os

# Function to calculate the hash of a file
def calculate_file_hash(filename, hash_type="sha256"):
    hash_func = getattr(hashlib, hash_type)()
    with open(filename, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_func.update(chunk)
    return hash_func.hexdigest()

# List of files to monitor with their known good hashes
files_to_monitor = {
    r"C:\Users\ADMİN\Documents\TestHashCheck.txt": "d8d76c60b81af1ddd7926d2988a4cbd8",
}

# Checking each file
for file, known_good_hash in files_to_monitor.items():
    if os.path.exists(file):
        current_hash = calculate_file_hash(file)
        if current_hash != known_good_hash:
            print(f"XƏBƏRDARLIQ: Sənəd {file} dəyişdirildi!")
        else:
            print(f"Sənəddə  {file} dəyişiklik qeydə alınmadı.")
    else:
        print(f"SƏHV: Sənəd  {file} mövzud deyil .")

