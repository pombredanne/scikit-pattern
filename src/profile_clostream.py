from clostream import CloStream
import pandas as pd

columns = ['song_id','user_id', 'artist_id', 'provider_id', 'ip']
df = pd.read_csv('listen-20131115.log', names=columns).head(10000)

cs = CloStream()
cs.add_df(df)
