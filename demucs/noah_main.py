from pathlib import PosixPath

import demucs.api
from argparse import Namespace

from demucs.api import Separator


def noah_main():
    print("noah main")
    #      Namespace(tracks=[PosixPath('NoahWithBackgroud.wav')], sig=None, name='htdemucs', repo=None, list_models=False, verbose=False, out=PosixPath('separated'), filename='{track}/{stem}.{ext}', device='cpu', shifts=1, overlap=0.25, split=True, segment=None, stem='vocals', other_method='add', int24=False, float32=False, clip_mode='rescale', flac=False, mp3=False, mp3_bitrate=320, mp3_preset=2, jobs=0)
    args = Namespace(tracks=[PosixPath('NoahWithBackgroud.wav')], sig=None, name='htdemucs', repo=None, list_models=False, verbose=False, out=PosixPath('separated'), filename='{track}/{stem}.{ext}', device='cpu', shifts=1, overlap=0.25, split=True, segment=None, stem="vocals", other_method='add', int24=False, float32=False, clip_mode='rescale', flac=False, mp3=False, mp3_bitrate=320, mp3_preset=2, jobs=0)
    separator = Separator(model=args.name,
                          repo=args.repo,
                          device=args.device,
                          shifts=args.shifts,
                          split=args.split,
                          overlap=args.overlap,
                          progress=True,
                          jobs=args.jobs,
                          segment=args.segment)
    origin, separated = separator.separate_audio_file(args.tracks[0])
    print("finished")
    for file, sources in separated:
        for stem, source in sources.items():
            demucs.api.save_audio(source, f"WAlla{stem}_{file}", samplerate=separator.samplerate)

    print("finished saving")