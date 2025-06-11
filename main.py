import argparse
import os
import json
from csv_reader import read_csv
from concept_extractor import extract_concepts
from llm_api import get_concepts_from_llm, load_simulated_llm
from collections import Counter
import matplotlib.pyplot as plt

def write_output(filepath, results):
    with open(filepath, 'w', encoding='utf-8') as out:
        out.write('Question Number,Question,Concepts\n')
        for row in results:
            out.write(f'{row["qnum"]},"{row["question"]}","{"; ".join(row["concepts"])}"\n')

def visualize_concepts(results):
    all_concepts = []
    for row in results:
        all_concepts.extend(row["concepts"])
    counter = Counter(all_concepts)
    plt.figure(figsize=(10, 6))
    plt.barh(list(counter.keys()), list(counter.values()))
    plt.title("Concept Distribution")
    plt.xlabel("Frequency")
    plt.tight_layout()
    plt.savefig("concept_distribution.png")
    print("[INFO] concept_distribution.png generated.")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--subject', required=True, help='Subject name, e.g., ancient_history')
    parser.add_argument('--use-llm', action='store_true', help='Use LLM (simulated) for concept extraction')
    args = parser.parse_args()

    input_file = f'resources/{args.subject}.csv'
    dict_file = f'concepts/{args.subject}.json'
    output_file = 'output_concepts.csv'

    if not os.path.exists(input_file):
        print(f"[ERROR] CSV file not found: {input_file}")
        return

    if args.use_llm:
        load_simulated_llm(args.subject)
    else:
        if not os.path.exists(dict_file):
            print(f"[ERROR] Concept dictionary not found: {dict_file}")
            return
        with open(dict_file, 'r', encoding='utf-8') as f:
            concept_dict = json.load(f)

    data = read_csv(input_file)
    results = []

    for row in data:
        qnum = row['Question Number']
        question = row['Question']
        if args.use_llm:
            concepts = get_concepts_from_llm(question, qnum)
        else:
            concepts = extract_concepts(question, concept_dict)

        print(f"Question {qnum}: {', '.join(concepts)}")
        results.append({"qnum": qnum, "question": question, "concepts": concepts})

    write_output(output_file, results)
    visualize_concepts(results)

if __name__ == "__main__":
    main()
