import requests

def fetch_wikipedia_data(query, limit=10):
    try:
        url = f"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch={query}&format=json&srlimit={limit}"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data['query']['search']
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data for {query}: {e}")
        return []

def extract_event_data(search_results):
    events = []
    for result in search_results:
        event = {
            'Title': result['title'],
            'Snippet': result['snippet'],
            'Timestamp': result.get('timestamp', '2024-01-01')  # Default date if not provided
        }
        events.append(event)
    return events
