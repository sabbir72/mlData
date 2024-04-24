import glob
import subprocess

file_list = []
cam_wise_video_list = []

def camera_list(cam_list_path):

    for file in cam_list_path:
        file_list.append(file.split("/")[-1].split("_")[0])
    return file_list


def cam_video_list(video_file_list,cam_id):

    for f in video_file_list:
       chk = f.split("/")[-1].split(cam_id)
       if len(chk)>1:
        cam_wise_video_list.append(f)

    return cam_wise_video_list


if __name__ =='__main__':

    parent_dir = "line3/"
    
    video_list = glob.glob(parent_dir + "*.mp4")
    video_list =  sorted(video_list, key=lambda x: int(x.split("/")[-1].split(".mp4")[0].split("_")[-1]), reverse=False)

    cam_list = set(camera_list(video_list))
    cam_list = sorted(cam_list, key=lambda x: int(x.split("D")[-1]), reverse=False)

    for i in video_list:

        print(f"file {cam_list[0]}.mp4\n", end=' ')
    print("\n")
       


    #print(subprocess.run(["/path/to/your/shell/script","arguments"], shell = True))
