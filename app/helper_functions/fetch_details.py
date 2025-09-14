import requests
import json
import time
import random
from datetime import datetime, timezone

BASE_URL = "http://127.0.0.1:3123"

# ----------------------------
# 1. Fetch raw data from Docker API
# ----------------------------
def fetch_all_animals(output_file: str = "animals_raw.json"):
    all_animals = []
    page = 1
    total_pages = 1  # placeholder

    while page <= total_pages:
        try:
            resp = requests.get(f"{BASE_URL}/animals/v1/animals?page={page}", timeout=10)
            
            if resp.status_code != 200:
                print(f"Page {page}: Error {resp.status_code}, retrying...")
                time.sleep(2)
                continue

            data = resp.json()
            total_pages = data.get("total_pages", total_pages)

            print(f"Fetching page {page}/{total_pages} with {len(data['items'])} animals")

            for item in data["items"]:
                animal_id = item["id"]
                details = fetch_animal_details(animal_id)
                if details:
                    all_animals.append(details)

            page += 1

        except Exception as e:
            print(f"Error fetching page {page}: {e}, retrying...")
            time.sleep(2)

    # Save raw data
    with open(output_file, "w") as f:
        json.dump(all_animals, f, indent=2)

    print(f"✅ Saved {len(all_animals)} raw animals to {output_file}")
    return output_file


def fetch_animal_details(animal_id: int, retries: int = 3):
    for attempt in range(retries):
        try:
            resp = requests.get(f"{BASE_URL}/animals/v1/animals/{animal_id}", timeout=10)

            if resp.status_code == 200:
                return resp.json()
            else:
                print(f"Animal {animal_id}: Error {resp.status_code}, retry {attempt+1}/{retries}")
        except Exception as e:
            print(f"Animal {animal_id}: Exception {e}, retry {attempt+1}/{retries}")

        # Wait before retry
        time.sleep(random.uniform(1, 3))

    return None