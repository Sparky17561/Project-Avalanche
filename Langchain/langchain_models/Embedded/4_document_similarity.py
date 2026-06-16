from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
load_dotenv()

embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

document = [
    "Delhi is the capital of India.",
    "Mumbai is known as the financial capital of India.",
    "The Taj Mahal is located in Agra.",
    "Bangalore is famous for its IT industry.",
    "Jaipur is called the Pink City of India."
]

print("Enter query")
query = input()

doc_embeddings = embedding.embed_documents(document) # this is a costly operation so u have to store it somewhere in db .. which is vector DB
query_embedding = embedding.embed_query(query)

print(cosine_similarity([query_embedding],doc_embeddings))

scores = cosine_similarity([query_embedding],doc_embeddings)[0]

print(sorted(list(enumerate(scores)),key=lambda x:x[1])[-1])

index,score = sorted(list(enumerate(scores)),key=lambda x:x[1])[-1]

print(query)
print(document[index])

print("similarity score is: ", score)

