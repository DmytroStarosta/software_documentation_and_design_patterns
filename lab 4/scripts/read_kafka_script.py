from kafka import KafkaConsumer

consumer = KafkaConsumer(
    'taxi_trips',
    bootstrap_servers='localhost:9092',
    api_version=(0, 11, 5),
    auto_offset_reset='earliest',
    enable_auto_commit=True
)

def main():
    try:
        for message in consumer:
            if message:
                print(message.value.decode('utf-8'))
    except Exception as ex:
        print(f'Error: {ex}')
    except KeyboardInterrupt:
        print('Stop read by Ctrl+C')
    finally:
        print('This is in kafka')
        consumer.close()

if __name__ == '__main__':
    main()