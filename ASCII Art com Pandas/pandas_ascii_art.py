import cv2
import pandas as pd
im = cv2.imread(
    r'C:\Users\Gamer\Pictures\2023-01-12 08_59_14-anitta - Google Search.png',
    cv2.IMREAD_GRAYSCALE
)
df = pd.DataFrame(im)
letters = "'X.G "
df4 = df.copy()
for i,l in enumerate(letters):
    end = (
        int(i*350/len(letters))
    )
    start = (
        int(end-350/len(letters))
    )
    for c in df.columns:
        (
            df4.loc[
                (df[c] > start) &
                (df[c] <= end),
                c
            ]
        ) = l
print(df4.to_string(
    index=False,
    header=[' '] * df4.shape[1],
    max_colwidth=1
))