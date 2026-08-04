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
                    "“Built-in face pressure” does not define a controllable design method. The proposal "
                    "needs an engineered pressure range and verification."
                ),
                "best": False,
            },
            {
                "label": "Option B — Automatic TBM Face Pressure with Ground Improvement Works",
                "scores": {"cs": 0, "pi": 0, "s": 0},
                "feedback": (
                    "Automation can control the tunnelling process, but “automatic” does not establish that "
                    "the selected face pressure is technically optimised for the ground or safe for nearby assets."
                ),
                "best": False,
            },
            {
                "label": "Option C — Optimised TBM Face Pressure with Ground Improvement Works",
                "scores": {"cs": 10, "pi": 10, "s": 10},
                "feedback": (
                    "An optimised face-pressure range, supported by targeted ground improvement, is a "
                    "performance-based alternative that manages stability, safety, and settlement while "
                    "improving efficiency."
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
                "label": "Option A — Accredited Laboratory Testing with Random Site Testing",
                "scores": {"cs": 5, "pi": 5, "s": 10},
                "feedback": (
                    "This is the safest option in isolation, but excessive and repetitive sampling would "
                    "use resources unproductively."
                ),
                "best": False,
            },
            {
                "label": (
                    "Option B — Accredited Laboratory Testing with Batch Declaration "
                    "and Shipment Approval"
                ),
                "scores": {"cs": 10, "pi": 10, "s": 10},
                "feedback": (
                    "SAC-accredited laboratory testing during shipment and batch declaration reduces "
                    "excessive, redundant site-level testing while maintaining quality records that are "
                    "easy for the QP and site supervisors to retrieve."
                ),
                "best": True,
            },
            {
                "label": "Option C — Full Reliance on the Supplier for Compliance",
                "scores": {"cs": 0, "pi": 0, "s": 0},
                "feedback": (
                    "Relying on the supplier alone is unsafe without verifying that the product was "
                    "manufactured under an established conformity-assessment scheme."
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
        "options": [
            {
                "label": "Option A — 10 samples",
                "scores": {"cs": 0, "pi": 0, "s": 0},
                "feedback": (
                    "This applies one sample per 100 m³ to the entire pour, but that rate applies only "
                    "to the first 400 m³. It is therefore not the correct answer."
                ),
                "best": False,
            },
            {
                "label": "Option B — 7 samples",
                "scores": {"cs": 10, "pi": 10, "s": 10},
                "feedback": (
                    "For 1,000 m³, the unified standard proposal requires four samples for the first "
                    "400 m³ and three for the remaining 600 m³ at one sample per 200 m³: 4 + 3 = 7."
                ),
                "best": True,
            },
            {
                "label": "Option C — 5 samples",
                "scores": {"cs": 0, "pi": 0, "s": 0},
                "feedback": (
                    "This applies one sample per 200 m³ to the entire pour, but that rate applies only "
                    "after the first 400 m³. It is therefore not the correct answer."
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
                "label": "Option A — Manual Inspection with a Reduced Remote-Supervision Scheme",
                "scores": {"cs": 0, "pi": 0, "s": 0},
                "feedback": (
                    "This reverses the intended role of RSS. Remote supervision should increase as a tool "
                    "that supports efficient and productive deployment of the limited pool of supervisors."
                ),
                "best": False,
            },
            {
                "label": "Option B — Reduced Site-Supervisor Deployment with CCTV and Technology",
                "scores": {"cs": 10, "pi": 10, "s": 10},
                "feedback": (
                    "CCTV and supporting technology can maintain oversight and records while enabling a "
                    "carefully managed reduction in on-site supervisor deployment. Technology can also help "
                    "the builder deliver compliance work upstream."
                ),
                "best": True,
            },
            {
                "label": "Option C — With CCTV, a Lower Level of Site Safety Is Acceptable",
                "scores": {"cs": 0, "pi": 0, "s": 0},
                "feedback": (
                    "CCTV can reduce manual inspection effort, but it must not compromise the required level "
                    "of site safety. Safety obligations remain unchanged; real-time situational awareness "
                    "and behavioural deterrence can improve safety outcomes."
                ),
                "best": False,
            },
        ],
    },
]
