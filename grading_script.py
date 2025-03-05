#!/usr/bin/env python3
"""
Grading Script for CptS 122 PA5: Grocery Store Simulation
TA Edition. Comes with built-in sarcasm and existential dread.
"""
import os
import subprocess
import yaml
from time import sleep

# Configuration
GRADE_DIR = "grade"  # Where student submissions hide
EXECUTABLE_NAMES = ["pa5", "PA5", "GrocerySim"]  # Because naming is hard
TEST_TIMEOUT = 30  # Seconds before we assume their code entered an infinite loop

def find_executable(student_dir):
    """Locate the student's executable. Like Where's Waldo, but less fun."""
    for root, _, files in os.walk(student_dir):
        for file in files:
            if file in EXECUTABLE_NAMES or file.endswith((".exe", ".out")):
                return os.path.join(root, file)
    return None  # Cue dramatic "no executable found" music

def run_test(executable, test_input):
    """Run the student's code and capture output. Pray for no segfaults."""
    try:
        proc = subprocess.run(
            [executable],
            input=test_input.encode(),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=TEST_TIMEOUT
        )
        return proc.stdout.decode().lower()  # Case-insensitive because typos
    except subprocess.TimeoutExpired:
        return "timeout"  # Student code is now in the shadow realm
    except:
        return "error"  # Because why handle exceptions when you can panic?

def grade_student(student_folder):
    """Grade a single student. May cause mild despair."""
    print(f"\nGrading {student_folder}...")
    exec_path = find_executable(os.path.join(GRADE_DIR, student_folder))
    
    if not exec_path:
        print("  ❌ No executable found. F for respect.")
        return
    
    with open("grader.yml", "r") as f:
        tests = yaml.safe_load(f)["tests"]
    
    for test in tests:
        print(f"  🧪 {test['name']}", end="")
        output = run_test(exec_path, test["input"])
        
        if "timeout" in output:
            print(" - 💤 Timeout. Did they code a black hole?")
            continue
        if "error" in output:
            print(" - 💥 Crash. Better call a debugger... or a priest.")
            continue
        
        all_pass = True
        for expected_line in test["expected"]:
            if expected_line.lower() not in output:
                all_pass = False
                break
        
        print(" - ✅ Pass" if all_pass else " - ❌ Fail")

def main():
    """Main function. Tears optional."""
    student_folders = [f for f in os.listdir(GRADE_DIR) if f.startswith("Last_Name_PA5")]
    
    if not student_folders:
        print("No students to grade. Go home early! 🎉")
        return
    
    for student in student_folders:
        grade_student(student)
    print("\nGrading complete. Now go cry in the break room.")

if __name__ == "__main__":
    main()
