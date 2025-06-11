# Concept Extractor Tool

##  Submission Info

* **Author**: \[Sameer Ladekar / 22b2275]

##  Objective

This Python-based tool extracts the **underlying concepts** being tested in multiple-choice questions from competitive exams like UPSC, UGC-NET, etc. It supports both **rule-based keyword matching** and **simulated LLM-based extraction**. The goal is to assist with:

* **Curriculum mapping**
* **Trend analysis** of concepts
* **Targeted preparation** by identifying topic weightage

---

## 📂 Project Structure

```
concept_extractor/
├── main.py                     # Main CLI entry point
├── concept_extractor.py       # Rule-based concept extraction
├── csv_reader.py              # Reads formatted CSVs
├── llm_api.py                 # Loads simulated LLM outputs from JSON
├── concepts/                  # Subject-wise keyword-to-concept mappings
│   └──ancient_history.json
├── resources/                 # Question CSVs (input)
│   └──ancient_history.csv
├── simulated_llm_outputs/     # LLM-style concept mappings (manual or ChatGPT-generated)
│   └── ancient_history.json
├── output_concepts.csv        # Final output file (auto-generated)
├── concept_distribution.png   # Chart showing concept frequency
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation
```

---

##  Installation

Install required Python packages:

```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

---

##  How to Use

### 🔹 Rule-Based Extraction (Offline)

```bash
python main.py --subject=ancient_history
```

Example Output:

```
Question 1: Harappan Civilization, Urban Planning
```

### 🔹 Simulated LLM-Based Extraction (using JSON)

```bash
python main.py --subject=ancient_history --use-llm
```

Example Output:

```
Question 1: Harappan Civilization, Urban Planning
[INFO] concept_distribution.png generated.
```

### 🔹 Output File (CSV)

Auto-generated:

```
output_concepts.csv
```

Format:

```
Question Number,Question,Concepts
1,"Which...Harappan civilization?","Harappan Civilization; Urban Planning"
```

---

##  Simulated LLM Prompt Format

When preparing simulated data:

```
Given the question: "<question text>", identify the historical concept(s) it is based on.
```

Used for files like:

```
simulated_llm_outputs/ancient_history.json
```

Example:

```json
{
  "1": ["Harappan Civilization", "Urban Planning"],
  "2": ["Mauryan Empire", "Arthashastra"]
}
```

---

##  Concept Frequency Visualization

After execution, this chart is generated:

```
concept_distribution.png
```

It summarizes the number of times each concept appears across questions.

---

##  Adding New Subjects

To support a new subject (e.g., biology):

1. Add a file: `resources/biology.csv`
2. Add keywords: `concepts/biology.json`
3. (Optional) Add LLM output: `simulated_llm_outputs/biology.json`
4. Run:

```bash
python main.py --subject=biology
```

---

## 🧾 Requirements (Included in requirements.txt)

```
spacy==3.7.2
nltk==3.8.1
matplotlib==3.8.4
fuzzywuzzy==0.18.0
python-Levenshtein==0.25.1
rapidfuzz>=3.8.0
python-dotenv==1.0.1
```

---





