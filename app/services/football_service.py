from app.clients.football_api import get_fixtures, get_fixture_events
from app.models.event import Event
from app.models.fixture import Fixture
from app.config.settings import PREMIER_LEAGUE_ID

RELEVANT_EVENT_TYPES = ("Goal", "Card")


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
    raw_fixtures = get_fixtures(date=date)

    raw_fixtures = [
        item
        for item in raw_fixtures
        if item["league"]["id"] == PREMIER_LEAGUE_ID
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
