import datetime
import json
import logging
import pickle

from django.db import models
from hashid_field import HashidAutoField
import requests
from icalendar import Calendar
from django.utils import timezone

logger = logging.getLogger(__name__)


class Team(models.Model):
    id = HashidAutoField(primary_key=True)
    name = models.TextField(unique=True)
    ical_games_url = models.URLField(null=True, blank=True)

    _ical_cache = models.BinaryField(null=True, blank=True, editable=False)
    _ical_cache_on = models.DateTimeField(null=True, blank=True)

    is_active = models.BooleanField(default=True)

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    @property
    def events(self):
        now = timezone.now()
        mins_ago = now - timezone.timedelta(minutes=5)

        if self._ical_cache_on and self._ical_cache_on > mins_ago:
            return pickle.loads(self._ical_cache)
        else:
            events_data = get_calendar_from_ical(self.ical_games_url)
            self._ical_cache = pickle.dumps(events_data)
            self._ical_cache_on = now
            self.save()
            return events_data

    @property
    def next_game(self):
        return self.events[0] if len(self.events) else ""


def get_calendar_from_ical(url):
    response = requests.get(url)
    response.raise_for_status()  # Raises exception when not a 2xx response
    cal = Calendar.from_ical(response.text)

    events = []

    for component in cal.walk():
        if component.name == "VEVENT":
            # Extracting start and end datetimes
            start = component.get("dtstart").dt
            end = component.get("dtend").dt
            events.append(
                {
                    "summary": component.get("summary"),
                    "description": component.get("description"),
                    "location": component.get("location"),
                    "start": start,
                    "end": end,
                }
            )

    # Filter events that are older than today
    today = datetime.date.today()
    filtered_events = [
        event
        for event in events
        if (
            event["start"].date()
            if isinstance(event["start"], datetime.datetime)
            else event["start"]
        )
        >= today
    ]

    # Sort the filtered events
    sorted_events = sorted(
        filtered_events,
        key=lambda x: x["start"].date()
        if isinstance(x["start"], datetime.datetime)
        else x["start"],
    )

    return sorted_events
