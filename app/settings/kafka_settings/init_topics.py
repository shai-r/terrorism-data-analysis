import os

from dotenv import load_dotenv
from kafka import KafkaAdminClient
from kafka.admin import NewTopic
from kafka.errors import TopicAlreadyExistsError


load_dotenv(verbose=True)


def init_topics():
    client = KafkaAdminClient(bootstrap_servers=os.environ['BOOTSTRAP_SERVERS'])

    topics_name = [
        os.environ['SAVE_IN_SQL_TOPIC'],
        "bla"
    ]

    existing_topics = client.list_topics()

    topics = [
        NewTopic(
        name=topic_name.strip(),
        num_partitions=int(os.environ['NUM_PARTITIONS']),
        replication_factor=int(os.environ['REPLICATION_FACTOR'])
        )
        for topic_name in topics_name if topic_name not in existing_topics]

    try:
        client.create_topics(topics)

    except TopicAlreadyExistsError as e:
        print(str(e))

    client.close()


