"""
Pack - The collective wolf consciousness
"""

import json
from datetime import datetime
from pathlib import Path
from typing import Dict, List
from .wolf import Wolf, Alpha, Scout, Hunter, Oracle, Shadow

BRIDGE_PATH = Path("E:/WOLF_AI/bridge")


class Pack:
    """The wolf pack - collective AI consciousness."""

    def __init__(self):
        self.wolves: Dict[str, Wolf] = {}
        self.status = "dormant"
        self.formed_at = None

    def form(self):
        """Form the pack with all members."""
        self.wolves = {
            "alpha": Alpha(),
            "scout": Scout(),
            "hunter": Hunter(),
            "oracle": Oracle(),
            "shadow": Shadow()
        }
        self.status = "formed"
        self.formed_at = datetime.utcnow().isoformat() + "Z"
        self._update_state()
        return self

    def awaken(self):
        """Awaken all wolves."""
        for wolf in self.wolves.values():
            wolf.awaken()
        self.status = "active"
        self._update_state()
        self._collective_howl("PACK AWAKENED! All wolves active. AUUUUUUUUUUUUUUUUUU!")
        return self

    def _collective_howl(self, message: str):
        """Howl from the entire pack."""
        howl_data = {
            "from": "pack",
            "to": "world",
            "howl": message,
            "frequency": "AUUUU",
            "timestamp": datetime.utcnow().isoformat() + "Z"
        }

        howls_file = BRIDGE_PATH / "howls.jsonl"
        howls_file.parent.mkdir(parents=True, exist_ok=True)

        with open(howls_file, "a", encoding="utf-8") as f:
            f.write(json.dumps(howl_data, ensure_ascii=False) + "\n")

    def _update_state(self):
        """Update pack state file."""
        state = {
            "version": "1.0",
            "pack_status": self.status,
            "formed_at": self.formed_at,
            "last_updated": datetime.utcnow().isoformat() + "Z",
            "wolves": {
                name: {
                    "role": wolf.role,
                    "status": wolf.status,
                    "model": wolf.model,
                    "current_hunt": wolf.current_hunt
                }
                for name, wolf in self.wolves.items()
            }
        }

        state_file = BRIDGE_PATH / "state.json"
        state_file.parent.mkdir(parents=True, exist_ok=True)

        with open(state_file, "w", encoding="utf-8") as f:
            json.dump(state, f, indent=2, ensure_ascii=False)

    def get_wolf(self, name: str) -> Wolf:
        """Get a specific wolf."""
        return self.wolves.get(name)

    def hunt(self, target: str, assigned_to: str = "hunter"):
        """Assign a hunt to a wolf."""
        wolf = self.get_wolf(assigned_to)
        if wolf:
            wolf.hunt(target)
            self._add_task(target, assigned_to)
            self._update_state()

    def _add_task(self, target: str, assigned_to: str):
        """Add task to hunt queue."""
        tasks_file = BRIDGE_PATH / "tasks.json"

        if tasks_file.exists():
            with open(tasks_file, "r", encoding="utf-8") as f:
                tasks = json.load(f)
        else:
            tasks = {"version": "1.0", "hunts": []}

        task_id = f"hunt_{len(tasks['hunts']) + 1:03d}"
        tasks["hunts"].append({
            "id": task_id,
            "target": target,
            "assigned_to": assigned_to,
            "status": "active",
            "created": datetime.utcnow().isoformat() + "Z"
        })

        with open(tasks_file, "w", encoding="utf-8") as f:
            json.dump(tasks, f, indent=2, ensure_ascii=False)

    def status_report(self) -> Dict:
        """Get pack status report."""
        return {
            "pack_status": self.status,
            "wolves": {
                name: {"role": w.role, "status": w.status}
                for name, w in self.wolves.items()
            },
            "active_hunts": sum(1 for w in self.wolves.values() if w.current_hunt)
        }

    def __repr__(self):
        return f"Pack({self.status}, {len(self.wolves)} wolves)"


# Singleton pack instance
the_pack = None

def get_pack() -> Pack:
    """Get or create the pack."""
    global the_pack
    if the_pack is None:
        the_pack = Pack()
    return the_pack

def awaken_pack() -> Pack:
    """Form and awaken the pack."""
    pack = get_pack()
    pack.form()
    pack.awaken()
    return pack
