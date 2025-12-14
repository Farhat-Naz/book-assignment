"""
Document loader module for processing course materials and books
Supports multiple formats: PDF, TXT, DOCX, MD, etc.
"""
import os
import asyncio
from pathlib import Path
from typing import List, Dict, Any
from abc import ABC, abstractmethod
import logging

logger = logging.getLogger(__name__)

# Import based on available packages
try:
    import PyPDF2
except ImportError:
    PyPDF2 = None

try:
    from docx import Document
except ImportError:
    Document = None

try:
    from langchain.document_loaders import TextLoader, UnstructuredMarkdownLoader
except ImportError:
    TextLoader = None
    UnstructuredMarkdownLoader = None


class DocumentLoader(ABC):
    """Abstract base class for document loaders"""
    
    @abstractmethod
    async def load_documents(self, path: str) -> List[Dict[str, Any]]:
        """Load documents from specified path asynchronously"""
        pass


class PDFLoader(DocumentLoader):
    """PDF document loader"""
    
    async def load_documents(self, path: str) -> List[Dict[str, Any]]:
        """Load and extract text from PDF files"""
        if PyPDF2 is None:
            raise ImportError("PyPDF2 is required to load PDF files. Install with: pip install PyPDF2")
        
        documents = []
        
        # Handle single file or directory
        file_paths = []
        if os.path.isfile(path):
            file_paths = [path]
        elif os.path.isdir(path):
            file_paths = [os.path.join(path, f) for f in os.listdir(path) if f.lower().endswith('.pdf')]
        
        for pdf_path in file_paths:
            try:
                with open(pdf_path, 'rb') as file:
                    pdf_reader = PyPDF2.PdfReader(file)
                    text_content = ""
                    
                    for page_num, page in enumerate(pdf_reader.pages):
                        text_content += page.extract_text() + "\n"
                    
                    documents.append({
                        "content": text_content,
                        "metadata": {
                            "source": pdf_path,
                            "format": "pdf",
                            "page_count": len(pdf_reader.pages),
                            "file_size": os.path.getsize(pdf_path)
                        }
                    })
            except Exception as e:
                logger.error(f"Error processing PDF {pdf_path}: {str(e)}")
                continue
        
        return documents


class TxtLoader(DocumentLoader):
    """Plain text document loader"""
    
    async def load_documents(self, path: str) -> List[Dict[str, Any]]:
        """Load and extract text from text files"""
        documents = []
        
        # Handle single file or directory
        file_paths = []
        if os.path.isfile(path):
            file_paths = [path]
        elif os.path.isdir(path):
            file_paths = [os.path.join(path, f) for f in os.listdir(path) if f.lower().endswith('.txt')]
        
        for txt_path in file_paths:
            try:
                with open(txt_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                
                documents.append({
                    "content": content,
                    "metadata": {
                        "source": txt_path,
                        "format": "txt",
                        "file_size": os.path.getsize(txt_path)
                    }
                })
            except Exception as e:
                logger.error(f"Error processing TXT {txt_path}: {str(e)}")
                continue
        
        return documents


class MarkdownLoader(DocumentLoader):
    """Markdown document loader"""
    
    async def load_documents(self, path: str) -> List[Dict[str, Any]]:
        """Load and extract text from markdown files"""
        documents = []
        
        # Handle single file or directory
        file_paths = []
        if os.path.isfile(path):
            file_paths = [path]
        elif os.path.isdir(path):
            file_paths = [os.path.join(path, f) for f in os.listdir(path) if f.lower().endswith('.md')]
        
        for md_path in file_paths:
            try:
                with open(md_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                
                documents.append({
                    "content": content,
                    "metadata": {
                        "source": md_path,
                        "format": "md",
                        "file_size": os.path.getsize(md_path)
                    }
                })
            except Exception as e:
                logger.error(f"Error processing MD {md_path}: {str(e)}")
                continue
        
        return documents


class UniversalDocLoader:
    """Universal document loader that handles multiple formats"""
    
    def __init__(self):
        self.loaders = {
            'pdf': PDFLoader(),
            'txt': TxtLoader(),
            'md': MarkdownLoader(),
        }
    
    async def load_from_path(self, path: str) -> List[Dict[str, Any]]:
        """Auto-detect format and load documents"""
        if os.path.isfile(path):
            # Single file - determine format from extension
            ext = Path(path).suffix.lower()[1:]  # Remove dot
            if ext in self.loaders:
                loader = self.loaders[ext]
                return await loader.load_documents(path)
            else:
                raise ValueError(f"Unsupported file format: {ext}")
        elif os.path.isdir(path):
            # Directory - process all supported formats recursively
            all_documents = []

            for fmt, loader in self.loaders.items():
                try:
                    # Recursively look for files with this format in directory and subdirectories
                    path_obj = Path(path)
                    files = list(path_obj.rglob(f'*.{fmt}'))

                    if files:
                        # Process each file found
                        for file_path in files:
                            docs = await loader.load_documents(str(file_path))
                            all_documents.extend(docs)
                except Exception as e:
                    logger.error(f"Error loading {fmt} files from {path}: {str(e)}")
                    continue

            return all_documents
        else:
            raise ValueError(f"Path does not exist: {path}")


# Example usage and test function
async def test_loader():
    """Test the document loader with sample data"""
    # This would be used to test on actual data
    pass