from pytube import *
from typing import Any


def get_video_info(youtube_url: str, download_status: str) -> Any:
    """ Return a list contain the following information from the video:
    - The video title
    - The video (YouTube) url
    - The channel's name
    - The channel's (YouTube) url
    """
    youtube_object = YouTube(youtube_url)
    video_details = youtube_object.vid_info['videoDetails']
    video_title = video_details['title']

    channel_object = Channel(youtube_object.channel_url)
    channel_name = channel_object.channel_name
    channel_url = channel_object.channel_url

    video_info = [video_title, youtube_url, channel_name, channel_url, download_status]

    return video_info
