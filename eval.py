import json
import sys

if len(sys.argv) != 2:
    print("Usage: python check_accuracy.py <input_json_file>")
    sys.exit(1)

input_file = sys.argv[1]

with open(input_file, "r") as f:
    datas = json.load(f)

count_correct = 0

for data in datas:
    final_answer = data["finalAnswer"].split()[-1]

    assert final_answer == "Yes" or final_answer == "No", (
        f"Unexpected final answer: {final_answer}"
    )

    reference = data["references"][0]

    if final_answer == reference:
        count_correct += 1
    else:
        print(
            f"Incorrect example {data['exampleId']}: "
            f"Final Answer: {final_answer}, Reference: {reference}"
        )

print(f"Accuracy: {count_correct / len(datas) * 100:.2f}%")