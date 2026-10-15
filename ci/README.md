# Enable CI

Move this file into place to run tests, validation, and packaging on every push:

```bash
mkdir -p .github/workflows && git mv ci/validate.yml .github/workflows/validate.yml
git commit -m "ci: enable validate workflow" && git push
```

(Pushing workflow files requires a token with the `workflow` scope, or do it via the GitHub web UI.)
