# AI Notes – Generative AI, Agentic AI & Prompt Engineering

---

# 1. Types of AI on the Basis of Functionality

AI can be divided into 4 types based on how they function and respond.

---

## 1. Reactive Machines

These AI systems:

- Have no memory
- Only react to current input
- Cannot learn from past experience

### Simple Understanding
> “Only reacts to the present situation.”

### Example
Chess-playing AI

If the board changes, it reacts according to current moves only.

---

## 2. Limited Memory AI

These systems:

- Store a limited amount of past data
- Use previous information for decisions

Most modern AI systems belong here.

### Simple Understanding
> “Learns using some past experience.”

### Examples

- Self-driving cars
- Recommendation systems
- Chatbots with conversation memory

---

## 3. Theory of Mind AI

This AI can understand:

- Human emotions
- Intentions
- Feelings
- Behavior

### Simple Understanding
> “AI that can understand humans emotionally.”

### Current Status
Still under research and not fully developed.

---

## 4. Self-Aware AI

This is the most advanced AI concept.

Such AI would:

- Be conscious
- Understand itself
- Think like humans emotionally

### Simple Understanding
> “AI that becomes self-conscious like humans.”

### Current Status
Does not exist yet.

---

# Easy Revision

| Type | Main Idea |
|---|---|
| Reactive Machine | No memory |
| Limited Memory | Uses past data |
| Theory of Mind | Understands emotions |
| Self-Aware AI | Conscious AI |

---

# 2. Generative AI (Gen AI)

Generative AI is AI that creates new content.

It can generate:

- Text
- Images
- Videos
- Music
- Code

### Simple Definition
> Gen AI creates something new using learned data.

---

## Examples of Generative AI

- ChatGPT → Generates text
- Google Gemini → Generates text/images
- AI image generators
- AI video generators

---

# How Gen AI Works

Gen AI:

1. Learns patterns from huge datasets  
2. Understands prompts  
3. Generates new output  

---

## Examples

| Input | Generated Output |
|---|---|
| “Write a poem” | AI writes poem |
| “Create cat image” | AI generates image |
| “Explain Python” | AI generates explanation |

---

# 3. Agentic AI

Agentic AI not only generates content but also performs tasks automatically.

### Simple Definition
> Agentic AI can think, plan, and perform actions to complete a goal.

---

# Difference Between Gen AI and Agentic AI

| Generative AI | Agentic AI |
|---|---|
| Generates content | Performs actions/tasks |
| Gives output | Takes decisions |
| Needs user commands | Can act automatically |
| Example: ChatGPT response | AI booking ticket automatically |

---

# Simple Understanding

## Gen AI

```text
User asks → AI generates answer
```

## Agentic AI

```text
User gives goal → AI plans + performs tasks
```

---

# Example of Agentic AI

Suppose user says:

> “Book my meeting and send reminder.”

Agentic AI can:

- Check calendar
- Schedule meeting
- Send notification

without asking for every step.

---

# 4. Prompt Engineering

Prompt Engineering means writing better instructions/prompts to get better AI responses.

### Simple Definition
> Prompt Engineering is the skill of communicating properly with AI.

---

# Why Prompt Engineering is Important

Better prompts = Better output

AI works according to:

- Instructions
- Context
- Examples

---

# RTS Technique

RTS stands for:

| Letter | Meaning |
|---|---|
| R | Role |
| T | Task |
| S | Style |

---

# Understanding RTS

## 1. Role

Tell AI who it should behave like.

### Examples

- Teacher
- Developer
- Interviewer

---

## 2. Task

Tell AI what work to do.

### Examples

- Explain AI
- Write code
- Create notes

---

## 3. Style

Tell AI how the output should look.

### Examples

- Simple language
- Professional tone
- Bullet points

---

# RTS Prompt Example

```text
Role: Act as a teacher

Task: Explain Machine Learning

Style: Use simple language with examples
```

---

# 5. Types of Prompt Engineering

---

## 1. One-Shot Prompting

AI is given:

- One example
- One task

### Simple Understanding
> “Learning from one example.”

### Example

```text
Example:
Good → Positive

Now classify:
"This movie is amazing."
```

---

## 2. Few-Shot Prompting

AI is given:

- Multiple examples
- Then the task

### Simple Understanding
> “Learning from multiple examples.”

---

## 3. Zero-Shot Prompting

AI performs task directly without examples.

### Simple Understanding
> “Only task is given.”

### Example

```text
Translate this sentence into Hindi.
```

---

## 4. Chain of Thought Prompting

AI explains solution step-by-step.

### Simple Understanding
> “Reasoning step by step.”

### Example

```text
Solve step by step:
If 2x + 3 = 11, find x.
```

---

## 5. Role-Based Prompting

AI is assigned a specific role before answering.

### Example

```text
Act as a professional interviewer.
```

---

# Quick Revision Table

| Prompt Type | Meaning |
|---|---|
| Zero-Shot | No examples |
| One-Shot | One example |
| Few-Shot | Multiple examples |
| Chain of Thought | Step-by-step reasoning |
| Role-Based | AI behaves like a role |

---

# Final Understanding

```text
Gen AI = Generates content

Agentic AI = Performs tasks intelligently

Prompt Engineering = Giving smart instructions to AI
```