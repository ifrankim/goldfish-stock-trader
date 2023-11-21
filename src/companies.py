from collections import deque
import random

# Initialize the queue of companies
company_queue = deque(["Company1", "Company2", "Company3", "Company4", "Company5"])

def select_action(fish_position):
    if fish_position == "right":
        selected_action = company_queue.popleft()
        print(f"Selected action for the right side: {selected_action}")
    else:
        selected_action = company_queue.popleft()
        print(f"Selected action for the left side: {selected_action}")

    # Move forward in the queue and add two new companies
    new_company1 = "New Company 1"
    new_company2 = "New Company 2"
    company_queue.extend([new_company1, new_company2])

if __name__ == "__main__":
    # Fish tracking simulation
    fish_position = random.choice(["left", "right"])  # Simulates the fish position
    select_action(fish_position)
