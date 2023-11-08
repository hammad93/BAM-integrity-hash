import hashlib
import argparse

def md5_large_file(filepath, chunk_size=8192):
    hash_md5 = hashlib.md5()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(chunk_size), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def main():
    parser = argparse.ArgumentParser(description="Calculate MD5 hash of a file.")
    parser.add_argument("filepath", help="The file path of the file to hash.")
    args = parser.parse_args()

    # Compute and print the MD5
    try:
        md5_hash = md5_large_file(args.filepath)
        print(f"The MD5 hash of the file {args.filepath} is: {md5_hash}")
    except FileNotFoundError:
        print("File not found. Please check the path and try again.")
    except IOError as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
