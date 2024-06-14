import surprise

from recommenders.utils.timer import Timer
import pandas as pd
from recommenders.models.surprise.surprise_utils import (
    predict,
)

from app.db import mydb
df = pd.read_sql_query(sql="SELECT * FROM `vote`", con=mydb)
df= df[["userId","musicId","rate"]]


class Recommend(object):
    def __init__(self):
        self.svd =surprise.SVD(random_state=0, n_factors=200, n_epochs=30, verbose=True)
       
        train_set = surprise.Dataset.load_from_df( df=df, reader=surprise.Reader("ml-100k")).build_full_trainset()
        with Timer() as train_time:
          self.svd.fit(train_set)

    def predict(self):
       predictions = predict(self.svd, df, usercol="userId", itemcol="musicId")
       return predictions



