# version 1.0

# import cv2
# import numpy as np
# x = input("Enter Path (q to quit) : ")
# capture = cv2.VideoCapture(f"{x}")
#
# if (capture.isOpened()==False):
#     print("ERROR")
#
# while(capture.isOpened()):
#     ret,frame=capture.read()
#     if ret == True:
#         cv2.imshow("STREIN PLAYER", frame)
#         if cv2.waitKey(25) & 0xFF==ord('q'):
#             break
#     else:
#         break
# capture.release()
# cv2.destroyAllWindows()

# version 2.0

import cv2
import numpy as np
from ffpyplayer.player import MediaPlayer
x = input("Enter Path (q to quit) : ")
video_path = (f"{x}")
def PlayVideo(video_path):
    video=cv2.VideoCapture(video_path)
    player = MediaPlayer(video_path)
    while True:
        grabbed, frame=video.read()
        audio_frame, val = player.get_frame()
        if not grabbed:
            print("End of video")
            break
        if cv2.waitKey(28) & 0xFF == ord("q"):
            break
        cv2.imshow("STREIN Media PLAYER", frame)
        if val != 'eof' and audio_frame is not None:
            #audio
            img, t = audio_frame
    video.release()
    cv2.destroyAllWindows()
PlayVideo(video_path)


















