import json
import redis


def main():
    r = redis.Redis(host="localhost", port=6379)
    len_read = 100
    start = 0

    while True:
        rows = r.lrange('taxi_trips_list', start, start + len_read -1)

        if not rows:
            break

        rows = [json.loads(row) for row in rows]
        print(rows)
        start += len_read

    print('This is in redis')

if __name__ == "__main__":
    main()