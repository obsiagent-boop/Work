**Hermes Agent Handoff & Project Restoration Guide (**rules.md**)**
  
This document provides a clear process for a human user or another AI agent to access, restore, and continue working on the projects archived from the Hermes Agent environment.
  
**1. Understanding the Archives**
  
**What is **.tar.gz**?**
Think of a .tar.gz file as a **combined moving box and vacuum-seal bag**.
  
1.  tar** (The Box):** The tar command takes many files and folders and bundles them together into a single file, like packing many small items into one big moving box. It preserves the entire folder structure.
2.  gz** (The Vacuum Seal):** The gz (gzip) command then compresses that single "box," sucking all the extra air out to make it much smaller and faster to move.
  
A .tar.gz file is simply a compressed archive that holds an entire project directory.
  
**What is Git LFS and "What Happened to My File"?**
When you look at the Data-Archive-LFS repository on the GitHub website, you will see that the large .tar.gz files are only a few hundred bytes each. This is a safety feature.
  
Think of it like a **claim ticket for a very heavy item at a warehouse.**
  
1.  **The Pointer File (The Claim Ticket):** The tiny file you see on GitHub is just a "claim ticket." It's a text file that says, "The real file is very large and is stored securely in GitHub's Large File Storage (LFS) warehouse."
2.  **LFS Storage (The Warehouse):** GitHub stores the actual, multi-megabyte .tar.gz file on special, dedicated servers designed for large data.
3.  git lfs pull** (Claiming Your Item):** When you run the git lfs pull command on your machine, you are telling Git: "Go to the LFS warehouse and redeem all these claim tickets for the real, full-sized files."
  
This process is automatic and secure. It keeps the main repository fast and clean while ensuring the large project data is safely stored and accessible.
  
**2. For a Human User: How to Restore a Project**
  
To get a project running on your own machine, follow these steps.
  
1.  **Install Prerequisites:**
    *   Install **Git** from the official website: [git-scm.com](https://git-scm.com/downloads)
    *   Install **Git LFS** from the official website: [git-lfs.github.com](https://git-lfs.github.com/)
    *   After installing, open a terminal and run git lfs install one time to activate it.
  
2.  **Clone the Archive Repository:**
```
        git clone https://github.com/obsiagent-boop/Data-Archive-LFS.git
```
  
3.  **Download the Large Files:**
    Navigate into the new directory and pull the real files from the LFS "warehouse."
```
        cd Data-Archive-LFS
    git lfs pull
```
  
4.  **Un-archive Your Project:**
    You can now un-archive any project you need using the tar command. For example, to restore the personal_agent_os project:
```
        tar -xvf personal_agent_os.tar.gz
```
    This will create the full personal_agent_os directory in your current location.
  
**3. For another AI Agent: How to Take Over**
  
To onboard a new AI agent with the same capabilities and access, provide it with these instructions.
  
**Preamble:** "You are an AI assistant taking over from a previous agent. Your primary task is to restore a project from a secure GitHub archive. You will need a GitHub Personal Access Token (PAT) with repo scope, which I will provide."
  
**Step 1: Ensure **git-lfs** is Available**
"First, you must ensure you have git-lfs. Do not use a system package manager. Download it and install it locally like this:"
```
# Download and extract the LFS binary
curl -L https://github.com/git-lfs/git-lfs/releases/download/v3.5.1/git-lfs-linux-amd64-v3.5.1.tar.gz | tar xz

# Create a local bin directory and copy the executable
mkdir -p /data/bin
cp git-lfs-3.5.1/git-lfs /data/bin/

# Add the local bin to your PATH for this session
export PATH="/data/bin:$PATH"

# Verify the installation
git lfs --version

```
  
  
**Step 2: Authenticated Clone**
"I will provide you with a GitHub PAT. Use it to clone the central Data-Archive-LFS repository:"
```
# The user will provide the <TOKEN>
git clone https://<TOKEN>@github.com/obsiagent-boop/Data-Archive-LFS.git /data/archive

```
  
  
**Step 3: Fetch LFS Data**
"The repository is now cloned. Navigate into it and pull the large files from LFS storage:"
```
cd /data/archive
git lfs pull

```
  
  
**Step 4: Un-archive a Specific Project**
"The archive is now complete. Un-archive the project we need to work on. For example, if we are working on FinceptTerminal:"
```
tar -xvf FinceptTerminal.tar.gz -C /data/

```
  
This will extract the project to /data/FinceptTerminal.
  
**Step 5: Begin Work**
"The project is now fully restored at /data/FinceptTerminal. Your task is to cd into that directory, inspect its README.md file and contents, and continue its development as instructed."
