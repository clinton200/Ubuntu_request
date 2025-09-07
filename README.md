# Ubuntu_Requests

## The Wisdom of Ubuntu: *"I am because we are"*

This project embraces the Ubuntu philosophy of **community, respect, and sharing**.  
It is a Python script that connects to the wider web community, respectfully fetches shared resources (images), and organizes them for later appreciation — while taking precautions to protect the user.

---

## Features
- Accepts **multiple image URLs** at once (separated by spaces or commas).  
- Creates a folder **Fetched_Images/** to store downloads.  
- **Validates file type and size** before downloading (only images, max 10MB).  
- **Prevents duplicates** by checking image hashes (SHA256).  
- **Ensures unique filenames** to avoid overwriting existing files.  
- Handles errors gracefully (timeouts, invalid links, bad responses).  

---

## Technologies Used
- Python 3.x  
- requests(https://pypi.org/project/requests/) library  
- Standard libraries: `os`, `uuid`, `hashlib`, `urllib.parse`  

---

## How to Run

1. **Clone the repository**
   ```bash
   git clone https://github.com/clinton200/Ubuntu_request.git
   cd Ubuntu_Requests
