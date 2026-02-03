#!/usr/bin/env python3
"""
Pickit — one-click random unseen subfolder opener
Completely silent, no popups, no console, just opens folder.
"""

import os
import sys
import secrets
from pathlib import Path
from fnmatch import fnmatch

try:
    import asana
    ASANA_AVAILABLE = True
except ImportError:
    ASANA_AVAILABLE = False


class Pickit:
    EXCLUDE_FILE = "pickit_exclude.txt"

    def __init__(self):
        self.project_dir = self._get_project_dir()
        if not self.project_dir:
            sys.exit(1)

        self.exclude_path = self._get_exclude_path()
        self.excludes, self.ignore_patterns = self._load_excludes_and_patterns()

        # Asana — only active if PAT + library present
        self.asana_enabled = False
        self.projects_api = None
        self.stories_api = None

        if ASANA_AVAILABLE and os.environ.get("ASANA_PAT"):
            try:
                cfg = asana.Configuration()
                cfg.access_token = os.environ["ASANA_PAT"]
                client = asana.ApiClient(cfg)
                self.projects_api = asana.ProjectsApi(client)
                self.stories_api = asana.StoriesApi(client)
                self.asana_enabled = True
            except Exception:
                pass

    def _get_project_dir(self) -> Path | None:
        proj = os.environ.get("PROJECT") or os.environ.get("project")
        if not proj:
            return None
        p = Path(proj).resolve()
        return p if p.is_dir() else None

    def _get_exclude_path(self) -> Path:
        tmp = os.environ.get("TMP") or os.environ.get("TEMP") or ""
        return Path(tmp) / self.EXCLUDE_FILE if tmp else Path.home() / self.EXCLUDE_FILE

    def _load_excludes_and_patterns(self) -> tuple[set[str], list[str]]:
        if not self.exclude_path.is_file():
            return set(), []
        excluded = set()
        patterns = []
        with self.exclude_path.open(encoding="utf-8", errors="replace") as f:
            for line in f:
                line = line.rstrip()
                if not line.strip():
                    continue
                if line.startswith("!"):
                    pat = line[1:].strip()
                    if pat:
                        patterns.append(pat)
                else:
                    excluded.add(line)
        return excluded, patterns

    def _save_excludes(self) -> None:
        try:
            tmp = self.exclude_path.with_suffix(".tmp")
            with tmp.open("w", encoding="utf-8", newline="\n") as f:
                for name in sorted(self.excludes):
                    f.write(f"{name}\n")
            tmp.replace(self.exclude_path)
        except Exception:
            pass

    def _leave_asana_note(self, folder_name: str) -> None:
        if not self.asana_enabled:
            return
        try:
            # minimal: just post comment if project name matches
            ws = asana.WorkspacesApi(self.projects_api.api_client).get_workspaces()
            if not ws.data:
                return
            w_gid = ws.data[0].gid
            projects = self.projects_api.get_projects({"workspace": w_gid})
            proj = next((p for p in projects if p.name == folder_name), None)
            if proj:
                ts = os.times()  # cheap timestamp
                text = f"Housekeeping: {ts}"
                self.stories_api.create_story_for_project(
                    proj.gid, {"data": {"text": text}}
                )
        except Exception:
            pass

    def pick_and_open(self):
        try:
            entries = [e for e in self.project_dir.iterdir() if e.is_dir()]
        except Exception:
            return

        folders = []
        for e in entries:
            name = e.name
            if name.startswith((".", "_")):
                continue
            if any(fnmatch(name, p) for p in self.ignore_patterns):
                continue
            folders.append(e)

        if not folders:
            return

        unseen = [f for f in folders if f.name not in self.excludes]
        if not unseen:
            self.excludes.clear()
            unseen = folders

        chosen = secrets.choice(unseen)
        self.excludes.add(chosen.name)
        self._save_excludes()

        # Optional Asana note (silent)
        self._leave_asana_note(chosen.name)

        # Open folder — silent
        try:
            os.startfile(str(chosen))
        except Exception:
            pass  # really don't care


def main():
    Pickit().pick_and_open()


if __name__ == "__main__":
    main()