# Natural Language Processing (NLP) — Beginner Friendly Notes

---

# 1. What is NLP?

## Definition
Natural Language Processing (NLP) is a field of AI that helps computers understand, process, and generate human language.

Human language includes:
- English
- Hindi
- Chat messages
- Voice commands
- Emails
- Documents

---

# 2. Real World Applications of NLP

- ChatGPT
- Google Translate
- Voice Assistants (Alexa, Siri)
- Spam Detection
- Sentiment Analysis
- Chatbots
- Auto-correct
- Text Summarization

---

# 3. NLP Workflow

```text
Raw Data
    ↓
Data Preprocessing
    ↓
Feature Extraction
    ↓
Model Training
    ↓
Language Understanding
    ↓
Output Generation
    ↓
Task Execution
```

---

# 4. Text Preprocessing

## Definition
Text preprocessing means cleaning and preparing text before giving it to AI models.

Raw text usually contains:
- Punctuation
- Emojis
- Extra spaces
- Symbols
- Unnecessary words

Preprocessing converts messy text into clean text.

---

# 5. Text Preprocessing Steps

```text
Cleaning
   ↓
Tokenization
   ↓
Stopword Removal
   ↓
POS Tagging
   ↓
NER Tagging
   ↓
Stemming & Lemmatization
```

---

# 6. Cleaning

## Definition
Cleaning removes unwanted things from text.

## Example

### Raw Text
```text
"Hello!!! How are you??? 😊"
```

### After Cleaning
```text
"hello how are you"
```

## Common Cleaning Tasks
- Lowercase conversion
- Removing punctuation
- Removing emojis
- Removing special characters
- Removing extra spaces

---

# 7. Tokenization

## Definition
Tokenization means breaking text into smaller pieces called **tokens**.

Tokens can be:
- Words
- Characters
- Sentences

## Example

### Sentence
```text
"I love AI"
```

### After Tokenization
```python
["I", "love", "AI"]
```

## Types of Tokenization

| Type | Example |
|---|---|
| Word Tokenization | `"I love AI" → ["I","love","AI"]` |
| Character Tokenization | `"AI" → ["A","I"]` |
| Sentence Tokenization | Splitting paragraphs into sentences |

---

# 8. Stopword Removal

## Definition
Stopwords are common words that usually do not add much meaning.

## Examples
- is
- am
- the
- a
- an
- are

## Example

### Sentence
```text
"I am learning NLP"
```

### After Stopword Removal
```python
["learning", "NLP"]
```

---

# 9. POS Tagging (Part of Speech Tagging)

## Definition
POS Tagging identifies the grammatical role of words.

## Common POS Tags

| Word Type | Example |
|---|---|
| Noun | boy, car |
| Verb | run, eat |
| Adjective | beautiful |
| Adverb | quickly |

## Example

### Sentence
```text
"Rahul eats mango"
```

### POS Tags

| Word | POS |
|---|---|
| Rahul | Noun |
| eats | Verb |
| mango | Noun |

---

# 10. NER (Named Entity Recognition)

## Definition
NER identifies important entities from text.

## Types of Entities
- Person Names
- Locations
- Organizations
- Dates
- Money

## Example

### Sentence
```text
"Elon Musk lives in America"
```

### NER Output

| Word | Entity |
|---|---|
| Elon Musk | Person |
| America | Location |

---

# 11. Stemming

## Definition
Stemming removes word endings to get root words.

## Example

| Original Word | Stem Word |
|---|---|
| playing | play |
| running | run |
| studies | studi |

## Problem
Stemmed words may not always be proper English words.

### Example
```text
studies → studi
```

---

# 12. Lemmatization

## Definition
Lemmatization converts words into meaningful root words.

## Example

| Original Word | Lemma |
|---|---|
| studies | study |
| running | run |
| better | good |

## Difference Between Stemming & Lemmatization

| Stemming | Lemmatization |
|---|---|
| Faster | More accurate |
| May create invalid words | Produces meaningful words |

---

# 13. Embeddings

## Definition
Embeddings convert words into numerical vectors.

AI models understand numbers, not text.

So words are converted into vectors.

---

# 14. Why Embeddings are Important?

Embeddings help AI understand:
- Meaning
- Similarity
- Context
- Relationships between words

---

# 15. Example of Embedding

```python
cat → [0.21, 0.88, 0.45]
dog → [0.19, 0.82, 0.41]
```

Notice:
- `cat` and `dog` vectors are similar because both are animals.

---

# 16. Word Similarity in Embeddings

Words with similar meanings have similar vectors.

## Examples
- King ≈ Queen
- Car ≈ Vehicle
- Dog ≈ Puppy

---

# 17. Popular Embedding Techniques

| Technique | Description |
|---|---|
| Word2Vec | Learns word relationships |
| GloVe | Uses word co-occurrence |
| FastText | Handles subwords |
| BERT Embeddings | Context-aware embeddings |

---

# 18. Language Modeling

## Definition
Language Modeling means predicting the next word in a sentence.

---

# 19. Example of Language Model

## Input
```text
"I love playing"
```

## Prediction
- cricket
- football
- games

---

# 20. How Language Models Work

Language models learn patterns from huge text data.

They understand:
- Grammar
- Sentence structure
- Context
- Word relationships

---

# 21. Types of Language Models

| Type | Example |
|---|---|
| Statistical Models | N-grams |
| Neural Language Models | RNN, LSTM |
| Transformer Models | GPT, BERT |

---

# 22. N-Gram Language Model

## Definition
N-gram predicts the next word using previous words.

## Example

### Bigram (2 words)
```text
"I love"
```

### Predicts
- AI
- coding
- music

---

# 23. RNN & LSTM in NLP

## RNN (Recurrent Neural Network)

RNN remembers previous words.

### Useful For
- Text generation
- Speech processing

### Problem of RNN
Cannot remember long context well.

---

## LSTM (Long Short-Term Memory)

LSTM solves the RNN memory problem.

### Better For
- Long sentences
- Sequence understanding

---

# 24. Transformers in NLP

## Definition
Transformers process all words together using the **Attention Mechanism**.

## Used In
- ChatGPT
- Gemini
- Claude
- BERT

---

# 25. Attention Mechanism

## Definition
Attention helps the model focus on important words.

## Example

### Sentence
```text
"I love playing cricket"
```

For understanding `"playing"`:
- The model focuses on `"cricket"`.

---

# 26. NLP Pipeline Summary

```text
Raw Text
    ↓
Cleaning
    ↓
Tokenization
    ↓
Stopword Removal
    ↓
POS Tagging
    ↓
NER
    ↓
Embeddings
    ↓
Model Training
    ↓
Language Understanding
    ↓
Prediction / Output
```

---

# 27. Important NLP Terms

| Term | Meaning |
|---|---|
| NLP | Processing human language |
| Tokenization | Breaking text into tokens |
| Stopwords | Common unnecessary words |
| POS Tagging | Grammar identification |
| NER | Entity extraction |
| Stemming | Removing suffixes |
| Lemmatization | Meaningful root word generation |
| Embeddings | Word vectors |
| Language Model | Predicts next word |
| Transformer | Attention-based NLP model |

---

# 28. Real Industry Applications

## NLP is Used In:
- Chatbots
- AI Assistants
- Translation Systems
- Recommendation Systems
- Sentiment Analysis
- Voice Assistants
- Search Engines
- Auto-complete Systems

---


---

# 29. Final Beginner Understanding

```text
Text
  ↓
Preprocessing
  ↓
Convert into Tokens
  ↓
Convert into Vectors (Embeddings)
  ↓
Train NLP Model
  ↓
Understand Language
  ↓
Generate Predictions
```

---
