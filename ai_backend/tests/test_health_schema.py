from app.schemas.student import FullWorkflowRequest


def test_full_workflow_request_schema():
    payload = {
        "user_id": "u1",
        "exam_date": "2026-03-01",
        "class_name": "12",
        "board": "CBSE",
        "subject": "Physics",
        "textbook_text": "Kinematics",
        "previous_papers_text": ["paper1", "paper2"],
        "syllabus_text": "Motion in 1D",
        "chapter": "Kinematics",
        "preferred_language": "English",
    }
    req = FullWorkflowRequest(**payload)
    assert req.board == "CBSE"
