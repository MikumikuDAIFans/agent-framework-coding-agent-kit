# Agent Framework Coding Agent Kit 执行启动包

## 执行目标

基于已批准的任务书 v5，完成剩余 Phase 5、Phase 7、Phase 8 和 Phase 9：同步当前
`microsoft/agent-framework` 上游；让 64 个可审核外部来源全部形成独立终态；将所有 adopted
项目和文档按政策接入检索；交付可重复的漂移/再审核入口；完成全量验证并发布到公共 GitHub 仓库。

## Canonical sources

- Canonical progress file: `E:\Microsoft-Agent-Framework\agent-framework-coding-agent-kit\docs\coding-agent-kit\PROJECT_TASK_BOOK.md`
- Final plan audit: `E:\Microsoft-Agent-Framework\agent-framework-coding-agent-kit\docs\coding-agent-kit\FINAL_PLAN_AUDIT.md`
- Review policy: `E:\Microsoft-Agent-Framework\agent-framework-coding-agent-kit\docs\coding-agent-kit\knowledge\external-sources\REVIEW_POLICY.md`
- Review queue: `E:\Microsoft-Agent-Framework\agent-framework-coding-agent-kit\docs\coding-agent-kit\knowledge\external-sources\REVIEW_QUEUE.md`
- Candidate registry: `E:\Microsoft-Agent-Framework\agent-framework-coding-agent-kit\docs\coding-agent-kit\knowledge\external-sources\sources.json`
- Collection contract: `E:\Microsoft-Agent-Framework\agent-framework-coding-agent-kit\docs\coding-agent-kit\knowledge\collection\README.md`
- Execution approval: `explicit`

## 已锁定的设计与执行决策

- 本地上游源码、设计、样例、公开 API 和测试优先于外部来源；在线资料不能静默升级目标版本。
- Coding Agent 可独立审核、评分、决定状态和收录，不需要逐来源请示。
- 项目只保存链接、不可变坐标、路由、设计注释和限制，不得复制或 vendor 外部代码。
- 文档正文只有在再分发许可明确时才转为 Markdown；否则只保存链接和原创审核注释。
- 只有 `adopted` 来源进入 collection；meta-index 永远只作发现入口。
- 用户既有 `tools/coding-agent-kit/install.py` 修改必须保留、独立审查和验证。
- 禁止推送 `upstream`；最终公共仓库为 `MikumikuDAIFans/agent-framework-coding-agent-kit`。
- 不重新讨论评分权重、状态阈值、项目/文档分轨或项目不复制代码等已批准规则，除非发现 P0/P1 风险。

## 实现顺序

1. **Preflight 与上游同步**：审查并保护 `install.py` 修改；确认公开提交使用的 Git 身份但不擅自修改全局配置；
   fetch `upstream/main`；形成漂移记录；
   合并或变基时保留 kit 历史和用户修改；更新 upstream baseline 并重建 catalog。
2. **关闭首个审核**：按 v1.1 完成 `repo-microsoft-agent-framework-samples`，作为代码项目审核样板。
3. **批量审核**：依次完成 Batch A–E。官方文档先做快速核对；官方工程文章、官方仓库和社区来源
   使用对应评分轨。每项立即更新独立 review、`sources.json` 和队列状态。
4. **随审核随收录**：adopted 项目用 `collect.py add-project`；许可允许的文档用
   `add-document`；不可镜像文档只保留链接/原创注释。持续运行 collection check 和代表性 lookup。
5. **维护闭环**：实现链接、版本、归档、许可证和 API 漂移检查，提供无网络结构测试、受控联网
   smoke test、再审核状态更新规则和 CI/automation 可复用入口。
6. **最终交付**：对照任务书完成定义做全量审计；清理所有 `queued`/`in-review`；创建公共 GitHub
   仓库，配置 `origin`，禁用 `upstream` push，推送分支并核对远端 commit 和仓库可访问性。

## Agent Team 策略

- Parallelization stance: `积极启用，但只拆分互不重叠的来源集合和只读证据调查`。
- Coordinator responsibility: 主会话拥有任务书、`sources.json`、`REVIEW_QUEUE.md`、collection
  manifests、catalog 集成、Git 操作、最终验证和发布。
- Worker splits:
  - 官方文档：按不重叠 source ID 收集页面日期、版本、成熟度、许可和本地冲突证据。
  - 官方/社区项目：按不重叠仓库收集 commit、MAF 依赖、设计、测试、生产化和许可证据。
  - 文章与维护：审核真实 Demo/时效性，并独立开发漂移检查测试或文档。
- 每个 worker 只写自己分配的独立 review 文件或返回证据；共享注册表和生成文件由 coordinator 串行更新。
- 不重复背景探索，不覆盖用户修改，不由 worker 执行 push 或最终状态晋升。

## 自主执行与升级规则

- 把任务视为端到端执行，不在常规批次或里程碑处请求确认。
- 对评分、验证替代、文件组织和批次大小等低风险细节自行做合理决定。
- 每完成一个有意义批次就更新 `PROJECT_TASK_BOOK.md` 的计数、阶段状态、验证和唯一下一步。
- 只有在无法本地解决的关键信息缺失、P0/P1 安全/许可/数据风险、破坏性操作、真实权限阻塞或
  必需验证无等价替代时暂停。
- 不运行需要云凭据、费用或生产资源的案例；记录 `not-run` 和替代证据即可。
- 若被阻塞，只报告阻塞点、已尝试方案和用户需要做出的最小决策。

## 完成定义与验证

Done means:

- 64 个可审核来源全部进入 `adopted`、`context-only`、`quarantined` 或 `rejected`，无 `queued`/
  `in-review`；1 个 meta-index 保持 `discovered`。
- 每个 adopted 来源完成合法收录和检索验证；项目无代码副本，文档有许可与哈希。
- Phase 9 漂移检查、测试、维护说明和再审核路径完成。
- 任务书、队列、注册表、collection、catalog 和实际文件完全一致。
- 公共 GitHub 仓库创建并成功推送，`upstream` 不可推送，工作树干净。

Required validation:

```powershell
python tools/coding-agent-kit/indexer/build_catalog.py --check
python -m unittest discover tools/coding-agent-kit/indexer/tests
python -m unittest discover tools/coding-agent-kit/knowledge/tests
python tools/coding-agent-kit/knowledge/collect.py check
python tools/coding-agent-kit/validate.py
git diff --check
git status --short --branch
gh repo view MikumikuDAIFans/agent-framework-coding-agent-kit
```

Known acceptable gaps: 需要真实云凭据、付费模型或生产资源的外部运行测试可以 `not-run`，但必须
有静态/本地替代证据、原因和残余风险。其他硬检查不得降级。

## 最终汇报契约

仅在完整完成或真实阻塞时统一汇报。最终报告必须包含：终态计数、adopted 清单与收录形式、关键
设计/代码/文档产物、实际验证结果、`not-run` 项、残余风险、GitHub URL 和远端 commit。汇报前
必须把主任务书更新为真实状态。

## `/goal` 提示词

```text
/goal
请在 E:\Microsoft-Agent-Framework\agent-framework-coding-agent-kit 中，严格基于已经批准的
docs/coding-agent-kit/PROJECT_TASK_BOOK.md v5 和 docs/coding-agent-kit/FINAL_PLAN_AUDIT.md，
端到端完成 Agent Framework Coding Agent Kit 的剩余计划。把这次任务当作执行任务，不要重新讨论
已经锁定的审核权重、状态规则和收录架构，也不要在常规里程碑处停下来请求确认。

Read first:
- AGENTS.md
- docs/coding-agent-kit/PROJECT_TASK_BOOK.md
- docs/coding-agent-kit/FINAL_PLAN_AUDIT.md
- docs/coding-agent-kit/knowledge/external-sources/REVIEW_POLICY.md
- docs/coding-agent-kit/knowledge/external-sources/REVIEW_QUEUE.md
- docs/coding-agent-kit/knowledge/external-sources/sources.json
- docs/coding-agent-kit/knowledge/collection/README.md

Execution contract:
- 首先保留并审查当前未提交的 tools/coding-agent-kit/install.py 用户修改，不得 reset、checkout 或覆盖。
- 确认公开提交应采用的 Git 身份；当前自动身份为 unknown <zhangjiayang@santint.com>，不得擅自修改全局 Git 配置。
- 随后 fetch/sync upstream/main，解决 c47f20d9... 到 5ab8877b... 的基线漂移，重建并验证 catalog。
- 完成 64 个可审核来源的逐项终态审核；唯一 meta-index 保持 discovered。
- 项目只收 URL、不可变版本、路由和注释，绝不复制外部项目代码。
- 许可允许时把 adopted 文档下载/转换为带来源、日期、许可和哈希的 Markdown；否则只存链接和原创注释。
- 随审核随更新 review、sources.json、REVIEW_QUEUE.md、collection manifests、KNOWLEDGE_INDEX.md 和 lookup。
- 完成 Phase 9 的链接/版本/许可/归档/API 漂移检查与可复用测试入口。
- 优先使用 Agent Team/subagent 并行处理不重叠来源的证据调查；主会话独占共享注册表、生成文件、集成、Git 和发布。
- 每个有意义批次后更新 PROJECT_TASK_BOOK.md；不要把 failed、blocked 或 not-run 写成 pass。
- 不运行需要云凭据、费用或生产资源的案例，使用静态/本地替代证据并记录边界。
- 最终创建公共仓库 MikumikuDAIFans/agent-framework-coding-agent-kit，配置 origin，禁止 upstream push，推送并核对远端 commit。
- 仅在无法本地解决的 P0/P1 风险、破坏性决策、权限阻塞或必需验证无替代时暂停。
- 完成全部实现和验证后只做一次统一汇报；若阻塞，只报告阻塞、已尝试方案和所需最小决策。

Definition of done:
- 64 个可审核来源无 queued/in-review，每项有独立 review、证据、终态和收录动作。
- 所有 adopted 来源合法进入项目路由、Markdown 文档或 link/annotation-only 结果，并能由 lookup 检索。
- 漂移维护入口、测试、任务书、队列、注册表、collection 和 catalog 一致且全部硬验证通过。
- 公共 GitHub 仓库已推送、upstream 不可推送、工作树干净，最终报告包含终态计数、验证、风险和远端 commit。

Start by:
审查并保护 tools/coding-agent-kit/install.py 的既有修改，然后同步 upstream/main 与 catalog 基线。
```
