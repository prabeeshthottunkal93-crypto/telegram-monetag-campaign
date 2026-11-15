# Telegram Monetag campaign

This repository publishes one transparent sponsored-link post to the Telegram channel `@goddessneha69` at five scheduled times each day using GitHub Actions.

## Schedule (India Standard Time)

- 8:00 AM
- 12:00 PM
- 4:00 PM
- 8:00 PM
- 12:00 AM

GitHub Actions cron schedules run in UTC by default. These entries are converted to the corresponding IST times.

## Setup

1. Create a Telegram bot with [@BotFather](https://t.me/BotFather).
2. Add the bot to `@goddessneha69` as an administrator and grant permission to post messages.
3. In this GitHub repository, open **Settings → Secrets and variables → Actions**.
4. Create a repository secret named `TELEGRAM_BOT_TOKEN` and paste the bot token as its value. Never commit the token into a file.
5. Open the **Actions** tab, select **Telegram Monetag campaign**, and choose **Run workflow** to test.

The workflow also runs automatically at the five scheduled times.

## Important

- Posts clearly identify the destination as a sponsored external link.
- Do not use misleading claims, forced clicks, click incentives, bots, or spam.
- Follow Telegram rules and Monetag publisher/traffic policies.
- SmartLink destinations and advertiser pages are controlled by the advertising provider, not this repository.
- GitHub Actions schedules can occasionally be delayed. See [GitHub's schedule documentation](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax).
