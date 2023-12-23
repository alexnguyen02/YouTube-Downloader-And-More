import pytube.exceptions as exceptions
import requests
from pytube import *
from typing import Any


def download_video(youtube_url: str, output_folder: str) -> Any:
    """Download the YouTube video from the url entered by the user

    Direct the downloaded video to the desired folder

    Return the download status of the video (downloaded, or error)
    """
    # Make a request to the youtube url
    request = requests.get(youtube_url)
    invalid = "Video unavailable" in request.text

    if invalid is True:
        return "Video is unavailable"
    else:
        pass

    youtube_object = YouTube(youtube_url)
    youtube_object.check_availability()

    try:
        folder = f"/Users/HP/PycharmProjects/youtubeDownload/downloaded_videos/{output_folder}/new_list"
        video = youtube_object.streams.get_highest_resolution()
        video.download(output_path=folder,
                       filename_prefix=f"[{video.resolution}] ")
        download_status = 'downloaded'
        print("Successfully downloaded")

    except exceptions.AgeRestrictedError:
        print("Age-resticted error. Please try again")
        download_status = 'error'
        pass

    return download_status
