# 🧠 AI To-Do Prioritizer

A simple Python CLI tool that helps you prioritize your to-do list based on **importance** and **due dates**. Optionally, you can integrate **OpenAI's GPT** to rewrite vague tasks into more actionable items.

---

## 🚀 Features

- 📌 Input tasks with description, importance level, and optional due date  
- ⚖️ Automatic priority scoring based on urgency and importance  
- 📋 Outputs a sorted list of your most important tasks  
- 🤖 (Optional) Rewrite tasks using OpenAI for clarity and actionability

---

## 🛠️ How It Works

1. You input the task details (description, importance, due date)
2. The script scores each task:
   - High importance = +2
   - Medium = +1
   - Due in 0-2 days = +2 to +3 more
3. Tasks are sorted by score and displayed in order

---

## 📦 Installation

### Clone the Repo
```bash
git clone https://github.com/your-username/ai-todo-prioritizer.git
cd ai-todo-prioritizer
