# Agent Framework Coding Agent Kit 最终计划审计

## 审计结论

- Audit date: `2026-07-17 Asia/Shanghai`
- Canonical plan: `docs/coding-agent-kit/PROJECT_TASK_BOOK.md` v5
- Audited baseline commit: `25d904de0e9b8d5e0c540c5da4b5d17d9393f634`
- Branch: `codex/agent-framework-coding-agent-kit`
- Verdict: `PASS-WITH-BOUNDARIES`
- Execution approval: `explicit`

计划已经具备端到端执行条件。没有未解决的 P0/P1 设计或安全风险；三项边界必须由执行会话在
对应阶段关闭，不得隐藏或绕过。

## 审计发现

### P0/P1

无。

### P2 — 执行前必须处理

1. **上游基线漂移**：目录锁定在 `c47f20d9...`，而 `upstream/main` 已到 `5ab8877b...`。
   在正式评价外部 API 兼容性前，必须 fetch、审查差异、同步上游并重建目录。
2. **用户既有修改**：`tools/coding-agent-kit/install.py` 存在未提交修改。不得 reset、checkout 或
   覆盖；应先审查、运行安装相关验证，再决定以独立提交纳入。
3. **公开交付未完成**：GitHub CLI 已登录 `MikumikuDAIFans`，但
   `MikumikuDAIFans/agent-framework-coding-agent-kit` 不存在，仓库没有 `origin`，且 `upstream`
   仍显示 push URL。最终发布前必须创建公共仓库、配置 `origin` 并禁用 `upstream` 推送。

### P3 — 持续跟踪

- 本机 Git 自动提交身份为 `unknown <zhangjiayang@santint.com>`；公开推送前确认有意采用的身份，
  但不要在未获授权时改写用户的全局 Git 配置。
- 网络搜索不保证穷尽；注册表应保持可扩展，而不是把 65 个候选解释为封闭全集。
- 无凭据或有成本的外部案例允许 `not-run`，但必须保留静态/本地替代证据和残余风险。
- 文档正文只有在再分发许可明确时才能落库；不能把“官方”自动解释为可镜像。

## 计划完整性审计

| Area | Result | Notes |
| --- | --- | --- |
| Goal and scope | pass | 目标明确覆盖审核、收录、检索、维护和开源交付。 |
| Locked decisions | pass | 项目只存路由；文档按许可转 Markdown；Coding Agent 可自主裁决。 |
| Source evidence | pass | 本地上游、Learn 元数据、外部注册表和逐来源 review 分层清楚。 |
| Completion definition | pass | 64 个可审核来源终态、1 个 meta-index 保持 discovered，所有 adopted 有收录动作。 |
| Verification | pass | validator、catalog、indexer tests、collection tests、collection check 均为硬检查。 |
| Maintenance | pass | Phase 9 要求交付可手动及 CI/automation 复用的漂移检查入口。 |
| Publishing | pass-with-boundary | 认证有效；提交身份确认、目标仓库、origin、push 和 upstream push protection 待执行。 |
| Resumability | pass | 主任务书、队列、注册表、审核文件和启动包提供唯一可恢复状态。 |

## 必须保留的执行证据

- 每个来源的 URL、不可变坐标、日期、许可、MAF 直接证据、版本/成熟度、验证与终态。
- 每个 `adopted` 项目的 route/design/limitations；不得产生外部项目代码副本。
- 每个 retained document 的许可 URL、抓取时间、source/stored SHA-256 和转换方式。
- 每次批次后的注册表/队列计数、失败或 `not-run` 检查、collection/catalog drift 结果。
- 最终 GitHub URL、remote 布局、远端 commit、分支和公开可访问性。

## 启动判定

`IW-GATE-00..05`：`pass-with-boundary`。计划可正式启动。`construction-plan-system` 专项技能当前
不可用，但本任务书 v5、执行追踪、本文审计和 `EXECUTION_LAUNCH.md` 已提供等价的范围、证据、
完成定义、停止规则和恢复契约；该缺口不构成 P0/P1 风险。

唯一启动动作：先保护并审查 `install.py` 用户修改，再同步上游基线。
