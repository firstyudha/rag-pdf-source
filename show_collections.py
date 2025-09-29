import chromadb

# Path to the directory containing your ChromaDB data.
CHROMA_PATH = "./chroma"

def list_collections():
    """Connects to ChromaDB and lists all available collections."""
    try:
        # Initialize the persistent client
        client = chromadb.PersistentClient(path=CHROMA_PATH)
        
        # List all collections
        collections = client.list_collections()
        
        if collections:
            print("Found the following collections:")
            for col in collections:
                print(f"- {col.name}")
        else:
            print("No collections found in the database.")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    list_collections()