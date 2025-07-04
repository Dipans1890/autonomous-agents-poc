
class CynthiaAgent:
    def __init__(self, memory):
        self.memory = memory

    def create_user_story(self, title, as_a, i_want, so_that, acceptance_criteria):
        story = {
            "title": title,
            "story": f"As a {as_a}, I want {i_want} so that {so_that}",
            "acceptance_criteria": acceptance_criteria
        }
        self.memory.save_interaction("cynthia", story, "PROJ-001", "user_story")
        return story
