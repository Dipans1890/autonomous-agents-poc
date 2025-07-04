import streamlit as st
from app.agents.crystal_pm import CrystalAgent
from app.agents.cynthia_ba import CynthiaAgent
from app.utils.memory import AgentMemory
from app.logic.rules_engine import evaluate_rules
from app.collaborator import coordinator_flow

st.title("Autonomous Agent Demo")

memory = AgentMemory()
project_id = st.text_input("Project ID", value="PROJ-001")
agent_choice = st.selectbox("Select Agent", ["Crystal", "Cynthia"])

if agent_choice == "Crystal":
    crystal = CrystalAgent(memory)
    if st.button("Generate Project Report"):
        result = crystal.create_project_status_report(project_id, "weekly")
        st.write(result)
    if st.button("Check Project Health"):
        decision = evaluate_rules(risk_level="high", budget_usage=0.85)
        st.write(decision)

elif agent_choice == "Cynthia":
    cynthia = CynthiaAgent(memory)
    if st.button("Create Sample User Story"):
        story = cynthia.create_user_story(
            title="Login Flow",
            as_a="user",
            i_want="to log in securely",
            so_that="my data is safe",
            acceptance_criteria=["Valid email", "Password > 8 chars"]
        )
        st.json(story)

if st.button("Run Cynthia ➜ Crystal Coordination"):
    result = coordinator_flow(project_id, memory)
    st.success(result)

if st.button("View Memory"):
    st.json(memory.get_context())
