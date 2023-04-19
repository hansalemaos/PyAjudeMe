# https://www.youtube.com/watch?v=3Q_oYDQ2whs
p1 = [['9:00', '10:30'], ['12:00', '13:00'],
      ['16:00', '18:00']]
p1off = [['0:00', '9:00'], ['20:00', '24:00']]
p2 = [['10:00', '11:30'], ['12:30', '14:30'],
      ['14:30', '15:00'], ['16:00', '17:00']]
p2off = [['0:00', '10:00'], ['18:30', '24:00']]
import numpy as np
import itertools

# No need to separate the schedules
l = list(itertools.chain(p1, p1off, p2, p2off))
# convert to int
li = [[list(map(int, y.split(':'))) for y in z]
      for z in l]
# convert to minutes
lm=[(o[0][0]*60+o[0][1],o[1][0]*60+o[1][1])
    for o in li]
# calculate every minute not available
ln = np.sort(np.unique(np.concatenate(
[np.arange(*o) for o in lm])))
# getting all free minutes
lf =np.nonzero(~np.in1d(np.arange(24*60),
                        ln))[0]
# where does each interval stop
liv  = np.diff(lf)
# split to get each interval
lc=np.array_split(lf,np.where(liv>1)[0]+1)
lc=[_ for _ in np.array_split(lf,
np.where(liv>1)[0]+1) if len(_)>=30]
# format the array
r=np.char.array([
np.array([divmod(u[0],60),
divmod(u[-1],60)])
for u in lc]).astype('U').zfill(2)

