import os
from dotenv import load_dotenv

from app.settings.kafka_settings.producer import producer_send_message

load_dotenv(verbose=True)


def save_in_sql_producer(data, key):
    try:
        producer_send_message(
            topic=os.environ["SAVE_IN_MONGO_TOPIC"],
            value=data,
            key=key.encode("utf-8")
        )
    except Exception as e:
        print(e)