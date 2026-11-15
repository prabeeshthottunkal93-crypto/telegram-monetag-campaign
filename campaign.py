import json
import os
import random
import urllib.parse
import urllib.request

BOT_TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
CHANNEL = "@goddessneha69"
SMARTLINK = "https://uplcm.com/4/12218619"

MESSAGES = [
    "✨ Discover something interesting today.\n\nThis is an external sponsored link. Open it only if you want to.",
    "🌟 Take a look at today's featured link.\n\nSponsored external link — destination is provided by the advertiser.",
    "🔎 Curious? You can explore this advertiser link here.\n\nOptional external link. Please browse responsibly.",
    "💫 A new link to check out.\n\nThis is a sponsored link that opens an external website.",
    "📌 Today's featured promotion is available below.\n\nAdvertisement / external link. Open at your discretion."
]

def main():
    text = random.choice(MESSAGES)
    payload = {
        "chat_id": CHANNEL,
        "text": text,
        "reply_markup": {
            "inline_keyboard": [[
                {"text": "View sponsored link", "url": SMARTLINK}
            ]]
        },
        "disable_web_page_preview": True
    }
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = urllib.parse.urlencode({"": ""}).encode()
    request = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"}
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        result = json.loads(response.read().decode("utf-8"))
    if not result.get("ok"):
        raise RuntimeError(f"Telegram API error: {result}")
    print("Campaign post sent successfully.")

if __name__ == "__main__":
    main()
