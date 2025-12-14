"""
Test script to verify Chapter 4 is loaded in the RAG chatbot
"""
import asyncio
import websockets
import json


async def test_chapter4():
    """Test queries related to Chapter 4 content"""
    uri = "ws://localhost:8000/ws/chat"

    print("\n" + "="*60)
    print("Testing Chapter 4: Motion Planning & Control")
    print("="*60)
    print(f"\nConnecting to: {uri}")

    try:
        async with websockets.connect(uri) as websocket:
            print("[OK] Connected to chatbot!\n")

            # Test queries about Chapter 4
            test_queries = [
                "What is motion planning?",
                "Tell me about A* algorithm",
                "What is RRT in robotics?",
                "Explain PID control",
            ]

            for i, query in enumerate(test_queries, 1):
                print(f"\n[Query {i}/{len(test_queries)}] {query}")
                print("-" * 60)

                # Send query
                await websocket.send(json.dumps({"query": query}))

                # Receive response
                response = await websocket.recv()
                data = json.loads(response)

                if data.get("type") == "complete":
                    content = data.get("content", "No content")
                    sources = data.get("sources", [])

                    # Check if response mentions Chapter 4
                    if "chapter-4" in str(sources).lower() or "motion" in content.lower():
                        print("[SUCCESS] Found Chapter 4 content!")
                    else:
                        print("[INFO] Response may not be from Chapter 4")

                    print(f"\n[Response Preview]")
                    print(content[:300] + "..." if len(content) > 300 else content)

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
            print("[COMPLETE] Chapter 4 verification finished!")
            print("="*60)

    except websockets.exceptions.ConnectionRefusedError:
        print("\n[ERROR] Could not connect to the server")
        print("        Make sure the server is running on http://localhost:8000")
    except Exception as e:
        print(f"\n[ERROR] {str(e)}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    asyncio.run(test_chapter4())
