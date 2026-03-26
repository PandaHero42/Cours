# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Context

This is a JavaScript front-end project directory within a school course repository (`Cours/`). The broader repo contains:

- `Q2/travaux pratiques/dev front-end/js/` — vanilla JS exercises
- `Q2/travaux pratiques/dev front-end/jQuery/` — jQuery exercises
- `Q2/travaux pratiques/dev_front-end_avances/` — advanced front-end notes
- `capteurs/` — Python sensor exercises (separate sub-repo)

## Project Structure

Plain HTML/CSS/JS front-end projects — no build tool, no bundler. Files are opened directly in a browser or via a local dev server (e.g. VS Code Live Server extension).

## Development

Open HTML files directly in a browser, or use the VS Code Live Server extension (already configured in the workspace).

There is no `package.json`, no npm scripts, and no test runner unless one is added to this project.

## Conventions

- French is used for comments, variable names, and content (course is taught in French).
- Inline `<script>` tags or separate `.js` files are both used depending on exercise complexity.
- No framework — vanilla JS or jQuery only.
