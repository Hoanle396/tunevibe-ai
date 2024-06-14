import surprise

from recommenders.utils.timer import Timer
import pandas as pd
from recommenders.models.surprise.surprise_utils import (
    predict,
)

from app.db import mydb


class Recommend(object):
    def __init__(self):
        self.svd =surprise.SVD(random_state=0, n_factors=200, n_epochs=30, verbose=True)
        self.df = pd.read_sql_query(sql="SELECT * FROM `vote`", con=mydb)
        self.df= self.df[["userId","musicId","rate"]]
        train_set = surprise.Dataset.load_from_df( df=self.df, reader=surprise.Reader("ml-100k")).build_full_trainset()
        with Timer() as train_time:
          self.svd.fit(train_set)

    def predict(self):
       predictions = predict(self.svd, self.df, usercol="userId", itemcol="musicId")
       return predictions



