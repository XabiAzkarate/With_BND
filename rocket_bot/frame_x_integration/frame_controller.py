from .frame_api_client import FrameXApiClient


class FrameXController():

    def __init__(self, video_name: str):
        self._api_client = FrameXApiClient(video_name)

    def get_frame(self, frame):
        return self._api_client.get_frame(frame)
    