import os
from dotenv import load_dotenv
from openai import OpenAI
from pyswip import Prolog
import re

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def natural_language_to_prolog(nl_input):
    prompt = f"""
Translate the following natural language statement into Prolog facts, rules, and a query.
Return ONLY the Prolog code block (no explanations or Markdown):
"{nl_input}"
"""
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )
    return response.choices[0].message.content.strip()

def parse_prolog_code(prolog_text):
    # Extract everything inside ```prolog ... ```
    code_blocks = re.findall(r"```prolog(.*?)```", prolog_text, re.DOTALL)
    if not code_blocks:
        code_blocks = [prolog_text]  # fallback: use whole text

    code = "\n".join(code_blocks).strip()
    lines = [line.strip() for line in code.splitlines() if line.strip() and not line.strip().startswith('%')]

    facts, rules, query = [], [], None
    for line in lines:
        if ":-" in line:
            rules.append(line.rstrip('.'))
        elif line.startswith("?-"):
            query = line.lstrip("?-").rstrip(".").strip()
        else:
            facts.append(line.rstrip('.'))
    return facts, rules, query

def run_prolog(facts, rules, query):
    prolog = Prolog()
    for f in facts + rules:
        prolog.assertz(f)
    return list(prolog.query(query))

def main():
    nl_input = input("Enter a natural language query:\n> ")
    prolog_text = natural_language_to_prolog(nl_input)
    print("\nGenerated Prolog:\n", prolog_text)

    facts, rules, query = parse_prolog_code(prolog_text)
    if not query:
        print("No query found.")
        return

    results = run_prolog(facts, rules, query)
    print("\nQuery Results:", results)



