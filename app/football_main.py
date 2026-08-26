import sys
from datetime import datetime, timedelta, timezone

from app.clients.telegram import send_message
from app.services.football_service import get_fixtures_by_date

VN_TIMEZONE = timezone(timedelta(hours=7))


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
        today_vn = datetime.now(VN_TIMEZONE).date()
        target_date = (today_vn - timedelta(days=1)).isoformat()

    fixtures = get_fixtures_by_date(target_date)

    if not fixtures:
        full_message = "⚽ Hôm nay không có trận Ngoại hạng Anh."
    else:
        messages = [format_fixture_message(fixture) for fixture in fixtures]
        full_message = "\n\n".join(messages)

    send_message(full_message)


if __name__ == "__main__":
    main()
