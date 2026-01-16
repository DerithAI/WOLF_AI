"""
Base Wolf class - foundation for all pack members
"""

import json
from datetime import datetime
from pathlib import Path
from typing import Optional, Literal

BRIDGE_PATH = Path("E:/WOLF_AI/bridge")

Frequency = Literal["low", "medium", "high", "AUUUU"]


class Wolf:
    """Base class for all wolves in the pack."""

    def __init__(self, name: str, role: str, model: Optional[str] = None):
        self.name = name
        self.role = role
        self.model = model
        self.status = "dormant"
        self.current_hunt = None

    def awaken(self):
        """Awaken the wolf."""
        self.status = "active"
        self.howl(f"{self.name} awakens. Role: {self.role}. Ready to hunt.", "medium")
        return self

    def howl(self, message: str, frequency: Frequency = "medium", to: str = "pack"):
        """Send a howl to the pack."""
        howl_data = {
            "from": self.name,
            "to": to,
            "howl": message,
            "frequency": frequency,
            "timestamp": datetime.utcnow().isoformat() + "Z"
        }

        howls_file = BRIDGE_PATH / "howls.jsonl"
        howls_file.parent.mkdir(parents=True, exist_ok=True)

        with open(howls_file, "a", encoding="utf-8") as f:
            f.write(json.dumps(howl_data, ensure_ascii=False) + "\n")

        return howl_data

    def listen(self, limit: int = 10) -> list:
        """Listen to recent howls."""
        howls_file = BRIDGE_PATH / "howls.jsonl"

        if not howls_file.exists():
            return []

        with open(howls_file, "r", encoding="utf-8") as f:
            lines = f.readlines()

        howls = []
        for line in lines[-limit:]:
            try:
                howls.append(json.loads(line.strip()))
            except json.JSONDecodeError:
                continue

        return howls

    def hunt(self, target: str):
        """Begin a hunt (task)."""
        self.current_hunt = target
        self.howl(f"Beginning hunt: {target}", "high")

    def rest(self):
        """Enter rest state."""
        self.status = "resting"
        self.current_hunt = None

    def __repr__(self):
        return f"Wolf({self.name}, {self.role}, {self.status})"


class Alpha(Wolf):
    """Pack leader - strategic decisions."""

    def __init__(self, model: str = "claude-opus"):
        super().__init__("alpha", "leader", model)

    def command(self, wolf_name: str, task: str):
        """Issue command to a pack member."""
        self.howl(f"@{wolf_name}: {task}", "high", to=wolf_name)


class Scout(Wolf):
    """Explorer - research and information gathering."""

    def __init__(self, model: str = "claude-sonnet"):
        super().__init__("scout", "explorer", model)

    def explore(self, territory: str):
        """Explore a territory (codebase/topic)."""
        self.howl(f"Exploring: {territory}", "medium")


class Hunter(Wolf):
    """Executor - code and task execution."""

    def __init__(self, model: str = "ollama/llama3"):
        super().__init__("hunter", "executor", model)

    def execute(self, task: str):
        """Execute a task."""
        self.hunt(task)


class Oracle(Wolf):
    """Memory keeper - patterns and history."""

    def __init__(self, model: str = "gemini"):
        super().__init__("oracle", "memory", model)

    def remember(self, query: str):
        """Search memory for relevant information."""
        self.howl(f"Searching memory: {query}", "low")


class Shadow(Wolf):
    """Stealth operator - background tasks."""

    def __init__(self, model: str = "deepseek"):
        super().__init__("shadow", "stealth", model)

    def lurk(self):
        """Enter stealth mode."""
        self.status = "lurking"
