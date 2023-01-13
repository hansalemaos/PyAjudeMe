import glob, pathlib, os
pasta=r'C:\Users\Gamer\Documents\Downloads'
pasta_a = (
    glob.glob(f'{pasta}\\*.*')
)
for a in pasta_a:
    if not os.path.isfile(a):
        continue
    sufixo=(
        pathlib
        .Path(a)
        .suffix
        .strip('.')
    )
    if sufixo == '':
        continue
    novap = (
        os.path.join(pasta, sufixo)
    )
    arq = a.split('\\')[-1]
    if not os.path.exists(novap):
        os.makedirs(novap)
    narq = (
        os.path.join(novap, arq)
    )
    os.rename(a,narq)