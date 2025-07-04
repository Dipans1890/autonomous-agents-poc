class CrystalAgent:
    def __init__(self, memory):
        self.memory = memory

    def create_project_status_report(self, project_id, report_type):
        report = f"[Crystal] {report_type} report for {project_id}"
        self.memory.save_interaction("crystal", report, project_id, "report")
        return report
