import requests
import sys
import json

def create_board(api_key, token, board_name="Proofreading Kanban 🌱"):
    url = "https://api.trello.com/1/boards/"
    query = {
        'key': api_key,
        'token': token,
        'name': board_name,
        'defaultLists': False,
        'prefs_background': 'blue'  # cozy blue default, can be changed later
    }
    response = requests.post(url, params=query)
    if response.status_code != 200:
        print(f"Error creating board: {response.text}")
        sys.exit(1)
    board = response.json()
    print(f"Created cozy board: {board['name']} → {board['shortUrl']}")
    return board['id'], board['shortUrl']


def create_list(api_key, token, board_id, list_name, pos='bottom'):
    url = "https://api.trello.com/1/lists"
    query = {
        'key': api_key,
        'token': token,
        'name': list_name,
        'idBoard': board_id,
        'pos': pos
    }
    response = requests.post(url, params=query)
    if response.status_code != 200:
        print(f"Error creating list '{list_name}': {response.text}")
        sys.exit(1)
    return response.json()['id']


def create_card(api_key, token, list_id, card_name, desc, pos='bottom'):
    url = "https://api.trello.com/1/cards"
    query = {
        'key': api_key,
        'token': token,
        'idList': list_id,
        'name': card_name,
        'desc': desc,
        'pos': pos
    }
    response = requests.post(url, params=query)
    if response.status_code != 200:
        print(f"Error creating card '{card_name}': {response.text}")
        return None
    return response.json()['id']


def main():
    print("Good morning! ☕ Let's turn your text pile into a cozy Trello board.\n")

    api_key = input("Trello API key: ").strip()
    token = input("Trello API token: ").strip()
    text_file = input("Path to your .md/.txt file: ").strip()

    try:
        with open(text_file, 'r', encoding='utf-8') as f:
            text = f.read().strip()
        # Split on double newlines, ignore empty blocks
        paragraphs = [p.strip() for p in text.split('\n\n') if p.strip()]
        print(f"\nFound {len(paragraphs)} paragraphs. Ready to make cushions... 🌱")
    except Exception as e:
        print(f"\nOops, couldn't read the file: {e}")
        sys.exit(1)

    if not paragraphs:
        print("No content found. Maybe the file is empty?")
        sys.exit(1)

    board_id, board_url = create_board(api_key, token)

    # Create cozy lists
    todo_list_id   = create_list(api_key, token, board_id, "To Review 🌅")
    doing_list_id  = create_list(api_key, token, board_id, "Reviewing ☕")
    done_list_id   = create_list(api_key, token, board_id, "Polished ✨")

    # Add paragraphs as cards
    for i, para in enumerate(paragraphs, start=1):
        card_name = f"¶ {i}"
        # Shorten description preview if very long (Trello has limits)
        desc_preview = para[:4000] + "…" if len(para) > 4000 else para
        create_card(api_key, token, todo_list_id, card_name, desc_preview)
        print(f"  Added card {i}/{len(paragraphs)}")

    print(f"\nAll done! Your cozy proofreading board is waiting here:")
    print(f"  {board_url}")
    print("\nGo make some coffee and start dragging cushions around. ☕🛋️")


if __name__ == "__main__":
    main()