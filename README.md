# LLM Logic Demos

A collection of demonstrations exploring the synergy between Large Language Models (LLMs) and various formal logic and reasoning systems. This repository provides code examples to illustrate how to integrate LLMs with techniques like logic programming, knowledge graph traversal, and advanced reasoning frameworks to create more robust and explainable applications.

The goal is to move beyond simple prompt-based LLM interactions by grounding the models in structured, symbolic logic to enhance reasoning capabilities and reduce hallucinations.

---

## Repository Structure

The repository is organized into distinct folders, each containing a specific set of logic and LLM integration demos:

| Directory | Description |
| :--- | :--- |
| **`Backward Chaining Engine`** | Demonstrations of implementing or utilizing a backward chaining inference engine, often used in expert systems, and how an LLM can interact with or formulate the initial goals and rules. |
| **`LangChain and LangGraph`** | Examples utilizing the powerful LangChain and LangGraph frameworks to build complex, multi-step LLM agents. Demos here may show how to construct conversational agents or reasoning pipelines that incorporate external knowledge and logical steps. |
| **`datalog`** | Code demonstrating the use of Datalog, a declarative logic programming language, for knowledge representation and querying, potentially using an LLM to generate Datalog queries or interpret results. |
| **`prolog`** | Demos focused on Prolog, a prominent logic programming language. This section explores how to bridge LLM outputs (e.g., extracting facts or rules) with a Prolog engine to perform sophisticated symbolic reasoning. |
| **`requirements.txt`** | A list of necessary Python packages required to run the demonstrations. |

---

## Getting Started

### Prerequisites

* Python (3.9+)
* API keys for the LLM services used in the demos (e.g., OpenAI, Anthropic, etc.), which you may need to configure as environment variables.

### Installation

```bash
git clone https://github.com/sakisaki-dev/LLM-Logic-Demos.git
cd LLM-Logic-Demos
python -m venv venv && source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Running the demos

Each folder is self-contained:

| Demo | Run |
| :--- | :--- |
| Prolog knowledge base queried from Python | `python prolog/python_prolog_demo.py` |
| Natural language → Prolog facts with an LLM | `python prolog/naturalLanguage_toprolog.py` |
| Datalog querying | `python datalog/datalog.py` |
| Backward chaining inference engine | `python "Backward Chaining Engine/backward_chaining.py"` |
| Multi-step LLM agent with LangGraph | `python "LangChain and LangGraph/lang_graph.py"` |

The LangGraph folder also includes a write-up of the agent design (PDF).

---

Built with Aman as part of UCSC's AIEA lab. Earlier course tasks are archived in separate repos
([task4](https://github.com/sakisaki-dev/task4AIEA), [task6](https://github.com/sakisaki-dev/task6AIEA),
[task7](https://github.com/sakisaki-dev/task7AIEA), [task9](https://github.com/sakisaki-dev/task9AIEA)).
