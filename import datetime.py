import datetime
from operator import itemgetter

# Optional: Uncomment to use OpenAI
# import openai
# openai.api_key = "your-api-key"

def get_priority_score(task):
    """Assigns a priority score based on importance and due date"""
    score = 0
    if task["importance"].lower() == "high":
        score += 2
    elif task["importance"].lower() == "medium":
        score += 1

    if task["due_date"]:
        days_left = (task["due_date"] - datetime.datetime.now()).days
        if days_left <= 0:
            score += 3
        elif days_left <= 2:
            score += 2
        elif days_left <= 5:
            score += 1

    return score

def ai_rewrite_task(task_description):
    """Optional GPT task rewriting (commented out unless OpenAI API is used)"""
    # response = openai.ChatCompletion.create(
    #     model="gpt-3.5-turbo",
    #     messages=[{"role": "user", "content": f"Rewrite this task to be more actionable: {task_description}"}]
    # )
    # return response['choices'][0]['message']['content'].strip()
    return task_description  # fallback

def main():
    tasks = []
    n = int(input("How many tasks do you want to enter? "))

    for _ in range(n):
        desc = input("Task description: ")
        desc = ai_rewrite_task(desc)
        importance = input("Importance (high/medium/low): ")

        date_input = input("Due date (YYYY-MM-DD) or leave blank: ")
        if date_input:
            due_date = datetime.datetime.strptime(date_input, "%Y-%m-%d")
        else:
            due_date = None

        task = {
            "description": desc,
            "importance": importance,
            "due_date": due_date
        }
        task["priority_score"] = get_priority_score(task)
        tasks.append(task)

    # Sort tasks by score descending
    sorted_tasks = sorted(tasks, key=itemgetter("priority_score"), reverse=True)

    print("\n🔝 Prioritized Tasks:")
    for i, t in enumerate(sorted_tasks, 1):
        print(f"{i}. {t['description']} [Score: {t['priority_score']}]")

if __name__ == "__main__":
    main()
