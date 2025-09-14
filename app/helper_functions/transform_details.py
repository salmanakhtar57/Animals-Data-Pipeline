import json
from datetime import datetime, timezone

def transform_fields(file_path: str, output_file: str = "animals_cleaned.json"):
    with open(file_path, "r") as file:
        animals = json.load(file)

    transformed = []

    for animal in animals:
        # Friends field
        if "friends" in animal:
            if animal["friends"] and isinstance(animal["friends"], str):
                separated = animal["friends"].split(",")
                cleaned = [f.strip() for f in separated if f.strip()]
                animal["friends"] = cleaned
            elif not animal["friends"]:
                animal["friends"] = []

        # born_at field
        if "born_at" in animal and animal["born_at"]:
            ts = int(animal["born_at"]) / 1000
            dt = datetime.fromtimestamp(ts, tz=timezone.utc)
            animal["born_at"] = dt.isoformat()

        transformed.append(animal)

    with open(output_file, "w") as f:
        json.dump(transformed, f, indent=2)

    print(f"Saved {len(transformed)} cleaned animals to {output_file}")
    return transformed
