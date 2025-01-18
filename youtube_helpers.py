from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import NoTranscriptFound, VideoUnavailable

def get_youtube_transcript(video_id):
    """
    Retrieves the transcript of a YouTube video using the youtube-transcript-api library.

    Args:
        video_id (str): The ID of the YouTube video.

    Returns:
        str: A single string containing the transcript with sentences.

    Raises:
        Exception: If no transcript is found or the video is unavailable.
    """
    try:
        # Fetch the transcript
        transcript = YouTubeTranscriptApi.get_transcript(video_id)

        # Join the transcript into a single string
        transcript_text = " ".join([item['text'] for item in transcript])
        return transcript_text

    except NoTranscriptFound:
        raise Exception("Transcript not available for this video.")
    except VideoUnavailable:
        raise Exception("The video is unavailable or the ID is invalid.")
    except Exception as e:
        raise Exception(f"An error occurred: {str(e)}")
