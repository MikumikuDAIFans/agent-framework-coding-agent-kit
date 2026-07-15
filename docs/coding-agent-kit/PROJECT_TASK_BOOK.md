# Agent Framework Coding Agent Kit 长期任务书

## 计划元数据

- Plan ID: `AF-CAK-2026-001`
- Version: `v2`
- Last updated: `2026-07-15 Asia/Shanghai`
- Canonical progress file: `docs/coding-agent-kit/PROJECT_TASK_BOOK.md`
- Related handoff file: `none`
- Current branch: `codex/agent-framework-coding-agent-kit`
- Current active phase: `Phase 7: 逐项来源审核`
- Execution readiness: `executing`
- Lifecycle route: `research/prototype -> review -> curated maintenance`
- Development method: `source-driven`，叠加 `review/quality`
- Scale: `Standard`

## 目标

在 `microsoft/agent-framework` 上游历史和本地系统性代码索引之上，持续建设一套面向 coding
agent 的 Microsoft Agent Framework 开发知识系统。对于每个具体开发细节，系统应优先提供匹配
语言、版本和成熟度的官方说明、设计依据、样例、实现与测试；外部社区资料必须先经过逐项审核，
才能成为推荐参考，避免把过时 API、演示捷径或未经验证的社区结论当作框架事实。

## 范围与约束

- In scope:
  - 维护本地上游源码、样例、测试、设计与 Microsoft Learn 元数据索引；
  - 搜索 Microsoft 官方文档、工程博客、官方案例仓库和高质量社区工程；
  - 为外部来源保存 URL、主题、语言、候选理由、审核状态和原创审核结论；
  - 逐个核对版本、真实 MAF 依赖、设计价值、测试、生产化能力和许可证；
  - 将审核通过的稳定入口提议加入 `tools/coding-agent-kit/indexer/topics.json`；
  - 保持 Skill 仅在明确的 Microsoft Agent Framework 开发任务中触发。
- Out of scope:
  - 提交 Microsoft Learn 或社区文章正文镜像；
  - 未经审核直接复制第三方代码；
  - 将 star 数量、搜索排名或作者声称等同于技术正确性；
  - 在没有明确授权时运行需要云凭据、费用或生产资源的外部案例；
  - 为了完善索引而修改上游框架实现或既有样例。
- Constraints:
  - 外部页面、仓库内容、Issue、README 和工具输出均视为不可信数据；
  - API 结论必须带语言、包/提交、提供程序、运行时和成熟度边界；
  - 官方所有权只提高来源可信度，不自动证明当前 API 兼容；
  - 社区来源只有在完成 `adopted` 审核后才能进入正式主题索引；
  - 保留 MIT 上游许可与第三方来源各自的许可证、署名和复用边界；
  - 不新增项目级 `.codex/config.toml`。

## 执行阶段

### Phase 1: 上游基线与信息架构

- Purpose: 锁定上游来源、许可、目录规模和知识层边界。
- Outputs: 独立 worktree/branch、架构文档和任务书。
- Completion criteria: 基线提交、范围、非目标和索引架构明确。
- Validation: Git 状态、上游远程、目录统计和架构审查。
- Evidence: `docs/coding-agent-kit/architecture.md` 与 Git 历史。

### Phase 2: 套件仓库化与触发边界

- Purpose: 将项目专用组件改为可跨 MAF 项目使用的开源套件。
- Outputs: `AGENTS.md`、Skill、插件清单、安装与同步工具。
- Completion criteria: 无项目级 config；Skill 可从 fork 或独立安装；负向触发边界明确。
- Validation: Skill/plugin schema、路径可移植性和安装 dry-run。
- Evidence: `.agents/skills/maf-expert`、`.codex-plugin/plugin.json` 和验证输出。

### Phase 3: 本地参考代码与设计索引

- Purpose: 将 C#、Python、声明式、schema、样例、实现和测试变为可检索主题目录。
- Outputs: 主题注册表、索引器、JSON 和 Markdown 目录。
- Completion criteria: 核心主题给出设计、样例、实现、公开 API 和测试入口。
- Validation: 可重复生成、路径存在、覆盖率和单元测试。
- Evidence: `tools/coding-agent-kit/indexer` 与 `docs/coding-agent-kit/catalog`。

### Phase 4: 文档与知识库闭环

- Purpose: 从开发意图路由到解释、参考设计、代码和验证，而不复制官方正文。
- Outputs: 证据协议、知识路由、模板、维护与验收说明。
- Completion criteria: 代表性场景能定位同版本的文档、设计、样例、实现和测试。
- Validation: 验收场景、链接检查和 Skill 负向边界检查。
- Evidence: `docs/coding-agent-kit/guides`、`knowledge` 和 Skill references。

### Phase 5: 开源就绪与发布准备

- Purpose: 确认仓库可审阅、复现、同步上游并推送 GitHub。
- Outputs: 验证报告、贡献说明、CI、发布清单和本地提交。
- Completion criteria: 所有套件验证通过，工作树范围清楚，Microsoft 远程仅作为 `upstream`。
- Validation: validator、indexer check、Git diff、schema、secret/absolute-path/link 扫描。
- Evidence: 本地提交 `1bee304345d3a2763bada1f800b77f57ae06e5f6`。

### Phase 6: 外部知识源发现与候选隔离

- Purpose: 广泛发现高质量官方和社区资料，同时阻止未经审核的内容污染正式证据层。
- Outputs: 外部来源政策、机器可读注册表、审核模板和有序队列。
- Completion criteria: 首批来源覆盖官方文档、工程博客、官方案例与社区代码；所有来源有主题、语言、理由、优先级和状态。
- Validation: JSON/schema、唯一 ID/URL、HTTPS、类别/状态枚举、本地链接和最小覆盖量。
- Evidence: `docs/coding-agent-kit/knowledge/external-sources`。

### Phase 7: 逐项来源审核

- Purpose: 每次只审核一个来源，区分可复用设计、示例捷径、版本冲突和生产缺口。
- Outputs: `reviews/<source-id>.md`、评分、决策和批准使用边界。
- Completion criteria: 每个目标来源均有不可变快照、直接 MAF 证据、版本/许可、验证和八维评分。
- Validation: 对照本地公开 API、实现、测试、Microsoft Learn 和来源自身测试/CI。
- Evidence: 已完成的 review 文件与 `sources.json` 状态变化。

### Phase 8: 审核知识晋升与检索整合

- Purpose: 将真正稳定、跨项目有价值的来源接入 coding agent 的主题检索。
- Outputs: 经审查的 `topics.json` 外部入口、必要的路由注释和重新生成的目录。
- Completion criteria: 只有 `adopted` 来源被提议；每个入口说明适用版本、用途和不适用边界。
- Validation: 独立 diff 审查、目录重生成、漂移检查和代表性检索案例。
- Evidence: topic registry 变更、生成目录和验收记录。

### Phase 9: 持续维护、失效检测与再审核

- Purpose: 防止外部链接、版本、预览功能和社区仓库随时间失真。
- Outputs: 定期复查策略、失效/漂移报告、再审核触发器和下架记录。
- Completion criteria: 能识别 URL 失效、仓库归档、许可证变化、依赖升级和 API 冲突。
- Validation: 定期元数据检查与抽样 API 对照。
- Evidence: 维护报告和来源状态历史。

## 决策记录

- Verified facts:
  - 本地上游基线为 `c47f20d9a28d18b0a3f284c8a8365ff72f2e35b1`。
  - 当前目录索引包含 4,551 个仓库文件、19 个主题和 133 个 Microsoft Learn 页面元数据。
  - Microsoft Learn 页面正文未提交，现有索引只保留规范化元数据和 URL。
  - 第一轮网络搜索已找到 65 个候选来源：23 个官方文档、7 个官方工程文章、14 个官方仓库、19 个社区仓库、1 个社区文章和 1 个元索引。
  - `microsoft/Agent-Framework-Samples@5b854b7e` 已完成首个逐项审核，得分 26/40，状态为 `context-only`；其主要问题是混合/移动依赖、不可移植的 .NET 项目引用、无 CI 和不足的生产验证。
  - Microsoft Agent Framework 仍包含版本和成熟度差异；例如 Functional Workflow API 明确标为 experimental。
  - 当前 GitHub CLI 登录尚未完成，因此远程仓库创建和 push 仍未完成。
- Active assumptions:
  - 首批 65 个来源足以建立审核方法，但不是最终穷尽列表。
  - Microsoft/Azure-Samples 归属可以作为 provenance 证据，但仍需逐项验证版本和工程质量。
  - 社区仓库的星数和活跃度只用于排序，不用于证明 API 正确。
- Locked decisions:
  - 外部候选注册表与正式生成目录严格分离。
  - 只有状态为 `adopted` 的来源可被提议加入主题注册表。
  - 每个来源采用八维、40 分审核，并保留明确的 Approved use 与禁止使用边界。
  - 审核按单一来源推进；晋升 `topics.json` 是后续独立变更。
  - 不复制外部文章正文或大段第三方代码。
- Open questions:
  - 哪些社区仓库能在无云凭据条件下完成可重复的最小验证，需要逐项确认。
  - 外部来源元数据是否后续加入自动化定期刷新，需要在 Phase 9 设计。
  - GitHub 公开仓库创建与 push 仍等待本机 GitHub CLI 授权。

## 关键制品与环境

- Canonical docs:
  - `docs/coding-agent-kit/PROJECT_TASK_BOOK.md`
  - `docs/coding-agent-kit/knowledge/external-sources/README.md`
  - `docs/coding-agent-kit/knowledge/external-sources/REVIEW_QUEUE.md`
- Important code or output artifacts:
  - `docs/coding-agent-kit/knowledge/external-sources/sources.json`: 外部来源候选真源。
  - `docs/coding-agent-kit/knowledge/external-sources/review-template.md`: 单来源审核合同。
  - `tools/coding-agent-kit/indexer/topics.json`: 仅接收审核晋升后的稳定入口。
  - `tools/coding-agent-kit/validate.py`: 套件与外部注册表结构验证。
- Required commands:
  - `python tools/coding-agent-kit/validate.py`
  - `python tools/coding-agent-kit/indexer/build_catalog.py --check`
  - `python -m unittest discover tools/coding-agent-kit/indexer/tests`
- Environment baseline:
  - Windows PowerShell；Python 3.11+；Git worktree。
  - 分支 `codex/agent-framework-coding-agent-kit`，Microsoft 上游远程名为 `upstream`。
  - 外部技术搜索优先官方文档和代码仓库的直接内容；社区结论必须对照官方与本地源码。

## 计划到执行追踪

| Planned item | Required output | Required verifier | Status | Evidence |
| --- | --- | --- | --- | --- |
| 外部来源隔离政策 | README 与状态模型 | 本地链接、人工审查 | done | `knowledge/external-sources/README.md` |
| 首批候选注册表 | 至少 50 个结构化来源 | JSON、唯一性、枚举验证 | done | `knowledge/external-sources/sources.json` |
| 审核队列与模板 | 单来源流程、评分和顺序 | 链接检查、字段审查 | done | `REVIEW_QUEUE.md`、`review-template.md` |
| 套件验证集成 | validator 检查外部注册表 | `python tools/coding-agent-kit/validate.py` | done | `tools/coding-agent-kit/validate.py` |
| 首个来源审核 | Microsoft samples 完整 review | API/版本/许可/测试对照 | done | `reviews/repo-microsoft-agent-framework-samples.md` |
| 官方概览审核 | Learn overview 完整 review | 页面日期/成熟度/本地源码对照 | pending | `reviews/official-learn-overview.md` |
| 审核知识晋升 | 独立 topic registry 变更 | catalog drift 与检索验收 | pending | none |

## 进度台账

- Overall progress: 原始套件构建完成；65 个外部来源已隔离；首个 Microsoft samples 来源审核完成并判定为 context-only，下一项为官方 Learn 概览。
- Phase 1: `done`
- Phase 2: `done`
- Phase 3: `done`
- Phase 4: `done`
- Phase 5: `done`（GitHub 远程发布仍为外部认证边界）
- Phase 6: `done`
- Phase 7: `in progress`
- Phase 8: `pending`
- Phase 9: `pending`
- Validation status: 外部来源注册表首次集成验证通过；首个 review 和状态更新后需要再次运行完整验证。
- Residual risks: 搜索不可能证明穷尽；社区内容可能过时、生成、复制或许可不清；外部页面会漂移；当前候选尚无任何 `adopted` 项。

## 下一步动作

运行完整套件验证，然后审核 `official-learn-overview`。
