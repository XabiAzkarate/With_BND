from urllib.parse import urljoin


class FrameXController():

    BASE_URL = 'http://framex-dev.wadrid.net/api/'
    GET_FRAME_ENDPOINT = 'video/{video_name}/frame/{frame_number}/'

    def __init__(self, video_name: str):
        self._video_name = video_name

    def get_frame(self, frame_number):
        response_data =  urljoin(self.BASE_URL, self.GET_FRAME_ENDPOINT.format(video_name=self._video_name, frame_number=frame_number))
        print(response_data)
        return response_data
    