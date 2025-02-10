import pandas as pd
import json
from confluent_kafka import Producer
from twitter_model import TweetModel

TOPIC = "twitter_proje"
conf = {
    'bootstrap.servers':"pkc-p11xm.us-east-1.aws.confluent.cloud:9092",
    'security.protocol':"SASL_SSL",
    "sasl.mechanisms":"PLAIN",
    "sasl.username":"5UIIQYJCBD7AUKYP",
    "sasl.password":"Cw+QNQgdnJ/sUqoWjLWVdoxsqb6ppkUoh8OZ/I3SgokiaBpeknVfPS3Md/YF9Lv+"
}

producer = Producer(conf)

# None Verileri Almamak için fonksiyon tanımlayalım
def delivery_report(err, msg):
    if err is not None:
        print(f"Mesaj Produce Edilemedi: {err}")
    else:
        print(f"Mesaj {msg.topic()} konusuna, partition {msg.partition()} gönderildi")
data = pd.read_csv('tweets_v8 (1).csv')
partition = 0
for index, row in data.iterrows():
    # TwitterModel Sınıfda modellediğim veri yapısıyla döngü olmasını istiyorum
    tweetModel = TweetModel()
    tweetModel.set_user_name(row.iloc[0])
    tweetModel.set_user_fallowers(row.iloc[4])
    tweetModel.set_user_friends(row.iloc[5])
    tweetModel.set_user_favorites(row.iloc[6])
    print(tweetModel)

    # Key ve Value verilerini JSON formatına çevirip utf-8 encode edicez
    key = json.dumps(partition).encode('utf-8')
    value = json.dumps(tweetModel.__dict__).encode('utf-8')

    producer.produce(
        topic = TOPIC,
        key = key,
        value = value,
        partition = partition,
        callback = delivery_report
    )
    # Call back fonksiyonnun tetiklenmesi için poll ile çağırıyoruz
    producer.poll(0)

    producer.flush() # her gönderimden sonra ön beliği temizleriz ki gönderim garanti olsım
    partition += 1
    if partition >= 6:
        partition = 0