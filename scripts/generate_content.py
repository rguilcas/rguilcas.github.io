
import os

publications = [
    {
        "title": "Understanding biases and changes in European heavy precipitation using dynamical flow precursors",
        "date": "2025-01-01",
        "venue": "(submitted)",
        "citation": "Oldham-Dorrington, J., Li C., Sobolowski S. and Guillaume-Castel, R. . &quot;Understanding biases and changes in European heavy precipitation using dynamical flow precursors.&quot; (submitted).",
        "category": "manuscripts"
    }
]

talks = [
    {"title": "Can a neural network learn atmosphericdynamics for extreme rainfall?", "date": "2025-01-01", "venue": "Stormtracks Workshop (Poster)", "location": "Rosendal, Norway"},
    {"title": "ENSO diversity explains the interannual variability of the SST pattern effect.", "date": "2025-01-01", "venue": "CFMIP (Poster)", "location": "Exeter, UK"},
    {"title": "Assessing the impact of changing warming patterns on transient global warming", "date": "2024-01-01", "venue": "EGU General Assembly (Poster)", "location": "Vienna, Austria"},
    {"title": "Quantitative impact of the pattern effect on historical warming", "date": "2024-01-01", "venue": "CFMIP (Poster)", "location": "Boston, MA, USA"},
    {"title": "The SST pattern effect on the TCR", "date": "2023-01-01", "venue": "CFMIP–GASS Meeting (Talk)", "location": "Paris, France"},
    {"title": "Dynamics of the global energy budget with a time–dependent climate feedback parameter", "date": "2022-01-01", "venue": "International Radiation Symposium (Talk)", "location": "Thessaloniki, Greece"},
    {"title": "Dynamics of the Earth energy budget with a variable climate feedback parameter", "date": "2022-01-01", "venue": "EGU General Assembly (Virtual Talk)", "location": "Vienna, Austria"},
    {"title": "Climate sensitivity with a time dependent climate feedback parameter.", "date": "2022-01-01", "venue": "Pattern Effect Workshop (Poster)", "location": "Boulder, CO, USA"},
    {"title": "Dynamics of the Global Energy Budget with a time–dependent Climate Feedback Parameter", "date": "2021-01-01", "venue": "AGU Fall Meeting (Virtual Poster)", "location": "New Orleans, LA, USA"},
]

teaching = [
    {"title": "Machine Learning for Geosciences", "date": "2025-01-01", "type": "Instructor", "venue": "Geophysical Institute, University of Bergen, Norway", "description": "Evening Courses teaching students from first year undergraduates to PhDs"},
    {"title": "Master's intern Lisa Valette", "date": "2025-01-01", "type": "Co-supervisor", "venue": "Geophysical Institute, University of Bergen, Norway", "description": "Constraining European extreme rainfall projections"},
    {"title": "Master's interns Zoé Pelletier and Matthias Hersent", "date": "2022-01-01", "type": "Supervisor", "venue": "LEGOS, CNRS, France", "description": "Earth's energy budget; data analysis in Python."},
    {"title": "Python for Probabilities and Statistics", "date": "2021-01-01", "type": "Teaching Assistant", "venue": "Université Toulouse III, France", "description": "First-year undergraduate course."},
    {"title": "Python for data analysis in geosciences", "date": "2020-01-01", "type": "CNRS Internal Instructor", "venue": "Observatoire Midi-Pyrénées, CNRS, France", "description": "Short courses and workshops including data analysis and visualization."},
    {"title": "High school Physics and English", "date": "2015-01-01", "type": "Teacher", "venue": "Bac Ninh High School, Vietnam", "description": "High school teaching abroad."},
]

base_dir = "/Users/robin/Library/CloudStorage/OneDrive-UniversityofBergen/Documents/Travail/Website/my-research-website"

def write_md(path, content):
    print(f"Writing to {path}")
    with open(path, "w") as f:
        f.write(content)

for pub in publications:
    slug = pub['title'].replace(" ", "-").replace(",", "").replace(".", "")[:50]
    content = f"""---
title: "{pub['title']}"
collection: publications
category: {pub['category']}
permalink: /publication/{pub['date']}-{slug}
date: {pub['date']}
venue: '{pub['venue']}'
citation: '{pub['citation']}'
---
"""
    write_md(os.path.join(base_dir, "_publications", f"{pub['date']}-{slug}.md"), content)

for talk in talks:
    slug = talk['title'].replace(" ", "-").replace(",", "").replace(".", "")[:50]
    content = f"""---
title: "{talk['title']}"
collection: talks
type: "Talk"
permalink: /talks/{talk['date']}-{slug}
venue: "{talk['venue']}"
date: {talk['date']}
location: "{talk['venue']}"
---
"""
    write_md(os.path.join(base_dir, "_talks", f"{talk['date']}-{slug}.md"), content)

for teach in teaching:
    slug = teach['title'].replace(" ", "-").replace(",", "").replace(".", "")[:50]
    content = f"""---
title: "{teach['title']}"
collection: teaching
type: "{teach['type']}"
permalink: /teaching/{teach['date']}-{slug}
venue: "{teach['venue']}"
date: {teach['date']}
location: "{teach['venue']}"
---

{teach['description']}
"""
    write_md(os.path.join(base_dir, "_teaching", f"{teach['date']}-{slug}.md"), content)

print("Done generating content.")
