import pickle


class BM25Search:

    INDEX_PATH = "storage/bm25.pkl"


    @classmethod
    def load(cls):

        with open(cls.INDEX_PATH, "rb") as f:

            return pickle.load(f)