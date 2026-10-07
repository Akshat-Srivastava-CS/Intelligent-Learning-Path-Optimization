import streamlit as st
import heapq
from collections import defaultdict, deque

# ==========================================
# 1. DSA LOGIC (Backend)
# ==========================================
class LearningTopic:
    def __init__(self, topic_id, name, subject, study_time, importance):
        self.topic_id = topic_id
        self.name = name
        self.subject = subject
        self.study_time = study_time  
        self.importance = importance  

class LearningPlatform:
    def __init__(self):
        self.topics = {}
        self.adj_list = defaultdict(list)
        self.in_degree = defaultdict(int)
        
    def add_topic(self, topic_id, name, subject, study_time, importance):
        self.topics[topic_id] = LearningTopic(topic_id, name, subject, study_time, importance)
        self.in_degree[topic_id] = 0
        
    def add_prerequisite(self, pre_id, post_id):
        self.adj_list[pre_id].append(post_id)
        self.in_degree[post_id] += 1

    def fastest_path(self, start_id, target_id):
        pq = [(self.topics[start_id].study_time, start_id, [self.topics[start_id].name])]
        visited = set()
        
        while pq:
            current_time, current_id, path = heapq.heappop(pq)
            
            if current_id == target_id:
                return {"time": current_time, "path": path}
                
            if current_id in visited:
                continue
            visited.add(current_id)
            
            for neighbor in self.adj_list[current_id]:
                if neighbor not in visited:
                    next_time = current_time + self.topics[neighbor].study_time
                    heapq.heappush(pq, (next_time, neighbor, path + [self.topics[neighbor].name]))
        return None

    def optimize_study_session(self, available_topics, max_hours):
        n = len(available_topics)
        dp = [[0 for _ in range(max_hours + 1)] for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            time = available_topics[i-1].study_time
            val = available_topics[i-1].importance
            
            for w in range(1, max_hours + 1):
                if time <= w:
                    dp[i][w] = max(dp[i-1][w], dp[i-1][w-time] + val)
                else:
                    dp[i][w] = dp[i-1][w]
                    
        selected_topics = []
        w = max_hours
        for i in range(n, 0, -1):
            if dp[i][w] != dp[i-1][w]:
                selected_topics.append(available_topics[i-1].name)
                w -= available_topics[i-1].study_time
                
        return dp[n][max_hours], selected_topics

# ==========================================
# 2. SEMESTER 3 DATA SETUP
# ==========================================
@st.cache_resource
def load_data():
    platform = LearningPlatform()
    
    # --- 1. DSA-II ---
    platform.add_topic(101, "Trees & BST", "DSA-II", 3, 7)
    platform.add_topic(102, "Graph Traversal (BFS/DFS)", "DSA-II", 4, 8)
    platform.add_topic(103, "Shortest Path (Dijkstra)", "DSA-II", 5, 10)
    platform.add_topic(104, "Dynamic Programming", "DSA-II", 6, 9)
    platform.add_topic(105, "0/1 Knapsack", "DSA-II", 4, 10)
    platform.add_prerequisite(101, 102)
    platform.add_prerequisite(102, 103)
    platform.add_prerequisite(104, 105)

    # --- 2. Operating Systems ---
    platform.add_topic(201, "OS Architecture", "Operating Systems", 2, 5)
    platform.add_topic(202, "Process Management", "Operating Systems", 4, 8)
    platform.add_topic(203, "CPU Scheduling", "Operating Systems", 5, 9)
    platform.add_topic(204, "Deadlocks", "Operating Systems", 4, 10)
    platform.add_topic(205, "Memory Management", "Operating Systems", 6, 9)
    platform.add_prerequisite(201, 202)
    platform.add_prerequisite(202, 203)
    platform.add_prerequisite(203, 204)

    # --- 3. Java Programming ---
    platform.add_topic(301, "Java Basics & JVM", "Java", 2, 6)
    platform.add_topic(302, "OOP Concepts", "Java", 4, 9)
    platform.add_topic(303, "Exception Handling", "Java", 3, 7)
    platform.add_topic(304, "Multithreading", "Java", 5, 10)
    platform.add_topic(305, "Collections Framework", "Java", 6, 9)
    platform.add_prerequisite(301, 302)
    platform.add_prerequisite(302, 303)
    platform.add_prerequisite(303, 304)

    # --- 4. Artificial Intelligence ---
    platform.add_topic(401, "Intro to AI & Agents", "Artificial Intelligence", 3, 6)
    platform.add_topic(402, "Uninformed Search", "Artificial Intelligence", 4, 8)
    platform.add_topic(403, "Heuristic Search (A*)", "Artificial Intelligence", 5, 10)
    platform.add_topic(404, "Knowledge Representation", "Artificial Intelligence", 4, 7)
    platform.add_prerequisite(401, 402)
    platform.add_prerequisite(402, 403)

    # --- 5. CAPP (Computer Architecture) ---
    platform.add_topic(501, "Digital Logic Review", "CAPP", 2, 5)
    platform.add_topic(502, "Instruction Set Architecture", "CAPP", 4, 8)
    platform.add_topic(503, "Pipelining", "CAPP", 6, 10)
    platform.add_topic(504, "Cache Memory", "CAPP", 5, 9)
    platform.add_prerequisite(501, 502)
    platform.add_prerequisite(502, 503)

    return platform

platform = load_data()

# ==========================================
# 3. STREAMLIT UI (Frontend)
# ==========================================
st.set_page_config(page_title="Sem 3 Study Optimizer", layout="wide")
st.title("🎓 B.Tech Sem-3 Learning Path Optimizer")
st.write("Plan your semester studies efficiently using DSA algorithms.")

# Sidebar for Subject Filtering
st.sidebar.header("Filter by Subject")
subjects = ["All Subjects", "DSA-II", "Operating Systems", "Java", "Artificial Intelligence", "CAPP"]
selected_subject = st.sidebar.selectbox("Choose a Syllabus to Target:", subjects)

# Filter logic
if selected_subject == "All Subjects":
    filtered_topics = platform.topics
else:
    filtered_topics = {k: v for k, v in platform.topics.items() if v.subject == selected_subject}

if not filtered_topics:
    st.warning("No topics found for this subject.")
else:
    tab1, tab2 = st.tabs(["Fastest Path (Dijkstra)", "Time Optimizer (Knapsack)"])

    with tab1:
        st.header("Find the Fastest Learning Route")
        
        col1, col2 = st.columns(2)
        with col1:
            start = st.selectbox("Current Topic:", options=list(filtered_topics.keys()), format_func=lambda x: filtered_topics[x].name)
        with col2:
            # Try to pick a different target if possible
            target_opts = list(filtered_topics.keys())
            default_idx = len(target_opts)-1 if len(target_opts) > 1 else 0
            target = st.selectbox("Target Topic:", options=target_opts, format_func=lambda x: filtered_topics[x].name, index=default_idx)
            
        if st.button("Generate Route", type="primary"):
            result = platform.fastest_path(start, target)
            if result:
                st.success(f"**Total Estimated Time:** {result['time']} hours")
                st.info(f"**Recommended Study Path:** {' ➔ '.join(result['path'])}")
            else:
                st.error("No direct prerequisite chain exists between these topics. Try checking dependencies.")

    with tab2:
        st.header("Exam Cram Optimizer")
        st.write("Select the maximum hours you have, and the algorithm will pick the highest-scoring topics.")
        
        hours_left = st.slider("Hours left until the exam:", min_value=1, max_value=30, value=12)
        
        if st.button("Optimize My Time", type="primary"):
            available_list = list(filtered_topics.values())
            max_score, selected = platform.optimize_study_session(available_list, hours_left)
            st.success(f"**Maximum Learning Score Achieved:** {max_score}")
            st.info(f"**Best combination of topics to cover:** \n\n" + ", ".join(selected))