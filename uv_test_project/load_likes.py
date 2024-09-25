import json
from pathlib import Path


def load_likes(data_directory):
    likes = []
    data_path = Path(data_directory)
    # Find all like files in the data directory
    like_files = data_path.glob("like*.js")
    for file_path in like_files:
        with file_path.open("r", encoding="utf-8") as f:
            content = f.read()
            # Remove the JavaScript variable assignment
            try:
                json_data = content[content.index("=") + 1 :].strip()
                like_part = json.loads(json_data)
                likes.extend(like_part)
            except Exception as e:
                print(f"Error processing file {file_path}: {e}")
    return likes


def main():
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
