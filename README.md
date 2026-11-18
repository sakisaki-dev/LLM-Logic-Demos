# LLM Logic Demos

Small Python demos of symbolic reasoning (Prolog, Datalog, a hand-written backward chaining engine, and a LangGraph pipeline), plus one demo that uses an LLM to translate natural language into Prolog. The work explores how structured, rule-based logic can make question answering more explainable than prompting a model alone.

All demos use a small family-tree knowledge base (parent, male, female facts with grandparent and ancestor rules).

Built with Aman Avinash as lab deliverables for Prof. Gilpin's AIEA Lab at UC Santa Cruz.

## Demos

| Folder | What it does | Uses an LLM |
| :--- | :--- | :--- |
| `prolog/` | `kb.pl` is a Prolog family tree. `python_prolog_demo.py` loads it through `pyswip` and runs grandparent queries. | No |
| `prolog/` | `naturalLanguage_toprolog.py` sends a sentence to OpenAI `gpt-4o-mini`, asks for Prolog facts, rules and a `?-` query, loads them into SWI-Prolog with `assertz`, and prints the query results. | Yes (OpenAI) |
| `datalog/` | `datalog.py` defines the same family tree in `pyDatalog` and queries grandparents and grandchildren. | No |
| `Backward Chaining Engine/` | `backward_chaining.py` is a from-scratch backward chainer with unification and an occurs check, run on a recursive `ancestor` rule. | No |
| `LangChain and LangGraph/` | `lang_graph.py` builds a four-node LangGraph `StateGraph` (retrieve, judge relevance, refine with Python rule functions, answer) and answers "Who is the grandparent of lisa?". The PDF in this folder is the lab write-up for this task. | No |

## Setup

Requirements:

* Python 3.9+
* [SWI-Prolog](https://www.swi-prolog.org/Download.html) installed and on your PATH (needed by `pyswip` for both Prolog demos), e.g. `brew install swi-prolog` on macOS
* An OpenAI API key, only for the natural-language-to-Prolog demo

```bash
git clone https://github.com/sakisaki-dev/LLM-Logic-Demos.git
cd LLM-Logic-Demos
python -m venv venv && source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

For the LLM demo, create a `.env` file in the repo root (it is gitignored):

```
OPENAI_API_KEY=your-key-here
```

## Running

| Demo | Command |
| :--- | :--- |
| Prolog KB queried from Python | `cd prolog && python python_prolog_demo.py` (must run from `prolog/` because it loads `kb.pl` by relative path) |
| Natural language to Prolog | `python prolog/naturalLanguage_toprolog.py` (see Known issues) |
| Datalog | `python datalog/datalog.py` |
| Backward chaining | `python "Backward Chaining Engine/backward_chaining.py"` |
| LangGraph pipeline | `python "LangChain and LangGraph/lang_graph.py"` |

## Known issues

* `naturalLanguage_toprolog.py` defines `main()` but never calls it, so the script exits without doing anything. Add `if __name__ == "__main__": main()` at the end to run it.
* The backward chaining engine keeps only the first solution of each subgoal and does not rename rule variables between recursive calls, so `ancestor(alice, Y)` returns only `bob` instead of `bob`, `charlie` and `david`.
* In `lang_graph.py` the `judge` node sets a `relevant` flag, but the graph always continues to `refine`; there is no conditional edge that stops on irrelevant questions. Retrieval is keyword matching, and the answer comes from Python rule functions, not a model.
* `langchain` and `langchain-community` are listed in `requirements.txt` but not imported by any demo.

## Related

Earlier versions of these lab tasks are archived in separate repos: [task4AIEA](https://github.com/sakisaki-dev/task4AIEA) (Prolog and Python), [task6AIEA](https://github.com/sakisaki-dev/task6AIEA) (Datalog), [task7AIEA](https://github.com/sakisaki-dev/task7AIEA) (backward chaining).
