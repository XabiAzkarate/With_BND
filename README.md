# With_BND - Xabier Rocket Bot
This project contains a Telegram bot (xabier_rocket_bot) that interacts with users to pinpoint the exact frame of a rocket launch video using the bisection algorithm.

## Getting Started
These instructions will guide you on how to deploy and run the project on your local machine and in production.

### Prerequisites
- Docker
- Docker Compose
- Python (version 3.8 or higher)
- A Telegram account

### Local Setup
1. Clone the repository

```
git clone <https://github.com/XabiAzkarate/With_BND.git>
```

2. Set up environment variables

Copy the .env.example file to .env and fill in the required values, such as the Telegram bot token.

3. Build and run the Docker containers

```
docker-compose build
docker-compose up -d
```

4. Start the Telegram bot
```
docker exec -it <container_id> python -m rocket_bot.bot_logic.telegram_bot
```
Check the logs to ensure it's running:
```
docker-compose logs
```

## Usage

### Start the bot

Open your Telegram app and search for @xabier_rocket_bot.

### Interact with the bot

Send /start to begin the interaction. The bot will show different frames from a rocket launch video. Your task is to tell the bot whether the rocket has launched in the displayed frame or not. Based on your inputs, the bot will use the bisection algorithm to find the exact frame where the rocket launched.

