from sklearn.base import TransformerMixin
from sklearn.base import BaseEstimator
from sklearn.pipeline import Pipeline
from sklearn.pipeline import make_pipeline


class FooTransformer(TransformerMixin):
    def __init__(self, number):
        self.number = number

    def fit(self, X, y=None):
        print("Transformer No.{}: fit X={}".format(self.number, X))
        return self

    def transform(self, X):
        print("Transformer No.{}: transform X={} => X+10={}".format(self.number, X, X+10))
        return X+10


class BarEstimator(BaseEstimator):
    def __init__(self, number):
        self.number = number

    def fit(self, X, y=None):
        print("Estimator No.{}: fit X={}".format(self.number, X))
        return self

    def predict(self, X):
        print("Estimator No.{}: predict X={} is...".format(self.number, X))
        return 0


if __name__ == '__main__':
    p1 = Pipeline(steps=[("Trans1", FooTransformer(1)),
                         ("Trans2", FooTransformer(2)),
                         ("Estmt1", BarEstimator(1))])
    print(p1)
    p2 = make_pipeline(FooTransformer(1), FooTransformer(2), BarEstimator(1))
    print(p2)
    #print("#===== Pipeline 1 fitting =====#")
    #p1.fit(X=100)
    #print("#===== Pipeline 1 predicting =====#")
    #pred = p1.predict(X=100)
    #print(pred)

#Transformer No.1: fit X=100
#Transformer No.1: transform X=100 => X+10=110
#Transformer No.2: fit X=110
#Transformer No.2: transform X=110 => X+10=120
#Estimator No.1: fit X=120
#===== Pipeline 1 predicting =====#
#Transformer No.1: transform X=100 => X+10=110
#Transformer No.2: transform X=110 => X+10=120
#Estimator No.1: predict X=120 is...


