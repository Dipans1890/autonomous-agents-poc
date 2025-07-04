def coordinator_flow(project_id, memory):
    # Simulate Cynthia creating a story and Crystal picking it up
    memory.save_interaction("cynthia", "User story created", project_id, "user_story")
    memory.save_interaction("crystal", "Task created based on Cynthia's input", project_id, "task")
    return "Cynthia ➜ Crystal flow completed successfully"
