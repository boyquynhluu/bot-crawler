import sys
from datetime import date, timedelta

from app.clients.telegram import send_message
from app.services.football_service import get_fixtures_by_date


EVENT_ICONS = {
    "Normal Goal": "⚽",
    "Own Goal": "⚽🔴",
    "Penalty": "⚽",
    "Missed Penalty": "❌",
    "Yellow Card": "🟨",
    "Red Card": "🟥",
    "Second Yellow card": "🟨🟥",
}


def format_fixture_message(fixture) -> str:
    lines = [
        f"<b>[{fixture.league}] {fixture.home_team} "
        f"{fixture.home_score} - {fixture.away_score} "
        f"{fixture.away_team}</b> ({fixture.status})"
    ]

    for event in fixture.events:
        icon = EVENT_ICONS.get(event.detail, "")
        lines.append(
            f"{icon} {event.minute}' {event.detail} - "
            f"{event.player} ({event.team})"
        )

    return "\n".join(lines)


def main():

    sys.stdout.reconfigure(encoding="utf-8")

    if len(sys.argv) > 1:
        target_date = sys.argv[1]
    else:
        target_date = (date.today() - timedelta(days=1)).isoformat()

    fixtures = get_fixtures_by_date(target_date)

    print(f"Total fixtures: {len(fixtures)}")

    messages = [format_fixture_message(fixture) for fixture in fixtures]
    full_message = "\n\n".join(messages)

    print(full_message)
    send_message(full_message)


if __name__ == "__main__":
    main()
