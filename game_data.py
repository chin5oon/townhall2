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
                "feedback": "“Built-in face pressure” does not define a controllable design method",
                "best": False,
            },
            {
                "label": "Option B — Automatic TBM Face Pressure  with Ground Improvement Works",
                "scores": {"cs": 0, "pi": 0, "s": 0},
                "feedback": (
                    "Automation can control tunneling process, but “automatic” does not establish that the "
                    "selected face pressure is technically optimised for the ground and safe for nearby assets."
                ),
                "best": False,
            },
            {
                "label": "Option C — Optimised TBM Face Pressure  with Ground Improvement Works",
                "scores": {"cs": 10, "pi": 10, "s": 10},
                "feedback": (
                    "An optimised face-pressure range, supported by targeted ground improvement, is a "
                    "performance-based alternative that manages stability (safety) and settlement while "
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
                    "While this proposal is the safest option, it would result in excessive and repetitive "
                    "sampling, leading to an unproductive use of precious resources"
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
                    "SAC-accredited laboratory testing during shipment and batch declaration will reduce "
                    "excessive and redundant site-level testing, while ensuring good quality records that "
                    "are easily retrievable by the QP and site supervisors"
                ),
                "best": True,
            },
            {
                "label": "Option C — Full Reliance on Supplier to ensure requirement are made",
                "scores": {"cs": 0, "pi": 0, "s": 0},
                "feedback": (
                    "Relying on the supplier alone is not safe without verification that the product has "
                    "been manufactured under an established conformity assessment scheme"
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
                    "This is based on a sampling rate of 1 sample per 100m³, which is only applicable for "
                    "the first 400m³, and therefore this is not the correct answer"
                ),
                "best": False,
            },
            {
                "label": "Option B — 7 samples",
                "scores": {"cs": 10, "pi": 10, "s": 10},
                "feedback": (
                    "For 1,000m³, the unified standard proposal requires 4 samples for the first 400m³ and "
                    "3 samples for the remaining 600m³ (1 sample per 200m³): 4 + 3 = 7 samples"
                ),
                "best": True,
            },
            {
                "label": "Option C — 5 samples",
                "scores": {"cs": 0, "pi": 0, "s": 0},
                "feedback": (
                    "This is based on a sampling rate of 1 sample per 200m³, which is only applicable for "
                    "volumes above 400m³ (for the initial 400m³, the sampling rate is 1 sample per 100m³), "
                    "and therefore this is not the correct answer."
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
                "label": "Option A — Manual Inspection and reduced remote supervision scheme",
                "scores": {"cs": 0, "pi": 0, "s": 0},
                "feedback": (
                    "This reverses the intended role of RSS. Remote supervision should increase as a tool "
                    "that supports efficient and productive deployment of our limited pool of supervisors"
                ),
                "best": False,
            },
            {
                "label": "Option B — Reduced site supervisor deployment with CCTV and technology",
                "scores": {"cs": 10, "pi": 10, "s": 10},
                "feedback": (
                    "CCTV and supporting technology can maintain oversight and records while enabling a "
                    "carefully managed reduction in on-site supervisor deployment. Technology can also help "
                    "the builder delivey compliance work upstream."
                ),
                "best": True,
            },
            {
                "label": "Option C —  With CCTV, a lower of site safety is acceptable",
                "scores": {"cs": 0, "pi": 0, "s": 0},
                "feedback": (
                    "CCTV will reduce manual inspection effort, but must not compromise the required level of "
                    "site safety. Safety outcomes and obligations remain unchanged. In fact, it will improve "
                    "safety outcomes by providing real-time situational awareness and acting as a behavioural "
                    "deterrent"
                ),
                "best": False,
            },
        ],
    },
]
