![Course Thumbnail](https://github.com/shreshthtuli/build-your-own-super-agents/blob/main/assets/build-your-own-super-agents-thumbnail.jpg?raw=true)

Welcome to **Build Your Own Super Agents** — a fast, fun, no-fluff adventure into agentic AI. In these notebooks, you’ll train agents, evolve them, and even make them battle (yes, there are [Pokémon](https://shreshthtuli.github.io/build-your-own-super-agents/07-multi-agent-workflows.html#creating-a-max-damage-baseline:~:text=Let%E2%80%99s%20see%20an%20example%20battle%20in%20action.)). You’ll start with a tiny single-step agent and end up commanding full swarms that can plan, retrieve, reason, and act. Whether you’re a researcher, engineer, or curious tinkerer, this course gives you everything you need to level up from simple prompts to real super-agent systems. 🚀🌟


<div align="center" id="top">
  
<a target="_blank" href="https://lightning.ai/shraysteam/environments/build-your-own-super-agents">
  <img src="https://pl-bolts-doc-images.s3.us-east-2.amazonaws.com/app-2/studio-badge.svg" alt="Open In Studio"/>
</a>

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Jupyter](https://img.shields.io/badge/Notebook-Interactive-orange)
![License](https://img.shields.io/github/license/shreshthtuli/build-your-own-super-agents)
[![GitHub code](https://img.shields.io/badge/View%20Code-on%20GitHub-black?logo=github)](https://github.com/shreshthtuli/build-your-own-super-agents)
![Stars](https://img.shields.io/github/stars/shreshthtuli/build-your-own-super-agents?style=social)
 
</div>

## 🎯 Course Highlights
* **Fully hands-on agentic notebooks** for every module — clone locally or run instantly in your preferred Jupyter environment.
* **Practical agent templates, evaluators, and tool integrations** so you can build real agents without drowning in boilerplate orchestration code.
* **Clear theory, references, and best-practice design patterns** interwoven with examples to make every agentic concept intuitive and reproducible.
* **Production-ready mindset throughout** — covering retrieval, graph reasoning, multi-agent coordination, reflection loops, model routing/selection, cost-latency tradeoffs, and cloud-scale deployment.


## 📚 Course Structure

Each module is a self-contained notebook filled with explanations, demos, and practical agentic workflows. You can browse them on GitHub Pages, clone them locally, or run them interactively in your preferred notebook environment.

| Module | Topic                                              | Notebook                          |
| ------ | -------------------------------------------------- | --------------------------------- |
| 01     | A Very Simple Agent                                | [01-simple-agent.ipynb]((https://shreshthtuli.github.io/build-your-own-super-agents/01-simple-agent.html))             |
| 02     | Moving to Agentic Frameworks                       | [02-framework-pydantic-ai.ipynb](https://shreshthtuli.github.io/build-your-own-super-agents/02-framework-pydantic-ai.html)       |
| 03     | Prompt Engineering & Reflection Loops              | [03-prompting-engg.ipynb](https://shreshthtuli.github.io/build-your-own-super-agents/03-prompt-engg.html)     |
| 04     | Retrieval-Augmented Generation (RAG)               | [04-rag.ipynb](https://shreshthtuli.github.io/build-your-own-super-agents/04-rag.html)                      |
| 05     | Knowledge Graphs & GraphRAG                        | [05-graphrag.ipynb](https://shreshthtuli.github.io/build-your-own-super-agents/05-graphrag.html)                 |
| 06     | Agentic Evaluation & Continuous Confidence         | [06-evaluation.ipynb](https://shreshthtuli.github.io/build-your-own-super-agents/06-evaluation.html)       |
| 07     | Multi-Agent Workflows & Agent Swarms               | [07-multi-agent-workflows.ipynb](https://shreshthtuli.github.io/build-your-own-super-agents/07-multi-agent-workflows.html)       |
| 08     | Model Selection for Agents                         | [08-model-selection.ipynb](https://shreshthtuli.github.io/build-your-own-super-agents/08-model-selection.html)        |
| 09     | Model Placement (Edge, Cloud, Hybrid)              | [09-model-placement.ipynb](https://shreshthtuli.github.io/build-your-own-super-agents/09-model-placement.html)          |
| 10     | Appendix: End-to-End Experimentation               | [10-appendix-experimentation.ipynb](https://shreshthtuli.github.io/build-your-own-super-agents/10-appendix-experimentation.html)          |
| 11     | Appendix: Designing Scalable Agentic Systems (AWS) | [11-scalable-agentic-systems.ipynb](https://shreshthtuli.github.io/build-your-own-super-agents/11-appendix-design-and-deployment.html) |


## 🧠 What You'll Learn

* How to design an agent’s full loop — perception, retrieval, reasoning, planning, and action.
* How to use modern agentic frameworks to add tools, memory, structured outputs, and multi-step workflows.
* Techniques for building powerful retrieval systems (RAG), knowledge graphs, and GraphRAG pipelines.
* How to evaluate agents with confidence metrics, behavioural tests, and multi-agent benchmarking.
* How to build, coordinate, and optimize multi-agent swarms that collaborate or compete.
* Practical orchestration: model selection, model placement, cost–latency tradeoffs, and routing strategies.


## ⚙️ Quick Start

### Option A: Launch in Lightning Studio (no setup!)
1. Click the **Open in Studio** badge above.
2. Authenticate with Lightning (or create a free account).
3. **Add API Keys** in `.env` file. Follow `.env.example` and [this](https://openrouter.ai/keys).
4. Explore the notebooks in a fully provisioned environment.

### Option B: Run Locally
1. **Clone the repository**
   ```bash
   git clone https://github.com/shreshthtuli/build-your-own-super-agents.git
   cd build-your-own-super-agents
   ```
2. **Install dependencies** (recommended: Python 3.10+)
   ```bash
   pip install uv
   uv sync
   ```
3. **Add API Keys** in `.env` file. Follow `.env.example`.
4. **Install docker** by following steps [here](https://docs.docker.com/engine/install/). 
5. **(Optional) Create LogFire account** [here](https://logfire.pydantic.dev/) and log in using 
    ```bash
    logfire auth
    ```
5. **Launch Jupyter**
   ```bash
   jupyter lab
   ```
6. Open any notebook to start experimenting.


## 🧭 Suggested Learning Path

1. **Foundations (Modules 01–03)** – Build your first agent, understand agentic loops, and layer in prompting + reflection.
2. **Retrieval & Knowledge (Modules 04–05)** – Add RAG, build knowledge graphs, and integrate GraphRAG into agent workflows.
3. **Evaluation & Behaviour (Module 06)** – Learn how to measure agent performance, confidence, robustness, and reasoning quality.
4. **Multi-Agent Systems (Module 07)** – Coordinate multiple agents, share context, resolve conflicts, and design agent swarms.
5. **Orchestration (Modules 08–09)** – Master model selection, routing, placement, and the cost–latency–quality trade-offs that power real systems.
6. **Capstone** – Combine everything to build, evaluate, and deploy a production-ready super-agent tailored to your real use case.

Every notebook stands alone, but following this sequence gives you the smoothest progression from simple agents to fully orchestrated super-agents.



## 🧑‍💻 Who am I?

I’m **Shreshth Tuli**, research engineer and educator specializing in advanced ML systems, optimisation and real-world deployment. I build and teach systems that go beyond isolated models into full pipelines and platforms. Done this course? Feel free to connect on LinkedIn [@shreshth-tuli](https://www.linkedin.com/in/shreshth-tuli/) or GitHub [@shreshthtuli](https://github.com/shreshthtuli).


## 🤝 Contributions

Contributions, ideas, and bug reports are always appreciated! To contribute:

1. Fork the repository and create a feature branch.
2. Open a pull request explaining what you changed and why.
3. Reference any affected notebooks or modules, and include examples or screenshots if helpful.

Check the issue tracker for beginner-friendly tasks or start a discussion if you’d like to propose a new agent module, framework, or workflow.


## 📄 License

This project is released under the [Apache 2.0 License](LICENSE). You're welcome to use the material in your own projects, demos, workshops, or derivative courses — just keep the attribution intact.

> Don’t just study agents—forge your own and unleash it. 🚀


[1]: https://shreshthtuli.github.io/build-your-own-super-agents/README.html " Course Highlights"
