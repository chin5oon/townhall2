"""Question content for Townhall Game — Folder B (Rounds 4–6)."""

GAME_TITLE = "The Building Challenges"
GAME_SUBTITLE = "A Different Mission · Rounds 4–6"

INTRODUCTION = (
    "Take on a standalone underground MRT challenge. Balance Cost Saving, "
    "Productivity & Innovation, and Safety across three rounds."
)

QUESTIONS = [
    {
        "id": "round_4",
        "round": "Round 4",
        "title": "Tunnelling Works",
        "prompt": (
            "The tunnels pass through soft marine clay near live MRT tracks and building foundations. "
            "Choose the TBM face-pressure and ground-treatment proposal."
        ),
        "options": [
            {
                "label": "Option A — Built-in TBM Face Pressure with Ground Improvement Works",
                "scores": {"cs": 0, "pi": 0, "s": 0},
                "feedback": (
                    "“Built-in face pressure” does not define a controllable design method or demonstrate "
                    "equivalent performance. The proposal needs an engineered pressure range and verification."
                ),
                "best": False,
            },
            {
                "label": "Option B — Automatic TBM Face Pressure with Ground Improvement Works",
                "scores": {"cs": 0, "pi": 0, "s": 0},
                "feedback": (
                    "Automation can control equipment, but “automatic” does not establish that the selected "
                    "face pressure is technically optimised for the ground and nearby assets."
                ),
                "best": False,
            },
            {
                "label": "Option C — Optimised TBM Face Pressure with Ground Improvement Works",
                "scores": {"cs": 10, "pi": 10, "s": 10},
                "feedback": (
                    "An optimised face-pressure range, supported by targeted ground improvement, is a "
                    "performance-based alternative that manages stability and settlement while improving efficiency."
                ),
                "best": True,
            },
        ],
    },
    {
        "id": "round_5_part_1",
        "round": "Round 5 · Part 1",
        "title": "Concrete and Rebar Testing Strategy",
        "prompt": (
            "Choose the materials-testing strategy for the project's large volumes of concrete and reinforcement."
        ),
        "options": [
            {
                "label": "Option A — Accredited Laboratory Testing with Minimum Code Requirements",
                "scores": {"cs": 5, "pi": 5, "s": 5},
                "feedback": (
                    "This meets minimum test frequencies, but manual or basic spreadsheet reporting is reactive "
                    "and can slow traceability, review, and construction decisions."
                ),
                "best": False,
            },
            {
                "label": "Option B — Accredited Laboratory Testing with Digital-Automatic Reporting",
                "scores": {"cs": 10, "pi": 10, "s": 10},
                "feedback": (
                    "A SAC-accredited laboratory with structured digital reporting improves traceability and "
                    "alerts the QP quickly, allowing faster verification and construction decisions."
                ),
                "best": True,
            },
            {
                "label": "Option C — Accredited Laboratory Testing with Third-Party Results",
                "scores": {"cs": 0, "pi": 0, "s": 0},
                "feedback": (
                    "Relying on other parties' results does not provide an adequate project-specific testing "
                    "and verification method for critical concrete and reinforcement works."
                ),
                "best": False,
            },
        ],
    },
    {
        "id": "round_5_part_2",
        "round": "Round 5 · Part 2",
        "title": "Concrete Cube Sampling Rate",
        "prompt": "Choose the correct sampling rate for a concrete volume of 1,000 m³.",
        "note": "Note: 1 sample = min. 2 cubes for 7 days and min. 2 cubes for 28 days.",
        "options": [
            {
                "label": "Option A — 1 sample per 100 m³",
                "scores": {"cs": 0, "pi": 0, "s": 0},
                "feedback": (
                    "The workbook associates one sample per 100 m³ with pours below 400 m³. "
                    "It is not the stated sampling rule for this 1,000 m³ case."
                ),
                "best": False,
            },
            {
                "label": "Option B — 7 samples per 1,000 m³",
                "scores": {"cs": 10, "pi": 10, "s": 10},
                "feedback": (
                    "For 1,000 m³, the workbook applies four samples for the first 400 m³ and one for each "
                    "subsequent 200 m³: 4 + 3 = 7 samples."
                ),
                "best": True,
            },
            {
                "label": "Option C — 1 sample per 100 m³ plus 7 samples per 1,000 m³",
                "scores": {"cs": 0, "pi": 0, "s": 0},
                "feedback": (
                    "This combines different sampling regimes and overstates the workbook's rule for a "
                    "1,000 m³ pour. The workbook reserves the separate maximum-sample note for larger pours."
                ),
                "best": False,
            },
        ],
    },
    {
        "id": "round_6",
        "round": "Round 6",
        "title": "Remote Site Supervision (RSS)",
        "prompt": "Choose how RSS should be introduced to enhance site supervision.",
        "options": [
            {
                "label": "Option A — Manual Inspection with Reduced Remote Supervision",
                "scores": {"cs": 0, "pi": 0, "s": 0},
                "feedback": (
                    "This reverses the intended role of RSS. Remote supervision should increase as a tool "
                    "that supports efficient, risk-based reductions in manual inspection."
                ),
                "best": False,
            },
            {
                "label": "Option B — Reduced Site-Supervisor Deployment with CCTV and Technology",
                "scores": {"cs": 10, "pi": 10, "s": 10},
                "feedback": (
                    "CCTV and supporting technology can maintain oversight and records while enabling a "
                    "carefully managed reduction in on-site supervisor deployment."
                ),
                "best": True,
            },
            {
                "label": "Option C — CCTV Helps to Reduce Site Safety",
                "scores": {"cs": 0, "pi": 0, "s": 0},
                "feedback": (
                    "RSS may reduce manual inspection effort, but it must not reduce the required level of "
                    "site safety. Safety outcomes and obligations remain unchanged."
                ),
                "best": False,
            },
        ],
    },
]
