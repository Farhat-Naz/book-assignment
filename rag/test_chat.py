"""
WebSocket test client for the RAG chatbot
"""
import asyncio
import websockets
import json


async def test_chat():
    """Test the chatbot with sample queries"""
    uri = "ws://localhost:8000/ws/chat"

    print("\n" + "="*60)
    print("RAG Chatbot Test Client")
    print("="*60)
    print(f"\nConnecting to: {uri}")

    try:
        async with websockets.connect(uri) as websocket:
            print("[OK] Connected to chatbot!\n")

            # Test queries
            test_queries = [
                "What is Physical AI?",
                "Tell me about sensors in robotics",
                "What is ROS2?",
            ]

            for i, query in enumerate(test_queries, 1):
                print(f"\n[Query {i}/{ len(test_queries)}] {query}")
                print("-" * 60)

                # Send query
                await websocket.send(json.dumps({"query": query}))

                # Receive response
                response = await websocket.recv()
                data = json.loads(response)

                if data.get("type") == "complete":
                    print(f"\n[Response]")
                    print(data.get("content", "No content"))

                    sources = data.get("sources", [])
                    if sources:
                        print(f"\n[Sources] ({len(sources)} results)")
                        for j, source in enumerate(sources[:3], 1):
                            score = source.get("score", 0)
                            src = source.get("source", "Unknown")
                            print(f"  {j}. {src} (score: {score:.3f})")

                elif data.get("type") == "error":
                    print(f"\n[ERROR] {data.get('error', 'Unknown error')}")

                print()

            print("="*60)
            print("[SUCCESS] All test queries completed!")
            print("="*60)

    except websockets.exceptions.ConnectionRefusedError:
        print("\n[ERROR] Could not connect to the server")
        print("        Make sure the server is running on http://localhost:8000")
    except Exception as e:
        print(f"\n[ERROR] {str(e)}")
        import traceback
        traceback.print_exc()


async def interactive_chat():
    """Interactive chat session with the RAG chatbot"""
    uri = "ws://localhost:8000/ws/chat"

    print("\n" + "="*60)
    print("Interactive RAG Chatbot")
    print("="*60)
    print(f"\nConnecting to: {uri}")

    try:
        async with websockets.connect(uri) as websocket:
            print("[OK] Connected! Type 'exit' to quit.\n")

            while True:
                # Get user input
                query = input("You: ").strip()

                if not query:
                    continue

                if query.lower() in ['exit', 'quit', 'bye']:
                    print("\n[INFO] Goodbye!")
                    break

                # Send query
                await websocket.send(json.dumps({"query": query}))

                # Receive response
                response = await websocket.recv()
                data = json.loads(response)

                if data.get("type") == "complete":
                    print(f"\nBot: {data.get('content', 'No content')}\n")

                    sources = data.get("sources", [])
                    if sources:
                        print(f"[Sources: {len(sources)} results]")
                        for j, source in enumerate(sources[:3], 1):
                            score = source.get("score", 0)
                            src = source.get("source", "Unknown")
                            print(f"  {j}. {src} (score: {score:.3f})")
                        print()

                elif data.get("type") == "error":
                    print(f"\n[ERROR] {data.get('error', 'Unknown error')}\n")

    except websockets.exceptions.ConnectionRefusedError:
        print("\n[ERROR] Could not connect to the server")
        print("        Make sure the server is running on http://localhost:8000")
    except Exception as e:
        print(f"\n[ERROR] {str(e)}")


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == "interactive":
        # Run interactive mode
        asyncio.run(interactive_chat())
    else:
        # Run test mode
        asyncio.run(test_chat())
