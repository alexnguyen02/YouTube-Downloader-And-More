import csv
from typing import Any

from src.download_video import download_video
from src.get_video_info import get_video_info


def download_from_file(read_file: str, write_file: str) -> Any:
    """Read the given csv file, download the YouTube video(s) from the url,
    and write the relevant info into another csv file
    """
    with open(read_file, mode='r') as csv_file:
        reader = csv.reader(csv_file)
        header = next(reader)
        artist_name = header[0]

        video_type = ''
        downloaded_vid = 0
        unavailable_vid = 0

        with open(write_file, mode='w') as output_file:
            writer = csv.writer(output_file)

            for row in reader:
                if row[0] == "type":
                    video_type = row[1]
                    writer.writerow([row[1]])

                else:
                    url = str(row[0])
                    download_status = download_video(url, f"{artist_name}/{video_type}")
                    video_info = get_video_info(url, download_status)
                    if video_info == "Video is unavailable":
                        unavailable_vid += 1
                        pass
                    else:
                        downloaded_vid += 1

                    writer.writerow(video_info)

    print("Download completed!")
    return f"Total downloaded videos: {downloaded_vid}, Unavailable videos: {unavailable_vid}"
