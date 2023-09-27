from ..frame_x_integration import FrameXController

class BisectionSearch:

    def __init__(self, video_name: str):
        self.controller = FrameXController(video_name)
        self.low = 0
        self.high = 61696

    def get_mid_frame(self) -> int:
        return (self.low + self.high) // 2

    def retrieve_frame(self, frame_number: int) -> dict:
        return self.controller.get_frame(frame_number)

    def update_bounds(self, rocket_launched: bool):
        mid = self.get_mid_frame()
        if rocket_launched:
            self.high = mid
        else:
            self.low = mid + 1
