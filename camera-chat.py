from vidstream import CameraClient
from vidstream import StreamingServer

import threading
import time

receiving = StreamingServer('95.2.8.103', 9999)
sending = CameraClient('176.219.193.172', 9999)

t1 = threading.Thread(target = receiving.start_server)
