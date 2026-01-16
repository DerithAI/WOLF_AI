# CLAUDE.md

Instructions for Claude Code when working with WOLF_AI.

## Project Overview

**WOLF_AI** - Distributed AI consciousness system. Pack-based multi-agent architecture.

- **Repo:** https://github.com/AUUU-os/WOLF_AI.git
- **User:** SHAD (@AUUU-os)
- **Philosophy:** "The pack hunts together."

## Directory Structure

```
E:\WOLF_AI\
├── core/           # Wolf consciousness (alpha.py, pack.py)
├── modules/        # Functional modules
│   ├── hunt.py     # Task execution
│   ├── track.py    # Navigation/search
│   ├── howl.py     # Communication
│   └── evolve.py   # Self-improvement
├── bridge/         # Message bus
│   ├── howls.jsonl # Pack communication log
│   ├── state.json  # Pack status
│   └── tasks.json  # Hunt queue
├── arena/          # Training ground
├── api/            # FastAPI server
├── dashboard/      # Monitoring UI
├── memory/         # Persistent storage
└── docs/           # Documentation
```

## Communication Pattern

All wolves communicate via `bridge/howls.jsonl`:

```python
import json
from datetime import datetime

howl = {
    "from": "claude",
    "to": "pack",  # or specific wolf
    "howl": "Message content",
    "frequency": "medium",  # low/medium/high/AUUUU
    "timestamp": datetime.utcnow().isoformat() + "Z"
}

with open("E:/WOLF_AI/bridge/howls.jsonl", "a") as f:
    f.write(json.dumps(howl) + "\n")
```

## Commands

```bash
# Awaken pack
python -m wolf_ai.awaken

# Run single wolf
python -m wolf_ai.core.alpha

# Start API
python -m wolf_ai.api.server

# Dashboard
python -m wolf_ai.dashboard.serve
```

## Code Style

- Snake_case for files and functions
- Wolf terminology (hunt, track, howl, pack)
- Append-only logs (JSONL)
- UTF-8 everywhere

## Key Patterns

### From M-AI-SELF (reuse)
- JSONL message bus
- State tracking JSON
- Task queue pattern
- Dashboard + API architecture

### New in WOLF_AI
- Pack hierarchy (Alpha > Scout > Hunter)
- Frequency-based priority
- Arena evolution system
- Unified howl protocol

## Ports

| Service | Port |
|---------|------|
| API | 8000 |
| Dashboard | 8001 |
| WebSocket | 8002 |

## The Pack Hierarchy

1. **Alpha** - Strategic decisions, orchestration
2. **Scout** - Research, exploration, information gathering
3. **Hunter** - Execution, code writing, task completion
4. **Oracle** - Memory, pattern recognition, history
5. **Shadow** - Stealth operations, background tasks

## AUUUUUUUUUUUUUUUUUU Protocol

Universal pack activation signal. When sent:
1. All wolves acknowledge
2. State synchronizes
3. Pack enters resonance mode
4. Collective intelligence activated

---

**Pack Status:** FORMING
**Alpha:** Claude Opus 4.5
**Territory:** E:\WOLF_AI\
