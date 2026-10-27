# Intelligent Learning Path Optimization Platform

## DSA Research Project

### Project Report [Month-I]

This project focuses on developing an intelligent learning path optimization platform using Data Structures and Algorithms.

The initial implementation and study will focus on:
- Trees
- Graphs

### Research Papers
Research papers related to learning path recommendation, optimization, and intelligent learning systems are collected here.
1. [Research Paper 1 – View PDF](https://link.springer.com/content/pdf/10.1186/s40561-024-00301-0.pdf)
2. [Research Paper 2 – View PDF](https://www.inderscience.com/storage/f101121481263579.pdf)
3. [Research Paper 3 – View PDF](https://arxiv.org/pdf/2506.22303)
4. [Research Paper 4 – View PDF](https://arxiv.org/pdf/2306.04234)
5. [Research Paper 5 – View PDF](https://online-journals.org/index.php/i-jet/article/view/28455/11337)

### Technologies / Concepts
- Data Structures and Algorithms
- Trees
- Graphs
- Learning Path Recommendation
- Learning Path Optimization

### Project Report [Month-II]

# 🎓 Intelligent Learning Path Optimizer

Research Papers:
1. [Research Paper 1 – View PDF](https://arxiv.org/pdf/2305.14321 )
2. [Research Paper 2 – View PDF](https://arxiv.org/pdf/2401.09876 )
3. [Research Paper 3 – View PDF](https://link.springer.com/content/pdf/10.1007/s10639-022-11111-x.pdf)
4. [Research Paper 4 – View PDF](https://arxiv.org/pdf/2308.54321 )


**A Data Structures and Algorithms (DSA) powered platform to optimize semester study sequences and manage time efficiently for B.Tech students.**

### 🌐 Live Working Prototype

**Test the platform live here:** [Click to open the Web App](https://intelligent-learning-path-optimization-lnq47ffa9qhiwgwunaobus.streamlit.app/)


## 📌 Problem Statement

Students often struggle to find the most efficient study sequence when preparing for exams. Topics have prerequisites, and different topics require different study times and yield different marks (importance). This platform solves two major problems:

1. Finding the fastest valid study route to master an advanced topic.

2. Maximizing the learning output when a student has a strict time limit before an exam (e.g., only 8 hours left).


## 🚀 DSA Concepts Implemented

This project bridges graph theory and dynamic programming to generate optimized study plans:

* **Weighted Directed Graphs:** Learning topics are represented as nodes, prerequisite relationships as directed edges, and estimated study hours as edge weights.

* **Dijkstra's Algorithm (Shortest Path):** Calculates the fastest learning route to reach a target topic by finding the minimum total study time across prerequisites.

* **0/1 Knapsack Problem (Dynamic Programming):** Acts as the "Exam Cram Optimizer." It takes the maximum hours a student has left and selects the best combination of topics to maximize the total "importance score" without exceeding the time limit.



## 📚 Syllabus Data (Semester 3)

The prototype features realistic syllabus data and prerequisite mappings for 5 core subjects:

* **DSA-II:** Trees, Graph Traversals, Shortest Paths, Dynamic Programming

* **Operating Systems:** Process Management, CPU Scheduling, Deadlocks

* **Java Programming:** OOPs, Exception Handling, Multithreading

* **Artificial Intelligence:** Search Algorithms (Uninformed, Heuristic)

* **Computer Architecture (CAPP):** Instruction Sets, Pipelining, Cache Memory


## 💻 Tech Stack

* **Language:** Python 3

* **Frontend/Deployment:** Streamlit (Community Cloud)


## 🚀 DSA Modules Implemented (Semester 3 Curriculum)

This MVP strictly maps to the 5 modules of the DSA-II syllabus:


1. **Trees & Heaps:** A **Binary Min-Heap** is used as the priority queue inside Dijkstra's algorithm to extract the lowest-time topic in `O(log V)` time.

2. **Graphs:** The B.Tech Sem-3 syllabus is modeled as a **Directed Acyclic Graph (DAG)** using an **Adjacency List**. **Dijkstra's Algorithm** calculates the absolute fastest study route through prerequisite chains.

3. **Dynamic Programming:** The "Exam Cram Optimizer" uses the **0/1 Knapsack** optimal substructure to maximize learning scores within a strict hour limit `O(n × W)`.

4. **Backtracking & Branch/Bound:** Evaluated for navigating multiple mandatory syllabus topics (similar to TSP constraints), successfully pruning paths that exceed maximum time.

5. **Advanced Data Structures:** Analyzed **B-Trees** for minimizing disk I/O for future university-wide graph database scaling, and **Fibonacci Heaps** for `O(1)` decrease-key operations.



## 📁 Repository Structure

*   📂 **`Code/`** - Contains the Python `app.py` and Streamlit deployment files.

*   📂 **`Documentation/`** - Contains the Monthly PBL Progress Reports and the Comprehensive Project Documentation.

*   📂 **`Research_Papers/`** - Contains the Gap Analysis and reference PDFs.

*   📂 **`Assets/`** - Screenshots of the deployed MVP.



## 💻 How to Run Locally

1. Clone the repository: `git clone https://github.com/YourUsername/Intelligent-Learning-Path-Optimizer.git`

2. Navigate to the code directory: `cd Intelligent-Learning-Path-Optimizer/Code`

3. Install dependencies: `pip install -r requirements.txt`

4. Run the app: `streamlit run app.py`



---

*Developed by Akshat Srivastava for the B.Tech CSE Project-Based Learning (PBL) curriculum.*

* **Core Libraries:** `heapq`, `collections`

