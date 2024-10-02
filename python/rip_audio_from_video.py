import argparse
from moviepy.editor import VideoFileClip


def extract_audio(video_file, audio_file):
    # Load the video file
    video_clip = VideoFileClip(video_file)

    # Extract the audio
    audio_clip = video_clip.audio

    # Write the audio to a file
    audio_clip.write_audiofile(audio_file)

    # Close the clips
    audio_clip.close()
    video_clip.close()


def main():
    # Set up command-line argument parsing
    parser = argparse.ArgumentParser(description="Extract audio from a video file.")
    parser.add_argument("video_file", help="Path to the input video file")
    parser.add_argument("audio_file", help="Path to the output audio file")

    args = parser.parse_args()

    extract_audio(args.video_file, args.audio_file)


if __name__ == "__main__":
    main()
