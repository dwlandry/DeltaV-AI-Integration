# Document Indexing and Embeddings

Approach:
- Use a text embedding model (e.g., OpenAI’s `text-embedding-ada-002` or a local model).
- Break content into chunks (~512-1024 tokens).
- Generate embeddings and store in a vector DB (e.g., Chroma or Pinecone).

See:
- [[Metadata-Tagging]] for enhanced retrieval.
