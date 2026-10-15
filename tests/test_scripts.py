"""Tests for validate_skill.py and package_skill.py. Run: python -m unittest discover tests"""
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "skill-forge-ultra" / "scripts"))
from validate_skill import validate  # noqa: E402
import package_skill  # noqa: E402

GOOD_DESC = ("Writes weekly status reports from bullet notes with highlights, risks, and next steps. "
             "Use whenever the user wants a status update, weekly report, or progress summary.")


def make_skill(tmp, name="demo-skill", fm=None, body="# Demo\n\nDo the thing.\n", files=None):
    d = Path(tmp) / name
    d.mkdir(parents=True)
    fm = fm if fm is not None else f"name: {name}\ndescription: {GOOD_DESC}"
    (d / "SKILL.md").write_text(f"---\n{fm}\n---\n{body}", encoding="utf-8")
    for rel, content in (files or {}).items():
        p = d / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(content, encoding="utf-8")
    return d


class ValidateTests(unittest.TestCase):
    def test_main_skill_is_valid(self):
        errors, warnings, _ = validate(ROOT / "skill-forge-ultra")
        self.assertEqual(errors, [])
        self.assertEqual(warnings, [])

    def test_examples_are_valid(self):
        for d in (ROOT / "examples").iterdir():
            if d.is_dir():
                errors, _, _ = validate(d)
                self.assertEqual(errors, [], d.name)

    def test_good_minimal(self):
        with tempfile.TemporaryDirectory() as t:
            errors, _, stats = validate(make_skill(t))
            self.assertEqual(errors, [])
            self.assertEqual(stats["name"], "demo-skill")

    def test_missing_frontmatter(self):
        with tempfile.TemporaryDirectory() as t:
            d = Path(t) / "x"
            d.mkdir()
            (d / "SKILL.md").write_text("# no frontmatter")
            errors, _, _ = validate(d)
            self.assertTrue(any("frontmatter" in e for e in errors))

    def test_bad_name(self):
        with tempfile.TemporaryDirectory() as t:
            d = make_skill(t, fm=f"name: Bad Name\ndescription: {GOOD_DESC}")
            self.assertTrue(any("kebab" in e for e in validate(d)[0]))

    def test_angle_brackets_and_extra_key(self):
        with tempfile.TemporaryDirectory() as t:
            d = make_skill(t, fm="name: demo-skill\ndescription: Use when <x>\nversion: 1")
            errors = validate(d)[0]
            self.assertTrue(any("angle" in e for e in errors))
            self.assertTrue(any("Disallowed" in e for e in errors))

    def test_missing_reference(self):
        with tempfile.TemporaryDirectory() as t:
            d = make_skill(t, body="Read `references/guide.md` first.\n")
            self.assertTrue(any("references/guide.md" in e for e in validate(d)[0]))

    def test_orphan_and_placeholder_warnings(self):
        with tempfile.TemporaryDirectory() as t:
            d = make_skill(t, body="Do {Something} here. TODO\n", files={"references/unused.md": "x"})
            warnings = validate(d)[1]
            self.assertTrue(any("never referenced" in w for w in warnings))
            self.assertTrue(any("placeholder" in w for w in warnings))

    def test_short_description_warns(self):
        with tempfile.TemporaryDirectory() as t:
            d = make_skill(t, fm="name: demo-skill\ndescription: Helps.")
            self.assertTrue(any("undertrigger" in w for w in validate(d)[1]))

    def test_duplicate_lines_warn(self):
        with tempfile.TemporaryDirectory() as t:
            line = "Always verify every factual claim before delivering the final answer.\n"
            d = make_skill(t, body=line * 2)
            self.assertTrue(any("duplicated" in w for w in validate(d)[1]))


class PackageTests(unittest.TestCase):
    def test_packages_valid_skill(self):
        with tempfile.TemporaryDirectory() as t:
            d = make_skill(t, body="See `references/a.md`.\n", files={"references/a.md": "ref"})
            out = Path(t) / "out"
            self.assertEqual(package_skill.main(["p", str(d), str(out)]), 0)
            with zipfile.ZipFile(out / "demo-skill.skill") as z:
                self.assertIn("demo-skill/SKILL.md", z.namelist())
                self.assertIn("demo-skill/references/a.md", z.namelist())

    def test_refuses_invalid_skill(self):
        with tempfile.TemporaryDirectory() as t:
            d = make_skill(t, fm="name: demo-skill")
            self.assertEqual(package_skill.main(["p", str(d), str(Path(t) / "out")]), 1)


if __name__ == "__main__":
    unittest.main()
