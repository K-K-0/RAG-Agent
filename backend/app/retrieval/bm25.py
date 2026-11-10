import pickle


class BM25Search:

    from pathlib import Path

    BASE_DIR = Path(__file__).resolve().parents[1]
    INDEX_PATH = BASE_DIR / "storage" / "bm25.pkl"


    @classmethod
    def load(cls):

        with open(cls.INDEX_PATH, "rb") as f:

            return pickle.load(f)