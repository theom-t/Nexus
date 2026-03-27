import chromadb
import os
import datetime

class VectorMemory:
    """
    Long-term project memory using ChromaDB.
    Enables NEXUS to 'remember' past projects and logic.
    """
    def __init__(self, db_path: str = "/home/tmainetucker/Repos/nexus/data/vector_db"):
        self.db_path = db_path
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
        self.client = chromadb.PersistentClient(path=self.db_path)
        self.collection = self.client.get_or_create_collection(name="nexus_mental_state")

    def remember(self, project_name: str, content: str, metadata: dict = None):
        """
        Stores a piece of information or strategy into long-term memory.
        """
        timestamp = datetime.datetime.now().isoformat()
        doc_id = f"{project_name}_{timestamp}"
        
        meta = metadata or {}
        meta["project"] = project_name
        meta["timestamp"] = timestamp
        
        self.collection.add(
            documents=[content],
            metadatas=[meta],
            ids=[doc_id]
        )

    def recall(self, query: str, n_results: int = 3) -> str:
        """
        Searches memory for information relevant to the current task.
        """
        results = self.collection.query(
            query_texts=[query],
            n_results=n_results
        )
        
        if not results['documents'][0]:
            return "No relevant past memories found."
            
        memory_block = "--- NEXUS LONG-TERM MEMORY (RELEVANT PAST INSIGHTS) ---\n"
        for i, doc in enumerate(results['documents'][0]):
            project = results['metadatas'][0][i].get('project', 'Unknown')
            memory_block += f"[From Project: {project}]:\n{doc}\n\n"
        return memory_block

if __name__ == "__main__":
    # Quick test
    memory = VectorMemory()
    memory.remember("Nexus_CORE", "We used absolute paths to fix sqlite3 OperationalErrors.")
    print("Testing recall on 'OperationalError'...")
    print(memory.recall("How did we fix the sqlite errors?"))
