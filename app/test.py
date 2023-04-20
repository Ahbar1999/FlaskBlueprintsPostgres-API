
if __name__ == '__main__':
    import httpx
    import time

    for i in range(10):
        payload = {
            'message': f'this is the message no. {i}',
            'location': f'POINT ({i} {i})'
        }
        print(payload)
        httpx.post('http://127.0.0.1:5000/posts/', json=payload)
        time.sleep(1)
    print(httpx.get('http://127.0.0.1:5000/posts/').json())