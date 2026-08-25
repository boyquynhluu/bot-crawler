import requests

from app.config.settings import (
    API_FOOTBALL_BASE_URL,
    API_FOOTBALL_KEY
)


def _get(endpoint: str, params: dict | None = None) -> dict:
    response = requests.get(
        f"{API_FOOTBALL_BASE_URL}/{endpoint}",
        headers={"x-apisports-key": API_FOOTBALL_KEY},
        params=params,
    )
    response.raise_for_status()

    data = response.json()

    if data.get("errors"):
        raise RuntimeError(f"API-Football error: {data['errors']}")

    return data


def get_fixtures(
    date: str | None = None,
    league: int | None = None,
    season: int | None = None,
    team: int | None = None,
) -> list[dict]:

    params = {
        "date": date,
        "league": league,
        "season": season,
        "team": team,
    }

    params = {
        key: value
        for key, value in params.items()
        if value is not None
    }

    data = _get("fixtures", params)

    return data["response"]


def get_fixture_events(fixture: int) -> list[dict]:
    data = _get("fixtures/events", {"fixture": fixture})

    return data["response"]


def get_teams(
    league: int | None = None,
    season: int | None = None,
    team: int | None = None,
) -> list[dict]:
    params = {
        "league": league,
        "season": season,
        "id": team,
    }
    params = {key: value for key, value in params.items() if value is not None}

    data = _get("teams", params)

    return data["response"]
