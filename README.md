Python
├── Playwright       → Crawl
├── BeautifulSoup    → Parse HTML
├── Pydantic         → Data validation
├── FastAPI          → Backend API
├── PostgreSQL       → Database
├── Redis            → Cache
├── RabbitMQ         → Task queue
├── Kafka            → Event streaming
├── OpenAI API       → AI matching
├── Docker           → Deployment
└── Telegram Bot     → Notification
React
   ↓
FastAPI
   ↓
AI Job Hunter
                         ┌──────────────┐
                         │   FastAPI    │
                         │ REST API     │
                         └──────┬───────┘
                                │
                                ▼
                         ┌──────────────┐
                         │ PostgreSQL   │
                         └──────────────┘
                                ▲
                                │
                    ┌───────────┴───────────┐
                    │                       │
              ┌─────┴─────┐           ┌────┴─────┐
              │  Crawler  │           │   Redis  │
              │ Playwright│           │  Cache   │
              │ Beautiful │           └──────────┘
              │   Soup    │
              └─────┬─────┘
                    │
                    ▼
              ┌────────────┐
              │ RabbitMQ   │
              │ Task Queue │
              └─────┬──────┘
                    │
                    ▼
              ┌────────────┐
              │   Kafka    │
              │ Job Events │
              └─────┬──────┘
                    │
          ┌─────────┴─────────┐
          ▼                   ▼
       OpenAI              Telegram
       Matching           Notification

| Phase | Thành phần          | Mục tiêu              |
| ----- | ------------------- | --------------------- |
| 1     | Python + Playwright | Mở website, crawl job |
| 2     | BeautifulSoup       | Parse HTML            |
| 3     | Pydantic            | Chuẩn hóa Job         |
| 4     | PostgreSQL          | Lưu job               |
| 5     | FastAPI             | API quản lý job       |
| 6     | Redis               | Cache/deduplicate     |
| 7     | RabbitMQ            | Chia task crawler     |
| 8     | Kafka               | Phát Job Event        |
| 9     | OpenAI              | Match Job ↔ CV        |
| 10    | Telegram            | Báo job mới           |
| 11    | Docker              | Đóng gói toàn bộ      |



================https://dashboard.api-football.com/profile?access============

app/
│
├── config/
│   └── settings.py
│       → Đọc API key, Telegram token...
│
├── clients/
│   ├── football_api.py
│   │   → Gọi API-Football
│   │
│   └── telegram.py
│       → Gửi message Telegram
│
├── models/
│   └── fixture.py
│       → Model dữ liệu trận đấu
│
├── services/
│   └── football_service.py
│       → Business logic
│
├── scheduler/
│   └── football_scheduler.py
│       → Chạy tự động mỗi X phút
│
└── main.py
    → Entry point


============TELEGRAM API KEY=====================
=====football_result_notify_bot=========
==========football_result_notify_bot============
Done! Congratulations on your new bot. You will find it at t.me/football_result_notify_bot. You can now add a description, about section and profile picture for your bot, see /help for a list of commands. By the way, when you've finished creating your cool bot, ping our Bot Support if you want a better username for it. Just make sure the bot is fully operational before you do this.

Use this token to access the HTTP API:
8564985938:AAG4ZcMHJVyOn72WHEX9WSYpVWtwD4HnZ4w
Keep your token secure and store it safely, it can be used by anyone to control your bot.

For a description of the Bot API, see this page: https://core.telegram.org/bots/api
