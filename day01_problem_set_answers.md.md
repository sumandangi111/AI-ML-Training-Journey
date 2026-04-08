# Day 01 - Problem Set (Interview Answers) 💼

---

## 🚀 Python vs Other Languages (Practical Differences)

### ❓ Why does Python not require semicolons? What trade-off?
👉 Python uses newline and indentation instead of semicolons, making code cleaner and more readable.  
👉 Trade-off: Python parser depends on indentation, so wrong spacing can cause errors.

---

### ❓ Why is indentation syntax in Python?
👉 Python uses indentation to define code blocks, ensuring consistent and readable code.  
👉 Other languages use `{}` so indentation is optional there.

---

### ❓ Dynamic typing vs static typing?
👉 Python is dynamically typed, so variable types are decided at runtime.  
👉 This gives flexibility but may cause runtime errors.  
👉 Static typing (like Java) catches errors earlier during compilation.

---

### ❓ Why is Python slower than C++?
👉 Python code is first converted to bytecode and then executed by a virtual machine.  
👉 C++ is directly compiled into machine code, so it runs faster.

---

### ❓ What problem does garbage collection solve?
👉 Python automatically removes unused memory (garbage collection).  
👉 In C, programmers must manage memory manually, which can cause memory leaks.

---

### ❓ Why multiple return values in Python?
👉 Python allows returning multiple values using tuples, making code shorter and flexible.  
👉 Java requires objects or arrays for this.

---

## 🚀 Interpreter vs Compiler

### ❓ Why interpreter executes line by line?
👉 Interpreter reads, converts, and executes code one line at a time, without creating an executable file.

---

### ❓ Error detection timing?
👉 Interpreter → errors occur at runtime (line by line).  
👉 Compiler → errors detected before execution (compile time).

---

### ❓ Why interpreted languages feel slower but flexible?
👉 No compilation step makes development fast and flexible, but execution is slower due to real-time translation.

---

### ❓ Why debugging easier?
👉 Errors are shown immediately at the exact line, making debugging simple.

---

### ❓ Is Python pure interpreter?
👉 No, Python is hybrid. It first compiles code into bytecode, then executes it using PVM.

---

### ❓ Why Python needs runtime?
👉 Python depends on Python Virtual Machine (PVM) to run code, so runtime environment is required.

---

## 🚀 Python Interpreter-Specific

### ❓ What happens when running `python file.py`?
👉 Step 1: Code → Bytecode  
👉 Step 2: Bytecode → executed by PVM  

---

### ❓ Where does `.pyc` come from?
👉 Python automatically creates `.pyc` files to store bytecode and speed up execution.

---

### ❓ Why Python uses Virtual Machine?
👉 To make code platform-independent (runs on any OS).

---

### ❓ How memory is managed?
👉 Python uses garbage collection and reference counting to manage memory automatically.

---

### ❓ Why Python is cross-platform?
👉 Because code runs on PVM instead of directly on OS.

---

## 🚀 Compiler vs Interpreter (Comparison)

### ❓ Why compiled code is faster?
👉 It is directly converted into machine code before execution.

---

### ❓ Why interpreted languages are portable?
👉 They run on a virtual machine available on different systems.

---

### ❓ Compile-time vs runtime — which safer?
👉 Compile-time is safer because errors are detected early.  
👉 Runtime is flexible but errors occur during execution.

---

### ❓ Why compilers optimize better?
👉 Compilers analyze the entire code and optimize it before execution.

---

### ❓ Why interpreters good for prototyping?
👉 They allow quick testing and changes without recompilation.

---

## 🚀 Comments (Real Understanding)

### ❓ Why Python ignores comments?
👉 Comments are not executed; they are only for developer understanding.

---

### ❓ Comments vs Docstrings?
👉 Comments → explain code for developers  
👉 Docstrings → used for documentation (functions/classes)

---

### ❓ Why excessive comments bad?
👉 Too many comments reduce readability. Good code should explain itself.

---

### ❓ When avoid comments?
👉 Avoid when code is simple and self-explanatory.

---

### ❓ Comments impact?
👉 Improve readability but excessive use reduces maintainability.

---

## 🚀 Trick / Thinking Questions

### ❓ If Python is interpreted, why `.pyc`?
👉 Because Python first compiles code into bytecode before execution.

---

### ❓ Can a language be both compiled and interpreted?
👉 Yes. Python is compiled to bytecode and then interpreted by PVM.

---

### ❓ Why removing comments doesn’t affect behavior?
👉 Because comments are ignored during execution.  
👉 But removing them can reduce understanding of code.

---

### ❓ Why Python is called slow but used in AI?
👉 Python is easy to use and has powerful libraries.  
👉 Heavy computations are handled by optimized C/C++ code internally.

---

### ❓ How Python handles functions defined later?
👉 Python reads the whole file before execution, so functions can be used even if defined later.

---