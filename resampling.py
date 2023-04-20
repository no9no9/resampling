import numpy as np
import os
import librosa
import soundfile
import argparse


def main(files_list,outdir_path,out_sr,out_dtype):
    files_num = len(files_list)
    for num,file in enumerate(files_list):
        data, sr = librosa.load(file,sr=None,mono=True)
        data = librosa.resample(y=data,orig_sr=sr, target_sr=out_sr)
        
        file_name = os.path.splitext(os.path.basename(file))[0]
        write_path = os.path.join(outdir_path,'{}_resample.wav'.format(file_name))
        soundfile.write(write_path,data,out_sr,subtype=out_dtype)
        print(f'{num}/{files_num}: {write_path}')
    return 0


def files_to_list(files_path):
    with open(files_path, encoding='utf-8') as f:
        files = f.readlines()
    files = [f.rstrip() for f in files]
    return files

if __name__=="__main__":
    parse = argparse.ArgumentParser()
    parse.add_argument('-f', '--files_list',type=str, required=True)
    parse.add_argument('-o', '--outdir_path',type=str, required=True)
    parse.add_argument('-sr_out','--sampling_rate_output',type=int, required=True)
    parse.add_argument('-d','--output_datatype' , type=str, default='PCM_16')
    
    args = parse.parse_args()
    
    if not os.path.isdir(args.outdir_path):
        os.makedirs(args.outdir_path)
        os.chmod(args.outdir_path,0o775)
        
    files_list = files_to_list(args.files_list)
    outdir_path = args.outdir_path
    
    main(files_list, outdir_path,args.sampling_rate_output,args.output_datatype)
    


    
