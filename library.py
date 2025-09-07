import requests
import os
from urllib.parse import urlparse
import uuid
import hashlib

# Store hashes of downloaded files to prevent duplicates
downloaded_hashes = set()

def is_valid_image(response):
    """Check headers to ensure the response is an image and safe to download."""
    content_type = response.headers.get("Content-Type", "")
    if not content_type.startswith("image/"):
        print(f"✗ Skipped: Content-Type '{content_type}' is not an image.")
        return False

    # Limit file size (example: 10 MB)
    content_length = response.headers.get("Content-Length")
    if content_length and int(content_length) > 10 * 1024 * 1024:
        print("✗ Skipped: File too large (over 10 MB).")
        return False

    return True

def get_file_hash(content):
    """Generate SHA256 hash of the file content."""
    return hashlib.sha256(content).hexdigest()

def fetch_images(urls):
    os.makedirs("Fetched_Images", exist_ok=True)

    for url in urls:
        url = url.strip()
        if not url:
            continue

        try:
            # Fetch image headers first
            response = requests.get(url, timeout=10, stream=True)
            response.raise_for_status()

            if not is_valid_image(response):
                continue


            content = response.content
            file_hash = get_file_hash(content)

            # Check if file already downloaded
            if file_hash in downloaded_hashes:
                print(f" Skipped duplicate: {url}")
                continue
            downloaded_hashes.add(file_hash)

            # Extract filename
            parsed_url = urlparse(url)
            filename = os.path.basename(parsed_url.path)

            if not filename:
                filename = f"image_{uuid.uuid4().hex}.jpeg"

            # Ensure unique filename
            filepath = os.path.join("Fetched_Images", filename)
            base, ext = os.path.splitext(filepath)
            counter = 1
            while os.path.exists(filepath):
                filepath = f"{base}_{counter}{ext}"
                counter += 1

            # Save file
            with open(filepath, "wb") as f:
                f.write(content)

            print(f"✓ Saved: {filename} → {filepath}")

        except requests.exceptions.RequestException as e:
            print(f"✗ Connection error for {url}: {e}")
        except Exception as e:
            print(f"✗ An error occurred for {url}: {e}")

def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("Mindfully collecting images from the web, with safety first \n")

    urls = input("Enter image URLs (separate with spaces or commas): ")
    url_list = [u for u in urls.replace(",", " ").split() if u]

    if not url_list:
        print("✗ No valid URLs provided.")
        return

    fetch_images(url_list)
    print("\n All connections strengthened. Community enriched.")

if __name__ == "__main__":
    main()
