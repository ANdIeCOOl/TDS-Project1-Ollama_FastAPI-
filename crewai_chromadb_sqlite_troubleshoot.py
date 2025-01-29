
# import chromadb

# client = chromadb.Client()
# # Create collection. get_collection, get_or_create_collection, delete_collection also available!
# collection = client.create_collection("all-my-documents")

# # Add docs to the collection. Can also update and delete. Row-based API coming soon!
# collection.add(
#     documents=["This is document1", "This is document2"], # we handle tokenization, embedding, and indexing automatically. You can skip that and add your own embeddings as well
#     metadatas=[{"source": "notion"}, {"source": "google-docs"}], # filter on these!
#     ids=["doc1", "doc2"],) # unique for each doc
# collection2 = client.get_collection(name="all-my-documents")
# results = collection2.get(ids=["page"])["documents"]
# print(results) # Not found []


# import os
# import autogen
# from autogen import AssistantAgent, UserProxyAgent
# print("hello")


