from agents import research

def main():
    print("=== Multi-Agent Research Assistant ===")
    print("Type 'exit' to quit\n")
    
    while True:
        query = input("Enter your research query: ")
        
        if query.lower() == "exit":
            print("Goodbye!")
            break
            
        print("\nResearching...\n")
        result = research(query)
        print(f"Answer: {result}\n")
        print("-" * 50)

if __name__ == "__main__":
    main()