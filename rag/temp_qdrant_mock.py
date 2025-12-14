"""
Temporary in-memory mock for Qdrant during development
"""
import uuid
from typing import List, Dict, Any, Optional
from dataclasses import dataclass
from types import SimpleNamespace

@dataclass
class MockPoint:
    id: str
    vector: List[float]
    payload: Dict[str, Any]

class MockQdrantClient:
    """Mock Qdrant client for development without running Qdrant server"""
    
    def __init__(self):
        self.collections = {}
        self.points = {}
    
    def create_collection(self, collection_name: str, vectors_config):
        """Create a mock collection"""
        self.collections[collection_name] = {
            'vectors_config': vectors_config,
            'points': []
        }
        self.points[collection_name] = []
        print(f"Created mock collection: {collection_name}")
    
    def upsert(self, collection_name: str, points: List[MockPoint]):
        """Mock upsert operation"""
        if collection_name not in self.points:
            self.points[collection_name] = []
        
        for point in points:
            # Remove existing point with same ID if exists
            self.points[collection_name] = [
                p for p in self.points[collection_name] if p.id != point.id
            ]
            # Add the new point
            self.points[collection_name].append(point)
        
        print(f"Upserted {len(points)} points to mock collection: {collection_name}")
    
    def search(self, collection_name: str, query_vector: List[float], limit: int, score_threshold: float = None, filter=None):
        """Mock search operation using cosine similarity"""
        if collection_name not in self.points:
            return []
        
        # Calculate cosine similarity
        def cosine_similarity(v1: List[float], v2: List[float]) -> float:
            dot_product = sum(a * b for a, b in zip(v1, v2))
            magnitude1 = sum(a * a for a in v1) ** 0.5
            magnitude2 = sum(b * b for b in v2) ** 0.5
            if magnitude1 == 0 or magnitude2 == 0:
                return 0
            return dot_product / (magnitude1 * magnitude2)
        
        # Calculate scores for all points
        scored_points = []
        for point in self.points[collection_name]:
            similarity = cosine_similarity(query_vector, point.vector)
            if score_threshold is None or similarity >= score_threshold:
                scored_points.append((similarity, point))
        
        # Sort by similarity (descending) and take top 'limit'
        scored_points.sort(key=lambda x: x[0], reverse=True)
        top_points = scored_points[:limit]
        
        # Convert to the format expected by the real Qdrant client
        from types import SimpleNamespace
        results = []
        for score, point in top_points:
            result = SimpleNamespace()
            result.id = point.id
            result.score = score
            result.payload = point.payload
            results.append(result)
        
        return results
    
    def get_collection(self, collection_name: str):
        """Mock get collection info"""
        if collection_name in self.collections:
            return SimpleNamespace(
                vectors_count=len(self.points.get(collection_name, [])),
                points_count=len(self.points.get(collection_name, [])),
                status="green"
            )
        else:
            raise Exception(f"Collection {collection_name} not found")

    def get_collections(self):
        """Mock get all collections"""
        collection_list = []
        for name in self.collections.keys():
            collection_list.append(SimpleNamespace(name=name))
        return SimpleNamespace(collections=collection_list)

    def delete_collection(self, collection_name: str):
        """Mock delete collection"""
        if collection_name in self.collections:
            del self.collections[collection_name]
            del self.points[collection_name]
            print(f"Deleted mock collection: {collection_name}")

# Create a global instance
mock_client = MockQdrantClient()