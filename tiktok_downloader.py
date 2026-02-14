import requests


def download_tiktok_video_without_watermark():
    url = input("Enter TikTok video URL: ").strip()
    api_url = f"https://www.tikwm.com/api/?url={url}"

    try:
        response = requests.get(api_url)
        response.raise_for_status()
        data = response.json()

        if "data" in data and "play" in data["data"]:
            video_url = data["data"]["play"]
            video_content = requests.get(video_url).content

            with open("tiktok_video_without_watermark.mp4", "wb") as f:
                f.write(video_content)
            print("Download complete: tiktok_video_without_watermark.mp4")

        else:
            print("Could not find video URL")

    except Exception as e:
        print("Error: ", e)


download_tiktok_video_without_watermark()
