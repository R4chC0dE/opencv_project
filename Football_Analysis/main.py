from utils.video_utils import read_video, save_video
from trackers.tracker import Tracker

def main():
    # read video 
    video_frames = read_video('input_videos/08fd33_4.mp4')

    # initialise tracker
    tracker = Tracker('models/best.pt')

    tracks = tracker.get_object_tracks(video_frames)
    # Save video
    save_video(video_frames, 'output_videos/output_video.avi')

if __name__ == '__main__':
    main()