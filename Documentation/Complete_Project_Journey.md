# 🚀 Complete Project Journey: From Concept to MVP



This document details the development lifecycle of the **Intelligent Learning Path Optimizer**, tracking its evolution across the three PBL review phases.



## 📌 Phase 1 (Month 1): Problem Identification & Conceptualization

*   **The Problem:** Students study prerequisite-heavy subjects randomly, missing foundational knowledge, and lack tools for strict last-minute exam time limits.

*   **The Innovation:** Treating the academic syllabus as a **Directed Acyclic Graph (DAG)**.

*   **Research Phase:** Reviewed 5 papers on e-learning. Identified a critical gap: existing systems rely on heavy predictive ML models that ignore strict time budgets and academic syllabus rules.



## ⚙️ Phase 2 (Month 2): Algorithm Selection & Prototyping

*   **Graph Design:** Built an Adjacency List representing topics and prerequisites, with physical weights for "Estimated Study Hours."

*   **Routing (Dijkstra's Algorithm):** Implemented using a Binary Min-Heap to calculate the guaranteed fastest prerequisite route to an advanced target topic.

*   **Time Optimization (0/1 Knapsack):** Treated the student's available hours as a strict boundary (weight limit) and topic importance as the value, maximizing the learning score within a fixed time budget.



## 🌟 Phase 3 (Month 3): Final MVP & Advanced Data Structures

*   **Dataset Innovation:** Mapped the actual B.Tech Semester-3 engineering syllabus (DSA-II, OS, Java, AI, CAPP).

*   **Advanced Evaluation:** Modeled Branch & Bound for alternative constrained paths and evaluated B-Trees for future university-wide database scaling.

*   **Deployment:** Wrapped the Python logic into a Streamlit UI and hosted the MVP live on Streamlit Community Cloud.
