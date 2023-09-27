from apiclient import APIClient
from urllib.parse import urljoin

class FrameXApiClient(APIClient):

    BASE_URL = 'http://framex-dev.wadrid.net/api/'
    GET_FRAME_ENDPOINT = 'video/{video_name}/frame/{frame}/'
    
    def __init__(self, video_name: str, rate_limit_lock=None, encoding='utf8'):
        super().__init__(rate_limit_lock, encoding)
        self._video_name = video_name

    def get_frame(self, frame_number: int):
        endpoint = urljoin(self.BASE_URL, self.GET_FRAME_ENDPOINT.format(video_name=self._video_name, frame=frame_number))
        try:
            return self.call(endpoint)
        except Exception as e:
            # Handle or log the exception as needed
            print(f"Error fetching frame: {e}")
            return {}
