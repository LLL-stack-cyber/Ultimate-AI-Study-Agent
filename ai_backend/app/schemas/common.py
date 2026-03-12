from typing import Any

from pydantic import BaseModel, Field


class AgentResponse(BaseModel):
    agent: str
    output: dict[str, Any]


class WorkflowResponse(BaseModel):
    workflow_id: str
    status: str = "completed"
    results: list[AgentResponse] = Field(default_factory=list)
