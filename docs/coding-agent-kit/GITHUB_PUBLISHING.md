# GitHub publishing checklist

The local branch is prepared as a derivative of `microsoft/agent-framework`. Publishing is an explicit maintainer action; the kit does not create a remote repository or push automatically.

## Before publishing

1. Choose the repository owner/name and decide whether GitHub should create it as a fork or a separate derivative repository.
2. Prefer a GitHub fork when retaining upstream history and regular synchronization is important.
3. Keep the upstream MIT `LICENSE`, attribution, security policy, code of conduct, and contribution files.
4. Review `git diff` and confirm no Microsoft Learn page bodies, credentials, local absolute paths, caches, or unrelated upstream changes are present.
5. Run `python tools/coding-agent-kit/validate.py`.
6. Commit generated catalog files with their registry/indexer changes.

## Remote layout

Recommended after creating the GitHub fork:

```bash
git remote rename origin upstream
git remote add origin https://github.com/<owner>/<repository>.git
git push -u origin codex/agent-framework-coding-agent-kit
```

After review, choose whether to keep this as a feature branch or make a kit-focused branch the fork's default branch. Do not push to `microsoft/agent-framework`; the upstream remote should remain fetch-oriented for this project.

## Repository description suggestion

> A coding-agent development kit built on Microsoft Agent Framework, with indexed documentation, designs, samples, source, and tests for production-grade .NET and Python agent systems.

Suggested topics: `microsoft-agent-framework`, `coding-agent`, `agentic-ai`, `python`, `dotnet`, `multi-agent`, `workflows`, `mcp`, `a2a`, `evaluation`.
