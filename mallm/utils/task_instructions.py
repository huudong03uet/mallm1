TASK_INSTRUCTIONS: dict[str, str] = {
    "etpc": "Paraphrase the provided text into a single paraphrase by using all paraphrase types.",
    "wmt19_de_en": "Translate the provided text from German to English.",
    "simple_ethical_questions": "Answer the provided question by choosing option A), B), C), or D). Include the letter corresponding to your answer in the solution.",
    "squad_v2": "Answer the following question. If the question is not answerable with the provided information, write '[UNKNOWN]'.",
    "strategyqa": "Answer the following question with A) Yes or B) No. Include the letter corresponding to your answer in the solution.",
    "xsum": "Summarize the provided text into one sentence.",
    "mmlu_pro": "Answer the provided question by choosing one option. Include the letter corresponding to your answer in the solution.",
    "musr": "Solve the mystery. Make sure to always include the full name of the suspect in your solution.",
    "gpqa": "Answer the provided question by choosing option A), B), C), or D). Include the letter corresponding to your answer in the solution.",
    "math_lvl5": "Answer the following math question. Output the number as the final solution.",
    "ifeval": "Follow the instruction.",
    "winogrande": "Correctly fill the blank space _ by choosing option A) or B). Include the letter corresponding to your answer in the solution.",
    "ethics": "Would most people believe this reasonable or unreasonable to say? Answer with A) Reasonable or B) Unreasonable. Include the letter corresponding to your answer in the solution.",
    "aqua_rat": "Answer the following math question. Include the letter corresponding to your answer in the solution.",
    "coliee_task4": """You are solving COLIEE Task 4, a binary Japanese legal entailment task.

Given:
- input: a Japanese legal statement
- context: relevant Japanese Civil Code article(s)

Decide whether the input statement is entailed by the provided context.

Use only the provided context as legal authority. Do not use outside legal knowledge, case law, commentary, examples, or Civil Code articles not included in the context.

Your response must follow this exact format:

Reason: <brief reason based only on the provided context>
Answer is: <Yes or No>

Decision rules:
- Use "Yes" if the input statement is fully supported by the provided context.
- Use "No" if the input statement is contradicted, only partially supported, requires outside legal rules, depends on missing conditions, ignores an exception, or cannot be inferred from the provided context.
- The final line must be exactly "Answer is: Yes" or "Answer is: No".
- Do not output markdown headings, bullet points, tables, JSON, citations, or any extra text.
- Keep the reason short: one or two sentences only.
"""}
