from rag import RAG

bot = RAG()

while True:

    question = input("\nASK: ")
    if question.lower() == "exit":
        break

    answer = bot.ask(question)
    print("\nAnswer\n")
    print(answer)