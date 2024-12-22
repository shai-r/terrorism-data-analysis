from app.services.merger_service import send_data_in_batches
from app.services.save_mongo_producer_service import save_in_mongo_producer



if __name__ == '__main__':
    for a in send_data_in_batches():
        save_in_mongo_producer(a, "raw-data")