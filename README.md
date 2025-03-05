# PA5 Grading Script Guide
Because manually grading 100+ queue simulations is how TAs lose their souls.

## Setup

1. **Install Python 3.8+**  
   Because we’re not savages.

2. **Install dependencies**  
   ```bash
   pip install pyyaml
   ```

3. **Organize Submissions**

Create a folder called grade in the same directory as this script.

Place each student’s submission folder inside grade, named as Last_Name_PA5.
Example:

```bash
grader.yml
grading_script.py
/grade
  /Doe_PA5
  /Smith_PA5
  ...
```

4. **Ensure Executables**

Each student’s folder must contain a compiled executable. The script looks for:

pa5, PA5, GrocerySim, or any .exe/.out file.
(Pro tip: Compile with g++ -std=c++20 *.cpp -o pa5)

**Usage**

```bash

python grading_script.py```

**Output**
✅ Pass: Test succeeded.

❌ Fail: Output missing expected text.

💤 Timeout: Code ran longer than 30 seconds (infinite loop?).

💥 Crash: Executable failed to run (segfault, exception, etc.).

**Notes**
The script is case-insensitive and ignores minor typos.

Students who hardcode output will be cursed

For best results, run this while listening to indie music. 🎧
---

### How It Works:
1. **YAML Configuration**: Defines test cases with expected output snippets.

2. **Python Script**: 
   - Finds student executables (handles CLion, VS, VS Code builds).
   - Runs each test, checks if expected strings appear in output.
   - Prints colorful results (because monotony kills).

3. **Cross-Platform**: Uses `subprocess` and `os` modules for OS compatibility.

Now go forth and grade like the automation-loving TA you were born to be! 🚀
