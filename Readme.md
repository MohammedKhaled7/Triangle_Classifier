# Triangle Classifier

## Overview
`Triangle_Classifier` is a Python application that classifies triangles based on side lengths. It outputs one of the following words: `Scalene`, `Isosceles`, `Equilateral`, or `NoTriangle`. If the input is invalid, it returns a relevant error message.

## How to Run
1. Clone the repository:
git clone <repo-url>


2. Navigate to the project directory:
cd Triangle_Classifier/src


3. Run the application:
python triangle_classifier.py



## Test Suite
- **Conformance**: Valid triangle classification.
- **Error Handling**: Proper error messages for invalid inputs.
- **Performance**: Handles large input sizes efficiently.
- **Reliability**: Stable across multiple executions.
- **Security**: Safely handles unexpected or malicious input.

## Usage Example
Input: 1 1 1 Output: Equilateral

Input: 1 Output: Error: Two sides missing

Input: Quit Application exits.