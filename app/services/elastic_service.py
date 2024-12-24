import json
from datetime import date

from app.elasticsearch_db.elastic_repository import save_to_elasticsearch
from app.utils.num_util import convert_to_int, convert_to_float


def dave_in_elastic(events):
    for event in events:
        save_to_elasticsearch(json.dumps({
            "event_id": convert_to_int(event["eventid"]),
            "date": str(date(
                year=convert_to_int(event['iyear']) or 2024,
                month=convert_to_int(event['imonth']) or 1,
                day=convert_to_int(event['iday'] or 1)
            )),
            "category": "past",
            "lat": convert_to_float(event["latitude"]),
            "lon": convert_to_float(event["longitude"]),
            "body": event["Description"]
        }))