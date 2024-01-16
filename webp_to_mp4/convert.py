import os
import shutil
import tempfile
import argparse
from moviepy.video.io.ImageSequenceClip import ImageSequenceClip
import PIL.Image

def analyse_image(path):
    im = PIL.Image.open(path)
    results = {
        'size': im.size,
        'mode': 'full',
    }
    try:
        while True:
            if im.tile:
                tile = im.tile[0]
                update_region = tile[1]
                update_region_dimensions = update_region[2:]
                if update_region_dimensions != im.size:
                    results['mode'] = 'partial'
                    break
            im.seek(im.tell() + 1)
    except EOFError:
        pass
    return results

def process_image(path, temp_dir):
    images = []
    mode = analyse_image(path)['mode']

    im = PIL.Image.open(path)

    i = 0
    p = im.getpalette()
    last_frame = im.convert('RGBA')

    try:
        while True:
            basename = os.path.basename(path)
            output_folder = temp_dir
            frame_file_name = os.path.join(output_folder, f'{os.path.splitext(basename)[0]}-{i}.png')
        
            print(f"saving {path} ({mode}) frame {i}, {im.size} {im.tile} to {frame_file_name}")

            if '.gif' in path:
                if not im.getpalette():
                    im.putpalette(p)

            new_frame = PIL.Image.new('RGBA', im.size)

            if mode == 'partial':
                new_frame.paste(last_frame)

            new_frame.paste(im, (0, 0), im.convert('RGBA'))
           
            new_frame.save(frame_file_name, 'PNG')
            images.append(frame_file_name)
            i += 1
            last_frame = new_frame
            im.seek(im.tell() + 1)
    except EOFError:
        pass
    return images

def webp_mp4(input_file, output_file=None, fps=20):
    temp_dir = tempfile.mkdtemp()
    try:
        images = process_image(input_file, temp_dir)
        if output_file is None:
            output_file = os.path.splitext(input_file)[0] + '.mp4'
        clip = ImageSequenceClip(images, fps=fps)
        clip.write_videofile(output_file)
        return [output_file]
    finally:
        shutil.rmtree(temp_dir)

def parse_arguments():
    parser = argparse.ArgumentParser(description="Convert WEBP to MP4")
    parser.add_argument("input_file", help="Input file name (.webp)")
    parser.add_argument("-o", "--output_file", help="Output file name (optional)")
    parser.add_argument("--fps", type=int, default=20, help="Frames per second (default: 20)")

    return parser.parse_args()

if __name__ == "__main__":
    args = parse_arguments()
    webp_mp4(args.input_file, args.output_file, args.fps)
