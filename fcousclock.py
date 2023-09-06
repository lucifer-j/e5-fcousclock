import time
import winsound  # 用于播放声音（仅适用于Windows）

def focus_timer(work_time, break_time):
    while True:
        print("工作时间（分钟）: " + str(work_time))
        for _ in range(work_time * 60, 0, -1):
            time.sleep(1)
        play_sound()  # 播放提醒声音
        print("休息时间（分钟）: " + str(break_time))
        for _ in range(break_time * 60, 0, -1):
            time.sleep(1)
        play_sound()  # 播放提醒声音

def play_sound():
    frequency = 1000  # 声音频率（Hz）
    duration = 1000  # 声音持续时间（毫秒）
    winsound.Beep(frequency, duration)

if __name__ == "__main__":
    work_time = int(input("输入工作时间（分钟）: "))
    break_time = int(input("输入休息时间（分钟）: "))
    focus_timer(work_time, break_time)
