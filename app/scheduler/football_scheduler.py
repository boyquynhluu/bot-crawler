import time

import schedule

from app.football_main import main as run_football_main

RUN_TIME = "07:00"


def job():
    print(f"Running football job at {time.strftime('%Y-%m-%d %H:%M:%S')}")
    run_football_main()


def main():
    schedule.every().day.at(RUN_TIME).do(job)

    print(f"Scheduler started, will run daily at {RUN_TIME}")

    while True:
        schedule.run_pending()
        time.sleep(60)


if __name__ == "__main__":
    main()
