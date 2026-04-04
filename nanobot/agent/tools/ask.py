"""Tool for asking the user for input or confirmation."""

from typing import Any

from nanobot.agent.tools.base import Tool


class AskUserInterrupt(BaseException):
    """Signal raised to interrupt execution and ask the user a question."""
    def __init__(self, question: str, options: list[str] | None = None):
        self.question = question
        self.options = options
        super().__init__(question)


class AskUserTool(Tool):
    """Tool that suspends the agent to ask the user a question."""

    name = "ask_user"
    description = (
        "Ask the user a question to confirm an action, get a decision, or request more information. "
        "The agent execution will pause and wait for the user's reply."
    )
    parameters = {
        "type": "object",
        "properties": {
            "question": {
                "type": "string",
                "description": "The question to ask the user.",
            },
            "options": {
                "type": "array",
                "items": {"type": "string"},
                "description": "Optional list of choices for the user to pick from.",
            },
        },
        "required": ["question"],
    }

    async def execute(self, question: str, options: list[str] | None = None, **kwargs: Any) -> Any:
        raise AskUserInterrupt(question, options)
