import os, pathlib

p = r"C:\enumera"
for i, a in enumerate(os.listdir(p)):
    antigo = os.path.join(p, a)
    sufixo = pathlib.Path(antigo).suffix
    novo = os.path.join(
        p,
        f"""{str(i)
                .zfill(6)}{sufixo}""",
    )
    os.rename(antigo, novo)
