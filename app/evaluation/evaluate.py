from app.retrieval.retriever import retrieve

TEST_SET = [
    {"question": "What is RAG?", "expected_keyword": "retrieval"},
    {"question": "What does a vector database store?", "expected_keyword": "embedding"},
]

def evaluate() -> float:
    hits = 0
    for case in TEST_SET:
        docs = retrieve(case["question"])
        found = any(case["expected_keyword"].lower() in d["text"].lower() for d in docs)
        hits += found
        print(f"{'PASS' if found else 'FAIL'} - {case["question"]}")
    score = hits / len(TEST_SET)
    print(f"Retrieval hit rate: {score:.0%}")
    return score

if __name__ == "__main__":
    evaluate()