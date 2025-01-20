from moviepy import *

import numpy as np


def create_animated_text(text="Hello World!", duration=5, fps=30):
    # Create a background
    background = ColorClip(size=(1920, 1080), color=(0, 0, 0))
    background = background.with_duration(duration)

    # get path to default font of the system
    font = "/usr/share/fonts/truetype/noto/NotoSans-Bold.ttf"

    # Create the text clip without a font parameter
    text_clip = TextClip(
        font=font, text=text, color="white", font_size=70
    )  # Removed font parameter

    # Set the clip duration
    text_clip = text_clip.with_duration(duration)

    # Define the movement function
    def move_text(t):
        # Start position (center of screen)
        start_x = 1920 / 2 - text_clip.w / 2
        start_y = 1080 / 2 - text_clip.h / 2

        # Add slight floating movement using sine wave
        y_offset = np.sin(t * 2 * np.pi) * 20

        return (start_x, start_y + y_offset)

    # Apply the movement
    text_clip = text_clip.with_position(move_text)

    # Combine background and text
    final_clip = CompositeVideoClip([background, text_clip])

    return final_clip


def main():
    # Create the animation
    video = create_animated_text(
        text="Welcome to Python Animation!", duration=5, fps=30
    )

    # Write the video file
    video.write_videofile("animated_text.mp4", fps=30, codec="libx264", audio=False)


if __name__ == "__main__":
    main()
