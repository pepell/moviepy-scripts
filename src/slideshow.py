# -*- coding: utf-8 -*-

from moviepy.editor import *

IMG_FOLDER = '../img'
SIZE = (1280, 720)
clip_list = []
with open('../conf/slideshow_img_list.txt', 'r') as f:
    for line in f.readlines():
        img_data = line[:-1].split(';')
        name = img_data[0]
        duration = float(img_data[1])
        print('Processing {}/{} - Duration {} seconds'.format(IMG_FOLDER, name, duration))
        clip = ImageClip('{}/{}'.format(IMG_FOLDER, name)).set_duration(duration)
        resized_clip = clip.resize(SIZE)
        clip_list.append(resized_clip)
    
fadein_videos = [CompositeVideoClip([clip.fx(transfx.crossfadein, 1)]) for clip in clip_list]
fadeout_videos = [CompositeVideoClip([clip.fx(transfx.crossfadeout, 1)]) for clip in fadein_videos]
video = concatenate(fadeout_videos)
video.write_videofile('out.mp4', fps=24)

