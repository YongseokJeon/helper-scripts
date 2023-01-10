#! /bin/bash

function print_help {
  echo ''
  echo 'Usage: ys_play <width> <height> <filename>'
  echo '  - <width> : width of video'
  echo '  - <height> : height of video'
  echo '  - <filename> : name of file'
  echo '  (optional) - <framerate> : framerate'
  echo ''
}

if [ $# -lt 3 ]; then
  echo ' (!) -- Invalid parameter (input params:'"$#"')'
  print_help
  exit 1
fi

width=$1
height=$2
filename=$3
if [ -z "$4" ]; then
  framerate=5
else
  framerate=$4
fi

echo "ffplay -f rawvideo -pixel_format yuv420p -video_size ${width}x${height} -framerate ${framerate} -i ${filename}"
ffplay -f rawvideo -pixel_format yuv420p -video_size ${width}x${height} -framerate ${framerate} -i ${filename}
