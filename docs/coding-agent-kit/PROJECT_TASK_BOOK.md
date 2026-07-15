# Agent Framework Coding Agent Kit 长程任务书

## 计划元数据

- Plan ID: `AF-CAK-2026-001`
- Version: `v1`
- Last updated: `2026-07-15 Asia/Shanghai`
- Canonical progress file: `docs/coding-agent-kit/PROJECT_TASK_BOOK.md`
- Related handoff file: `none`
- Current branch: `codex/agent-framework-coding-agent-kit`
- Current active phase: `Phase 5: 开源就绪验证`
- Execution readiness: `executing`

## 目标

在 `microsoft/agent-framework` 上游提交 `c47f20d9a28d18b0a3f284c8a8365ff72f2e35b1` 基础上，建设一个可独立上传至 GitHub、面向多项目使用的 Coding Agent 开发套件。套件应让 coding agent 在实现 MAF 细节时快速获得匹配语言和版本的官方说明、参考设计、样例、源码与测试入口，同时避免在无关项目中隐式触发。

## 范围与约束

- In scope:
  - 将现有 kit 集成到独立上游分支/worktree；
  - 移除项目级 `config.toml` 依赖；
  - 重构 Skill 的触发条件、工作区解析和输出契约；
  - 为源码、样例、测试、设计文档和 Microsoft Learn 元数据建立可再生成的主题索引；
  - 提供安装、索引生成、验证、贡献与同步上游说明；
  - 保留 Codex 插件分发能力。
- Out of scope:
  - 创建 GitHub 远程仓库、fork 或 push；
  - 提交 Microsoft Learn 正文镜像；
  - 修改上游框架实现或现有样例；
  - 执行需要云凭据、模型调用或部署的测试。
- Constraints:
  - 不触碰原 checkout 中未提交的 Ollama 文件；
  - 新内容保持 MIT 上游许可兼容，并清楚标注 fork/派生关系；
  - 索引必须可重复生成，不能依赖开发者机器绝对路径；
  - Skill 只对明确的 Microsoft Agent Framework 任务触发。

## 执行阶段

### Phase 1: 上游基线与信息架构

- Purpose: 锁定上游来源、许可证、目录规模和知识层边界。
- Outputs: 独立 worktree/branch、架构决策、任务书。
- Completion criteria: 基线提交、分支、范围、非目标和索引架构明确。
- Validation: `git status --short --branch`、目录/文件统计、上游远程核验。
- Evidence: 本任务书、Git worktree、`docs/coding-agent-kit/architecture.md`。

### Phase 2: 套件仓库化与触发边界

- Purpose: 把原项目专用组件改成可跨 MAF 项目使用的开源套件。
- Outputs: 根级 `AGENTS.md`、仓库 Skill、插件清单、安装说明、开源元数据。
- Completion criteria: 无项目级 config；Skill 可从 fork 内使用或单独安装；负向触发边界明确。
- Validation: Skill/plugin schema 校验、无关任务触发测试说明、路径可移植性扫描。
- Evidence: `.agents/skills/maf-expert`、`.codex-plugin/plugin.json`、README 和验证日志。

### Phase 3: 参考代码与设计索引

- Purpose: 将数千个 C#、Python、声明式、schema、样例和测试文件变成可检索的主题目录。
- Outputs: 主题注册表、索引生成器、机器可读 JSON 和人类/agent 可读 Markdown。
- Completion criteria: 每个核心主题同时给出文档、样例、实现、测试入口；索引记录上游提交。
- Validation: 生成器重复运行无差异；路径存在性和主题覆盖检查通过。
- Evidence: `tools/coding-agent-kit/indexer`、`docs/coding-agent-kit/catalog`。

### Phase 4: 文档与知识库闭环

- Purpose: 让 Skill 能从开发意图路由到解释、参考设计、代码和验证，而不复制官方正文。
- Outputs: 主题导航、证据使用协议、知识沉淀模板、维护与 upstream 同步流程。
- Completion criteria: 从一个 agent 细节可定位 Learn 页面、上游设计、两种语言示例/实现/测试中的适用项。
- Validation: 代表性场景走查和链接检查。
- Evidence: `docs/coding-agent-kit/guides`、Skill references、验收用例。

### Phase 5: 开源就绪验证

- Purpose: 确认仓库可以被审阅、复现、分支同步并上传 GitHub。
- Outputs: 验证报告、贡献说明、发布/同步清单。
- Completion criteria: 工作树只有预期新增/修改；生成、schema、链接和安装模拟通过；边界公开。
- Validation: validator、indexer check mode、Git diff 审查、secret/absolute-path/TODO 扫描。
- Evidence: 命令输出与最终任务书进度台账。

## 决策记录

- Verified facts:
  - 上游远程为 `https://github.com/microsoft/agent-framework.git`，许可证为 MIT。
  - 基线提交为 `c47f20d9a28d18b0a3f284c8a8365ff72f2e35b1`。
  - 上游包含约 1,105 个 .NET sample 文件、807 个 Python sample 文件，以及大量实现和测试。
  - 原 checkout 有未提交 Ollama 变更，新 worktree 与其隔离。
  - 用户已有全功能 Codex 配置，不需要项目 `.codex/config.toml`。
- Active assumptions:
  - 远程仓库名称可在上传时决定，当前本地目录名不作为永久品牌约束。
  - Microsoft Learn 元数据可以提交标题、官方 URL 和章节路径，但不提交镜像正文。
- Locked decisions:
  - 项目以 upstream fork branch 形式存在，不复制上游源码到独立非 Git kit。
  - 索引由主题注册表和生成器产生，生成物与生成器一起提交。
  - Skill description 同时包含正向 MAF 触发词和明确负向边界。
  - 不使用项目级 config，也不强制 hooks；工具能力通过 Skill/Plugin dependencies 声明。
- Open questions:
  - GitHub 远程仓库最终名称、组织和默认分支在实际上传前由用户决定。
  - 是否长期保留完整 upstream history，默认建议保留以便同步。

## 关键制品与环境

- Canonical docs:
  - `docs/coding-agent-kit/PROJECT_TASK_BOOK.md`
  - `docs/coding-agent-kit/architecture.md`
- Important code or output artifacts:
  - `.agents/skills/maf-expert`: coding agent 工作流入口。
  - `tools/coding-agent-kit/indexer`: 可重复索引生成器。
  - `docs/coding-agent-kit/catalog`: 生成的参考导航。
- Required commands:
  - `python tools/coding-agent-kit/indexer/build_catalog.py`: 生成索引。
  - `python tools/coding-agent-kit/indexer/build_catalog.py --check`: 验证生成物无漂移。
  - `pwsh tools/coding-agent-kit/validate.ps1`: 验证套件。
- Environment baseline:
  - Windows PowerShell；Python 3.11+（使用标准库）；Git worktree。
  - `construction-plan-system` skill 在当前会话不可用；本任务书承载 Full 级连续性和门禁，这是已记录的流程边界。

## 进度台账

- Overall progress: 上游派生分支、套件仓库化、19 主题索引、133 页 Learn 元数据、知识模板、安装/同步/发布说明和 CI 已完成。
- Phase 1: `done`
- Phase 2: `done`
- Phase 3: `done`
- Phase 4: `done`
- Phase 5: `done`
- Validation status: 4,551 个仓库文件已索引，4,444 个被主题覆盖；catalog drift、Skill 同步、单元测试、安装 dry-run、本地链接、绝对路径、插件 schema 和 Skill schema 均通过。
- Residual risks: 自动分类是导航提示而非 API 真相；GitHub 远程名称/所有者及实际 push 尚未选择；行为级隐式触发验收需安装后在新任务运行。

## 下一步动作

由维护者审阅新分支并按 `docs/coding-agent-kit/GITHUB_PUBLISHING.md` 选择 GitHub fork/远程后发布。
