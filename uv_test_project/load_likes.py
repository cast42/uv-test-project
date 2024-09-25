import json
from pathlib import Path
from typing import Any  # 'Any' still needs to be imported from 'typing'


def load_likes(data_directory: str) -> list[dict[str, Any]]:
    likes: list[dict[str, Any]] = []
    data_path: Path = Path(data_directory)
    # Find all like files in the data directory
    like_files = data_path.glob("like*.js")
    for file_path in like_files:
        with file_path.open("r", encoding="utf-8") as f:
            content: str = f.read()
            # Remove the JavaScript variable assignment
            try:
                json_data: str = content[content.index("=") + 1 :].strip()
                like_part: list[dict[str, Any]] = json.loads(json_data)
                likes.extend(like_part)
            except Exception as e:
                print(f"Error processing file {file_path}: {e}")
    return likes


def main() -> None:
    data_directory = "/Users/lode/Downloads/data"  # Adjust this path if your data directory is elsewhere
    likes = load_likes(data_directory)
    for like_obj in likes:
        like = like_obj.get("like", {})
        tweet_id = like.get("tweetId", "N/A")
        full_text = like.get("fullText", "")
        favorited_at = like.get("favoritedAt", "N/A")
        expanded_url = like.get("expandedUrl", "N/A")

        print("Tweet ID:", tweet_id)
        print("Favorited At:", favorited_at)
        print("Text:", full_text)
        print("URL:", expanded_url)
        print("-" * 40)


if __name__ == "__main__":
    main()
