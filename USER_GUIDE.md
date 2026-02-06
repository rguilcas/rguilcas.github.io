# Website Maintenance Guide

This guide explains how to update the content of your new `al-folio` based website.

## 1. Publications (`_bibliography/papers.bib`)
The most important change is that **publications are now generated automatically from a BibTeX file**, rather than being written manually in Markdown.

*   **File location**: `_bibliography/papers.bib`
*   **How to add a paper**:
    1.  Get the BibTeX citation for your paper (from Google Scholar, journal website, etc.).
    2.  Open `_bibliography/papers.bib`.
    3.  Paste the BibTeX entry into the file.
    4.  **Important**: To make a paper appear in the "Selected Publications" section on the homepage, add `selected={true}` to the BibTeX entry.

    ```bibtex
    @article{einstein1905relativity,
      title={On the electrodynamics of moving bodies},
      author={Einstein, Albert},
      journal={Annalen der Physik},
      year={1905},
      selected={true}  <-- Adds to homepage
    }
    ```

## 2. Homepage & About Me (`_pages/about.md`)
Your homepage content and profile information are managed in this file.

*   **File location**: `_pages/about.md`
*   **Profile Picture**:
    *   Replace the image at `assets/img/prof_pic.png` (or `.jpg`).
    *   Update the filename in `_pages/about.md` under the `profile:` section if the name changes.
*   **Bio Text**:
    *   Edit the text below the `profile:` block. This is standard Markdown.
*   **News**:
    *   News items are stored in `_news/`. To add a news item, create a new markdown file there or use the `inline` news feature if configured.

## 3. CV (`_pages/cv.md`)
Your CV allows for a structured layout.

*   **File location**: `_pages/cv.md`
*   **How to edit**:
    *   The file is written in standard Markdown / HTML.
    *   You can copy-paste from your old CV file or use the `al-folio` specific structure (if you choose to use the data-driven CV features in the future, they are located in `_data/cv.yml`, but currently your CV is a static markdown page).

## 4. Blog Posts (`_posts/`)
*   **Location**: `_posts/`
*   **Format**: Filenames must follow `YYYY-MM-DD-title.md`.
*   **Content**: Standard Jekyll posts with front matter.
    ```yaml
    ---
    layout: post
    title:  "My New Post"
    date:   2026-02-03 12:00:00
    categories: blog update
    ---
    Content goes here...
    ```

## 5. Projects (`_projects/`)
*   **Location**: `_projects/`
*   **How to add**: Create a markdown file for each project. See existing examples or the `al-folio` documentation for front matter options (images, redirects, etc.).

## 6. Testing Locally
To accept changes and preview them on your computer before deploying:

1.  Open Terminal.
2.  Navigate to your site folder: `cd "/Users/robin/Library/CloudStorage/OneDrive-UniversityofBergen/Documents/Travail/Site web/rguilcas.github.io"`
3.  Run the server:
    ```bash
    bundle exec jekyll serve
    ```
4.  Open `http://127.0.0.1:4000` in your web browser.

**Tip**: If you just want to check if the site builds correctly without starting a server, you can run:
```bash
bundle exec jekyll build
```

## 7. Deploying to GitHub
Once you are happy with your changes:

1.  **Stage changes**: `git add .`
2.  **Commit**: `git commit -m "Description of changes"`
3.  **Push**: `git push`

GitHub Actions will automatically rebuild and deploy your site to the `gh-pages` branch.
