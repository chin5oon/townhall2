# Townhall Game — Rounds 4–6

A standalone interactive decision game for an underground MRT construction proposal. It can be played independently or after Rounds 1–3. Players receive immediate scoring and feedback, plus the recommended option when needed.

## Included rounds

- Round 4: Tunnelling Works
- Round 5: Concrete and Rebar Testing
  - Part 1: Testing strategy
  - Part 2: Concrete cube sampling rate
- Round 6: Remote Site Supervision

The source workbook gives Round 5 two separate decisions, so this app contains three rounds and four decision screens.

## Files

- `streamlit_app.py` — app interface and game flow
- `game_data.py` — editable questions, choices, scores, and explanations
- `requirements.txt` — pinned Python dependency
- `.streamlit/config.toml` — visual theme
- `.gitignore` — files Git should ignore

## Run locally

Python 3.12 is recommended.

```bash
python -m venv .venv
```

Activate the environment on Windows:

```powershell
.venv\Scripts\Activate.ps1
```

Or on macOS/Linux:

```bash
source .venv/bin/activate
```

Install and run:

```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```

## Upload to GitHub

1. Create an empty GitHub repository.
2. Upload **the contents of this folder** so that `streamlit_app.py` and `requirements.txt` are in the repository root.
3. Commit the files to the `main` branch.

Command-line alternative:

```bash
git init
git add .
git commit -m "Add Townhall Game Rounds 4-6"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
git push -u origin main
```

## Deploy on Streamlit Community Cloud

1. Sign in at [share.streamlit.io](https://share.streamlit.io/).
2. Select **Create app** and choose the GitHub repository.
3. Set the branch to `main` and the entrypoint to `streamlit_app.py`.
4. In Advanced settings, select Python 3.12.
5. Deploy.

No secrets, database, or Excel file are required.

## Edit the game

All game content is in `game_data.py`. Keep exactly one option per question with `"best": True`. Scores use:

- `cs` — Cost Saving
- `pi` — Productivity & Innovation
- `s` — Safety in Design & Construction

After editing, run the app locally and complete every question once before pushing the update.
