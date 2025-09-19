import re

def parse_transcript(text: str):
    lines = [l.strip() for l in re.split(r"[.\n]", text) if l.strip()]
    resume = {"name": "", "education": [], "experience": [], "skills": [], "summary": ""}

    for line in lines:
        l = line.lower()
        if not resume["name"] and ("i am" in l or "my name is" in l):
            resume["name"] = line
        elif any(x in l for x in ["bachelor", "master", "university", "college", "degree"]):
            resume["education"].append(line)
        elif any(x in l for x in ["worked", "experience", "company", "intern"]):
            resume["experience"].append(line)
        elif any(x in l for x in ["skills", "proficient", "expert", "familiar"]):
            resume["skills"].extend([s.strip() for s in re.split(r",|and", line) if s.strip()])
        else:
            resume["summary"] += line + " "
    return resume
