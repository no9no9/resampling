# resampling

-f:[audio path list]

-o:[output dir]

-s:[sampling rate]

# useage
```sh
ls [waves/dir/path]/*.wav > list.txt
python resampling.py -f list.txt -o [waves/out/dir/path] -sr_out 16000
```