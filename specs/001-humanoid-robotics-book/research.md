# Research: Humanoid Robotics Book

## Decisions

### Translation Strategy
- **Decision**: Hybrid approach (cache first request per paragraph).
- **Rationale**: Balances repository size and API usage. Provides a good user experience by serving cached translations quickly.
- **Alternatives considered**: Pre-translating all content (larger repo), on-demand LLM translation (slower, requires API key).

### Personalization Depth
- **Decision**: Light personalization with an optional "explain like I’m beginner/expert" toggle.
- **Rationale**: Provides a good balance between personalization and implementation complexity. The toggle allows users to control the level of detail.
- **Alternatives considered**: Heavy personalization (rewriting explanations based on user background), which would be much more complex to implement and maintain.

### RAG Chunking Strategy
- **Decision**: 800-token chunks with 200-token overlap.
- **Rationale**: This was found to provide the best quality for robotics code and text.
- **Alternatives considered**: 512-token chunks with 128 overlap, 1024-token chunks.

## Research Approach

- **Research-concurrent**: No upfront 3-month literature review. Each module is researched only when its turn comes (week-of writing).
- **Primary sources**: official documentation (ROS 2, Isaac Sim, NVIDIA papers), GitHub repos, Panaversity curriculum.
- **Secondary**: latest arXiv papers on VLA, humanoid locomotion, sim-to-real (2023–2025 only).
- **Citation style**: APA 7th (as required by constitution).
