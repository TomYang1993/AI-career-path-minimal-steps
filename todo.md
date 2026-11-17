# Career path map — review backlog

Recorded: November 16, 2026 (Pacific time).

Audience: experienced software developers seeking practical AI engineering skills, foundational intuition and engineering judgment, without assuming a strong math background.

Decision: feature CMU Modern AI now. The unchecked suggestions below are saved for later review, not approved curriculum changes. Preserve appropriate mathematical and systems depth for research and specialist roles.

## Completed from today's discussion

- [x] Feature CMU 10-202 Introduction to Modern AI first in the shared ML fundamentals box; retain Stanford CS229 as an alternative.
- [x] Explain that the CMU selection reflects practical fit, not a measured popularity ranking.
- [x] Rename unsupported Popular badges to Featured and disclose their editorial basis.
- [x] Point CS229 directly to the supplied public lecture playlist, noting missing lecture numbers and restricted current course documents.
- [x] Add MIT 6.100L's 26-lecture gallery to the Python Videos tab and use the direct gallery for its course link.
- [x] Carry these changes through the relevant static role pages and preserve Featured wording in their generator.

## Priority: usable learning links and accurate descriptions

- [ ] Audit resources for actual public teaching materials. Distinguish full videos, partial videos, notes, assignments and description-only pages; a successful page load alone is not enough.
- [ ] Add direct watch/read/exercise links, edition/year, verification date, account requirements and missing material to each resource card.
- [ ] Link CS224N's public 2024 playlist directly in Videos; distinguish it from login-only current recordings. [Course access details](https://web.stanford.edu/class/cs224n/) · [Public playlist](https://www.youtube.com/playlist?list=PLoROMvodv4rOaMFbaqxPDoLWjDaRAdP9D)
- [ ] Correct Vector Database from Scratch: its current edition uses Rust/DataFusion; the C++/BusTub edition is deprecated. Consider moving it to optional depth. [Source](https://skyzh.github.io/vector-db-from-scratch/)
- [ ] Replace or reclassify CMU Cloud Computing's departmental profile until usable public learning materials are verified. The linked profile provides no sample lectures or assignments. [Current link](https://csd.cmu.edu/15319619-cloud-computing)
- [ ] Update CS329Z's Syllabus label to reflect its available video/slide links, without implying a complete recorded course. [Schedule](https://cs329z.stanford.edu/)
- [ ] Clarify LLM Zoomcamp cohort versus self-paced certificates/peer review and separate free material from API costs. Consider it as a practical application-building backbone. [Course](https://github.com/DataTalksClub/llm-zoomcamp)
- [ ] Recheck DeepLearning.AI embedding and vector-database courses: access could not be verified in this review. Do not treat a failed fetch as proof of a paywall or missing course.
- [ ] Recheck CMU AI Agents video availability and completeness; the research reader returned no course content.
- [ ] Replace blanket $0/free claims with separate teaching-material, API, GPU, hosting and certificate costs; verify any suggested free alternatives.

## Priority: recommendations and path structure

- [ ] Consider Start here, Alternative, Optional depth and Reference only labels, chosen by role and learning stage.
- [ ] Rank by usable access, prerequisites, relevance, practical exercise and manageable scope. Keep audience size and repository stars as context rather than the main recommendation rule.
- [ ] Replace the automatic plan's maximum-box-coverage rule with a plan that accounts for prerequisites, workload and selected lessons.
- [ ] Make optional/recommended labels consistent between the interactive graph, role pages and README.
- [ ] Present the large resource collection as alternatives around a short default route, not a requirement to finish every course and project.
- [ ] Give each stage a concrete completion check, estimated scope and stopping point.
- [ ] Keep the map, role-page generator, generated pages and minimal README consistent when implementing future changes.

## AI engineer: proposed learning changes

- [ ] Add skip checks for Python, Git, shell and backend skills. Existing developers should fill gaps rather than repeat complete introductory courses or rebuild a whole general web app.
- [ ] Scope Modern AI to useful foundations; disclose its use of derivatives and basic linear algebra/probability. Do not require every training/RL assignment for application builders. [Syllabus](https://modernaicourse.org/)
- [ ] Make evaluation splits, leakage, overfitting and error analysis part of a short required practical checkpoint while keeping the full ML course optional.
- [ ] Replace full CS224N/Advanced NLP/GPT-from-scratch requirements with selected lessons and experiments in tokenization, context, decoding and model behavior; keep full courses as depth.
- [ ] Begin embeddings with parsing, source metadata, chunking and comparing existing models on labeled queries; defer encoder training until a diagnosed need.
- [ ] Begin vector stores with indexing, filters, updates/deletion and retrieval quality; defer database internals and broad engine benchmarks.
- [ ] Start retrieval with keyword and dense baselines on the same queries. Add hybrid search, rerankers and query rewriting only when evaluation shows a benefit.
- [ ] Build a basic RAG milestone earlier: one corpus, citations and retrieval/answer evaluation. Advanced and graph RAG remain extensions.
- [ ] Build one bounded tool loop before frameworks. Introduce orchestration for demonstrated branching, checkpointing or recovery needs.
- [ ] Start agents with one agent and explicit stop/failure handling; make multi-agent designs and agent RL optional.
- [ ] Start memory with session state and context budgets; add persistent memory only with relevance, deletion and privacy checks.
- [ ] Teach permissions, validation, budgets, secret handling and approval boundaries with the first tool call. Reserve advanced sandboxing and long-running harnesses for later.
- [ ] Put small eval sets, failure analysis, traces, cost and latency measurements into the first application; add testing and CI progressively.
- [ ] Keep coding-agent use as a parallel productivity skill, with independent diff review and testing, rather than a prerequisite for agent architecture.
- [ ] Put practical guides and exercises before classic papers; reconsider must-read labels for application builders while preserving research reading depth.
- [ ] Simplify the first capstone to one real data source and one tool. Add MCP, more tools, hybrid retrieval and reranking only against observed failures; retain the original capstone as an advanced option.
- [ ] Review this proposed sequence: skill check → small model-backed feature + evals → foundation intuition → cited retrieval → one bounded tool → measured improvements → deployment, monitoring and rollback.

## Other paths and shared skills

- [ ] Computer systems/Linux: separate operational troubleshooting from kernel implementation; make xv6 and deeper OS projects optional where appropriate.
- [ ] Math: teach application intuition as needed; retain explicit calculus, probability and linear algebra preparation for model research, including a clearer calculus bridge.
- [ ] LLM APIs: require structured outputs, validation, streaming, bounded retries and tool use; make graduate slides and historical prompting papers supplementary.
- [ ] Frontend: focus on streaming, cancellation, citations and failure states; allow experienced developers to skip general frontend courses.
- [ ] Containers/CI: package and deploy one real app early, with tests and rollback; use selected course modules.
- [ ] DevOps/full-stack: distinguish product development from infrastructure operations. Make Kubernetes optional for the application branch and pick one cloud before several.
- [ ] DevOps/full-stack: resolve optional evals versus a capstone that requires an eval gate.
- [ ] MLOps: distinguish API-app prompt/config versioning and deployment from model artifacts, data and training pipelines.
- [ ] Platform: separate inference operations from training infrastructure. Move serving and monitoring before unnecessary full NLP, kernel-programming or autodiff-library requirements.
- [ ] GPU skills: separate utilization, memory and profiling fundamentals from CUDA/Triton kernel specialization.
- [ ] Deep learning/PyTorch: use a small training/checkpoint exercise and consider fast.ai as a practical entry; scope full vision/advanced DL courses to the target role.
- [ ] Inference/serving: benchmark one model before multi-node work; keep self-hosting optional for API-only application builders.
- [ ] Distributed training: reserve Needle/autodiff internals and multi-GPU pretraining for training-platform or research needs.
- [ ] Model research: keep substantial mathematical depth, but distinguish fine-tuning/experimentation from pretraining research.
- [ ] Pretraining: start with a tiny reproducible model and baseline before scale; keep CS336 on the advanced model-building route.
- [ ] Post-training: establish baseline and held-out evaluation, then SFT/LoRA; separate preference optimization and RL into later branches.
- [ ] Observability/cost: distinguish application cost per successful task and error rate from platform GPU utilization, queueing and capacity cost.

## Review provenance

These proposals came from the November 16 review of all 29 skill boxes, four role definitions, resource-selection logic, prerequisite graph and README, prompted by the CS229/CMU comparison and MIT video-link issue. External verification was targeted, not an exhaustive execution of all courses, notebooks or videos. Recheck live access and prices before implementing the deferred items.

Content repository: [AI-career-path-minimal-steps](https://github.com/TomYang1993/AI-career-path-minimal-steps). Website source: [ai-career-paths](https://github.com/TomYang1993/tomyang1993.github.io/tree/master/ai-career-paths).
