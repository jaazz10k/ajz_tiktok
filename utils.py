import time

def download_single(url):
    # Simulated response
    return {
        'status': 'success',
        'url': url,
        'downloadUrl': f"https://example.com/download/{int(time.time())}.mp4",
        'title': "Sample TikTok Video"
    }

def download_multiple(urls):
    return [download_single(url) for url in urls]

def download_by_username(username):
    return [
        {
            'id': i,
            'url': f'https://www.tiktok.com/@{username}/video/{i}',
            'thumbnail': f'https://picsum.photos/id/{i}/200/300',
            'description': f'TikTok #{i} from @{username}'
        }
        for i in range(1, 6)
    ]
