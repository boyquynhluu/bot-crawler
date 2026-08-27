from datetime import datetime, timedelta, timezone

from app.clients.football_api import get_fixtures, get_fixture_events
from app.models.event import Event
from app.models.fixture import Fixture
from app.config.settings import PREMIER_LEAGUE_ID

RELEVANT_EVENT_TYPES = ("Goal", "Card")
VN_TIMEZONE = timezone(timedelta(hours=7))


def _get_fixture_events(fixture_id: int) -> list[Event]:
    raw_events = get_fixture_events(fixture_id)

    events = []

    for item in raw_events:
        if item["type"] not in RELEVANT_EVENT_TYPES:
            continue

        assist_info = item["assist"]

        events.append(
            Event(
                minute=item["time"]["elapsed"],
                type=item["type"],
                detail=item["detail"],
                team=item["team"]["name"],
                player=item["player"]["name"],
                assist=assist_info["name"] if assist_info else None,
            )
        )

    return events


def get_fixtures_by_date(date: str) -> list[Fixture]:
    target_date = datetime.strptime(date, "%Y-%m-%d").date()

    vn_start = datetime(
        target_date.year, target_date.month, target_date.day,
        tzinfo=VN_TIMEZONE,
    )
    vn_end = vn_start + timedelta(days=1)

    utc_dates = {
        vn_start.astimezone(timezone.utc).date(),
        (vn_end - timedelta(seconds=1)).astimezone(timezone.utc).date(),
    }

    raw_fixtures_by_id = {}

    for utc_date in utc_dates:
        try:
            items = get_fixtures(date=utc_date.isoformat())
        except RuntimeError as error:
            print(f"Skipping {utc_date.isoformat()}: {error}")
            continue

        for item in items:
            raw_fixtures_by_id[item["fixture"]["id"]] = item

    raw_fixtures = [
        item
        for item in raw_fixtures_by_id.values()
        if item["league"]["id"] == PREMIER_LEAGUE_ID
        and vn_start
        <= datetime.fromisoformat(item["fixture"]["date"]).astimezone(VN_TIMEZONE)
        < vn_end
    ]

    fixtures = []

    for item in raw_fixtures:
        fixture_info = item["fixture"]
        league_info = item["league"]
        teams_info = item["teams"]
        goals_info = item["goals"]

        fixtures.append(
            Fixture(
                fixture_id=fixture_info["id"],
                date=fixture_info["date"],
                league=league_info["name"],
                round=league_info["round"],
                home_team=teams_info["home"]["name"],
                away_team=teams_info["away"]["name"],
                home_score=goals_info["home"],
                away_score=goals_info["away"],
                status=fixture_info["status"]["short"],
                events=_get_fixture_events(fixture_info["id"]),
            )
        )

    return fixtures
