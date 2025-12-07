# RAG Chatbot Golden Test Set

This file contains a set of "golden questions" and their expected answers for testing the RAG chatbot.

## Test Cases

### Test Case 1: Basic Retrieval
- **Question**: "What is ROS 2?"
- **Expected Answer**: [A concise summary of ROS 2 based on the book's content]
- **Relevant Document**: `frontend/docs/02-ros2/ros2.md`

### Test Case 2: Specific Information Retrieval
- **Question**: "How do I build a new ROS 2 package?"
- **Expected Answer**: [Step-by-step instructions for building a new ROS 2 package]
- **Relevant Document**: `frontend/docs/02-ros2/ros2.md`

### Test Case 3: Contextual Understanding
- **Question**: "Explain the concept of embodied intelligence in humanoid robots."
- **Expected Answer**: [Explanation of embodied intelligence drawing from Module 00 and 01]
- **Relevant Document**: `frontend/docs/00-introduction/intro.md`, `frontend/docs/01-foundations/foundations.md`

### Test Case 4: Edge Case - Out of Scope
- **Question**: "What is the capital of France?"
- **Expected Answer**: "I can only answer questions related to humanoid robotics and the content of this book."
- **Relevant Document**: None (should be identified as out of scope)
