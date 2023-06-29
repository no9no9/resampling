import numpy as np
import os
import librosa
import soundfile
import argparse
import tqdm

def resampling(files_list,outdir_path,out_sr,out_dtype='PCM_16', add=''):
    files_num = len(files_list)
    for num,file in tqdm.tqdm(enumerate(files_list)):
        data, sr = librosa.load(file,sr=None,mono=True)
        data = librosa.resample(y=data,orig_sr=sr, target_sr=out_sr)
        file_name = os.path.splitext(os.path.basename(file))[0]
        write_path = os.path.join(outdir_path,f'{file_name}{add}.wav')
        soundfile.write(write_path,data,out_sr,subtype=out_dtype)
        print(f'\r{num}/{files_num}: {write_path}', end='')
    return 0

def files_to_list(files_path):
    with open(files_path, encoding='utf-8') as f:
        files = f.readlines()
    files = [f.rstrip() for f in files]
    return files

if __name__=="__main__":
    parse = argparse.ArgumentParser()
    parse.add_argument('-f', '--files_list',type=str, required=True)
    parse.add_argument('-o', '--outdir_path',type=str, default='./resampling/output/', required=True)
    parse.add_argument('-s','--sampling_rate_output',type=int, required=True)
    parse.add_argument('-d','--output_dtype' , type=str, default='PCM_16')
    parse.add_argument('-T','--text_add', type=str, default='')
    args = parse.parse_args()
    
    os.makedirs(args.outdir_path, exist_ok=True)
    os.chmod(args.outdir_path,0o775)
    
    files_list = files_to_list(args.files_list)
    outdir_path = args.outdir_path
    sr = args.sampling_rate_output
    dtype = args.output_dtype
    text_add = args.text_add
    
    resampling(files_list, outdir_path, sr, dtype, text_add)
    


    
