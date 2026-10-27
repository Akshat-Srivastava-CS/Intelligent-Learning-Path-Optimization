# 📚 Research Papers & Gap Analysis



This folder contains the foundational research papers studied during Month 1 of the project, along with the gap analysis that shaped the final algorithm implementation.



## 1. Base Literature Studied



**1. Prerequisites-based course recommendation: Recommending learning objects using concept prerequisites and metadata matching**

* **Link:** [Springer (2024)](https://link.springer.com/content/pdf/10.1186/s40561-024-00301-0.pdf)

* **Usage:** Explored the concept of prerequisite relationships between topics.

* **Application in Project:** These relationships were used to build the Directed Acyclic Graph (DAG) to determine the mathematically correct order in which topics must be learned.



**2. Personalized Learning Path Recommendation and Knowledge Tracing Model for Large-Scale Online Education**

* **Link:** [Inderscience](https://www.inderscience.com/storage/f101121481263579.pdf)

* **Usage:** Investigated learner's knowledge level, prerequisites, and learning load.

* **Application in Project:** Helped the platform select and prioritize the next suitable topic based on the learner's current progress and unlocked prerequisites.



**3. Set-to-Sequence Ranking-Based Concept-Aware Learning Path Recommendation**

* **Link:** [arXiv (2025)](https://arxiv.org/pdf/2506.22303)

* **Usage:** Studied the generation of complete learning paths by connecting related concepts.

* **Application in Project:** Supported the graph-based approach for arranging connected topics into an appropriate, strict learning sequence.



**4. Education-Oriented Graph Retrieval-Augmented Generation (RAG) for Learning Path Recommendation**

* **Link:** [arXiv (2023)](https://arxiv.org/pdf/2306.04234)

* **Usage:** Evaluated how educational knowledge and relationships are represented through graphs.

* **Application in Project:** Provided the foundation for structuring graph-based concept relationships prior to running shortest-path algorithms.



**5. Personalized Learning Path Recommendation and Knowledge Tracing Model**

* **Link:** [i-JET](https://online-journals.org/index.php/i-jet/article/view/28455/11337)

* **Usage:** Examined intelligent approaches for organizing learning paths.

* **Application in Project:** Used to support graph-based topic dependencies and improve the overall selection algorithm.



---



## 2. Identified Research Gaps



While the papers above provided a strong theoretical foundation, the following critical gaps were identified for practical student use:

* **No Time Constraints:** Existing models assume unlimited study time, ignoring the highly practical scenario of last-minute exam preparation.

* **Predictive Over-reliance:** ML/AI models (like Knowledge Tracing or RAG) often generate invalid sequences that violate strict academic syllabus prerequisites.

* **Missing Cost Weights:** Concept graphs in current literature lack physical mathematical weights (e.g., estimated study hours) required for true path optimization.

* **Generic Datasets:** Most models are evaluated on theoretical data rather than rigid engineering curricula.



## 3. The Project's Solution



To resolve these gaps, this MVP completely replaces predictive AI with deterministic Data Structures and Algorithms (DSA):

* **Real-World Mapping:** Built a weighted Adjacency List using actual B.Tech Semester-3 subjects (DSA-II, OS, Java) instead of generic datasets.

* **Exact Routing (Dijkstra):** Assigned study hours as edge weights to calculate the guaranteed fastest, prerequisite-validated route, entirely avoiding AI hallucinations.

* **Time Optimization (0/1 Knapsack):** Treated the student's available time as a strict mathematical boundary, dynamically selecting the highest-scoring topic combination that strictly fits the time budget constraint.
