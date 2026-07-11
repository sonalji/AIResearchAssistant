# AIResearchAssistant
This repo builds an AI application for EEG Papers 
README.txt for EEG AI Research Assistant

It is an AI powered application that helps researchers, profs to ask queries in natural language and retrieve
relevant information from the uploaded documents/PDFs. These responses are context aware, concise and with citations.

Copyright 2026 by Sonal Bajpai and online resources


Problem:
--------
Researchers working in EEG spend a significant amount of time reading and comparing multiple research papers.
To find answers like which preprocessing pipeline is most commonly used in EEG? What techniques can be used to      remove eye blink from data ? Which EEG frequency bands are important?. Traditional search only matches keywords and cannot understand context As a result, researchers lose considerable time gathering information instead of conducting research.

Solution:
--------
The EEG Research Assistant allows users to upload EEG research papers and interact with them using natural language. The application retrieves the most relevant sections from the uploaded literature using semantic search and provides concise answers supported by citations. This reduces the effort required to review literature and helps users quickly understand EEG concepts, methodologies, and research trends.

Target Audience:
----------------
Healthcare AI Researchers, ML Engineers working on EEG,PhD Researchers


Features:
----------
 1) Upload Multiple EEG Research Papers
 2) Natural Language Q&A
 3) Source Citations
 4) Semantic search using vector embeddings
 5) Compare methodologies across research papers	
 6) Automatic paper summarization
 7) Literature Review Generator
 8) Local vector database for fast retrieval
 9) Built using Retrieval-Augmented Generation
 10) Working AI feature

 text_cleaner.py:Objective is to clean you text it includes removal of extra whitespaces,multiple blank lines, empty lines and if there is repeated common line in all pages like IEEE DOI etc. 

