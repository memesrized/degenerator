import requests


def get_random_pic():
    return requests.get("https://picsum.photos/1000/300").content


def get_random_fact():
    return requests.get("https://uselessfacts.jsph.pl/random.json?language=en").json()[
        "text"
    ]


def get_random_style_transfer():
    r = requests.post(
        "https://api.deepai.org/api/neural-style",
        data={
            "style": "https://picsum.photos/1000/300",
            "content": "https://picsum.photos/1000/300",
        },
        headers={"api-key": "quickstart-QUdJIGlzIGNvbWluZy4uLi4K"},
    ).json()
    return requests.get(r["output_url"]).content
