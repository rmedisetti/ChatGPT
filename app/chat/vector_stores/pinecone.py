#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 20:23:15 2023

@author: rajeswari-pro
"""

import os
import pinecone
from langchain.vectorstores import Pinecone

from app.chat.embeddings.openai import embeddings

pinecone.init(
    api_key=os.getenv("PINECONE_API_KEY"),
    environment=os.getenv("PINECONE_ENV_NAME")
)

vector_store=Pinecone.from_existing_index(
    os.getenv("PINECONE_INDEX_NAME"), embeddings
)