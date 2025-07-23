from flask import Flask, jsonify, Response
from scraper import fetch_pc_releases
from ics import Calendar, Event
from datetime import datetime
import re

app = Flask(__name__)

@app.route("/api/releases", methods=["GET"])
def releases():
    return jsonify(fetch_pc_releases())

@app.route("/api/releases.ics", methods=["GET"])
def calendar():
    games = fetch_pc_releases()
    cal = Calendar()

    for game in games:
        try:
            title = game["title"]
            date_str = game["release_date"]
            # Parse common formats like "Jul 30, 2025"
            date_obj = datetime.strptime(date_str, "%b %d, %Y")
        except Exception:
            continue  # skip invalid or unknown dates

        event = Event()
        event.name = f"{title} (PC)"
        event.begin = date_obj
        event.description = f"Releases on {date_str}"
        cal.events.add(event)

    return Response(str(cal), mimetype="text/calendar")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

