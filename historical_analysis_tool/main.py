import argparse
from .fetch_data import fetch_wikipedia_data, extract_event_data
from .visualize import create_timeline

def main():
    parser = argparse.ArgumentParser(description="Fetch and visualize historical data.")
    parser.add_argument('--figures', type=str, help="Comma-separated list of historical figures/events", required=False)
    parser.add_argument('--limit', type=int, default=10, help="Number of search results to fetch per figure")
    args = parser.parse_args()

    if args.figures:
        figures = [figure.strip() for figure in args.figures.split(",")]
    else:
        figures = [
            "Benjamin Franklin", "Sam Altman", "Nikola Tesla", "Thomas Edison", "Elon Musk",
            "Adolf Hitler", "Donald Trump", "Albert Einstein", "Marie Curie", "Isaac Newton",
            "Steve Jobs", "Tim Berners-Lee"
        ]

    all_events = []
    for figure in figures:
        data = fetch_wikipedia_data(figure, limit=args.limit)
        events = extract_event_data(data)
        for event in events:
            event['Figure'] = figure
        all_events.extend(events)

    create_timeline(all_events)

if __name__ == "__main__":
    main()
