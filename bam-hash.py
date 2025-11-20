import hashlib
import argparse
import tqdm
import os

def sha3_large_file(filepath, chunk_size=1024):
    hash_sha3 = hashlib.sha3_512()
    with open(filepath, "rb") as f:
        progress = tqdm.tqdm(total=os.path.getsize(filepath), unit="B", unit_scale=True, desc=filepath)
        for chunk in iter(lambda: f.read(chunk_size), b""):
            hash_sha3.update(chunk)
            progress.update(chunk_size)
    return hash_sha3.hexdigest()

def main():
    parser = argparse.ArgumentParser(description="Calculate SHA-3 512 bits hash of a file.")
    parser.add_argument("filepath", help="The file path of the file to hash.")
    args = parser.parse_args()

    # Compute and print the hash
    try:
        sha3_hash = sha3_large_file(args.filepath)
        with open(f"{args.filepath}.sh3", "w") as f:
            f.write(sha3_hash)
        print(f"The SHA-3 512 bits hash of the file {args.filepath} is:\n{sha3_hash}")
        print(f"Saved SHA-3 value to {args.filepath}.sh3")
    except FileNotFoundError:
        print("File not found. Please check the path and try again.")
    except IOError as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
