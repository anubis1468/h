import os
import shutil
import subprocess
from textwrap import dedent

# -----------------------------
# CONFIG — UPDATE THIS LINE ONLY
# -----------------------------
GITHUB_REPO_URL = "https://github.com/anubis1468/h.git"
ROOT = "surgecoin_hybrid_repo"
# -----------------------------

def write(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(dedent(content).lstrip())

def regen_repo():
    if os.path.exists(ROOT):
        shutil.rmtree(ROOT)

    os.makedirs(ROOT, exist_ok=True)

    # -----------------------------
    # ROOT README
    # -----------------------------
    write(f"{ROOT}/README.md", """
    # SurgeCoin Hybrid Ecosystem

    SurgeCoin is the world’s first dual‑mining crypto gaming ecosystem, combining:
    - Virtual in‑game mining
    - Real GPU‑powered mining
    - A unified, player‑owned token economy

    This repository contains:
    - Website content
    - Whitepaper
    - Docs (GitHub + GitBook‑style)
    - Pitch deck
    - Tokenomics
    - UI kit
    - Investor + press materials
    - Community launch assets
    """)

    # -----------------------------
    # GitHub Pages index
    # -----------------------------
    write(f"{ROOT}/index.md", """
    ---
    title: SurgeCoin Hybrid Ecosystem
    ---

    # SurgeCoin Hybrid Ecosystem

    **Mine in the game. Mine in the real world. Earn everywhere.**

    ## Explore
    - [Whitepaper](core/SurgeCoin_Hybrid_Whitepaper.md)
    - [Docs](docs/README.md)
    - [GitBook‑style Docs](gitbook/SUMMARY.md)
    - [GPU Miner Landing Page](landing/SurgeCoin_GPU_Miner_Landing_Page.md)
    - [UI Kit](ui-kit/SurgeCoin_UI_Kit.md)
    - [Investor One‑Pager](investor/SurgeCoin_Investor_One_Pager.md)
    - [Press Kit](press/SurgeCoin_Press_Kit.md)
    """)

    # -----------------------------
    # .gitignore
    # -----------------------------
    write(f"{ROOT}/.gitignore", """
    __pycache__/
    *.pyc
    .DS_Store
    .idea/
    .vscode/
    """)

    # -----------------------------
    # GitHub Actions workflow
    # -----------------------------
    write(f"{ROOT}/.github/workflows/pages.yml", """
    name: Deploy GitHub Pages

    on:
      push:
        branches: [ main ]

    permissions:
      contents: read
      pages: write
      id-token: write

    jobs:
      deploy:
        runs-on: ubuntu-latest
        steps:
          - name: Checkout
            uses: actions/checkout@v4

          - name: Setup Pages
            uses: actions/configure-pages@v4

          - name: Upload artifact
            uses: actions/upload-pages-artifact@v3
            with:
              path: .

          - name: Deploy to GitHub Pages
            uses: actions/deploy-pages@v4
    """)

    # -----------------------------
    # CORE FILES
    # -----------------------------
    write(f"{ROOT}/core/SurgeCoin_Hybrid_Website.md", "FULL WEBSITE CONTENT HERE…")
    write(f"{ROOT}/core/SurgeCoin_Hybrid_Whitepaper.md", "FULL WHITEPAPER CONTENT HERE…")
    write(f"{ROOT}/core/README.txt", "Core SurgeCoin Hybrid Ecosystem Files")

    # -----------------------------
    # PITCH DECK
    # -----------------------------
    write(f"{ROOT}/pitch_deck/SurgeCoin_Hybrid_Pitch_Deck.md", "FULL PITCH DECK CONTENT HERE…")

    # -----------------------------
    # TOKENOMICS CSV
    # -----------------------------
    write(f"{ROOT}/tokenomics/SurgeCoin_Tokenomics.csv", """
    Category,Allocation (%),Description,Notes
    Total Supply,100%,Fixed supply across both tokens,Governance controlled
    SurgeCoin (SCN),60%,Primary in-game currency,Earned via virtual mining
    SurgeCoin-GPU (SCN-G),40%,GPU-mined token,Earned via GPU miner
    """)

    # -----------------------------
    # DOCS
    # -----------------------------
    write(f"{ROOT}/docs/README.md", "# SurgeCoin Docs")
    write(f"{ROOT}/docs/getting-started.md", "# Getting Started")
    write(f"{ROOT}/docs/architecture.md", "# Architecture")
    write(f"{ROOT}/docs/tokenomics.md", "# Tokenomics")

    # -----------------------------
    # GITBOOK
    # -----------------------------
    write(f"{ROOT}/gitbook/SUMMARY.md", """
    # Summary
    - [Introduction](intro.md)
    - [Getting Started](getting-started.md)
    - [Ecosystem](ecosystem.md)
    - [Mining](mining.md)
    - [Tokenomics](tokenomics.md)
    - [Security](security.md)
    - [Roadmap](roadmap.md)
    """)

    write(f"{ROOT}/gitbook/intro.md", "# Introduction")
    write(f"{ROOT}/gitbook/getting-started.md", "# Getting Started")
    write(f"{ROOT}/gitbook/ecosystem.md", "# Ecosystem")
    write(f"{ROOT}/gitbook/mining.md", "# Mining")
    write(f"{ROOT}/gitbook/tokenomics.md", "# Tokenomics")
    write(f"{ROOT}/gitbook/security.md", "# Security")
    write(f"{ROOT}/gitbook/roadmap.md", "# Roadmap")

    # -----------------------------
    # UI KIT
    # -----------------------------
    write(f"{ROOT}/ui-kit/SurgeCoin_UI_Kit.md", "# SurgeCoin UI Kit")

    # -----------------------------
    # INVESTOR + PRESS
    # -----------------------------
    write(f"{ROOT}/investor/SurgeCoin_Investor_One_Pager.md", "# Investor One‑Pager")
    write(f"{ROOT}/press/SurgeCoin_Press_Kit.md", "# Press Kit")

    # -----------------------------
    # COMMUNITY
    # -----------------------------
    write(f"{ROOT}/community/SurgeCoin_Community_Launch_Announcement.md", "# Community Launch Announcement")

    print("Repo regenerated successfully.")

def git_push():
    subprocess.run(["git", "init"], cwd=ROOT)
    subprocess.run(["git", "add", "."], cwd=ROOT)
    subprocess.run(["git", "commit", "-m", "Automated SurgeCoin Hybrid Redeploy"], cwd=ROOT)
    subprocess.run(["git", "branch", "-M", "main"], cwd=ROOT)
    subprocess.run(["git", "remote", "add", "origin", GITHUB_REPO_URL], cwd=ROOT)
    subprocess.run(["git", "push", "-f", "origin", "main"], cwd=ROOT)

    print("Force‑pushed to GitHub. GitHub Pages will auto‑deploy.")

if __name__ == "__main__":
    regen_repo()
    git_push()

