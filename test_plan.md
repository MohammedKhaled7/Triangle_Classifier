# Test Plan for Triangle_Classifier Application

## Objective
To validate the functionality, performance, reliability, security, and usability of the `Triangle_Classifier`.

---

## Test Suites and Cases

### 1. Conformance Test Suite
- **Test Case 1.1**: Input: `"1 1 1"` → Output: `"Equilateral"`
- **Test Case 1.2**: Input: `"2 2 3"` → Output: `"Isosceles"`
- **Test Case 1.3**: Input: `"3 4 5"` → Output: `"Scalene"`
- **Test Case 1.4**: Input: `"1 2 3"` → Output: `"NoTriangle"`

### 2. Error Handling Test Suite
- **Test Case 2.1**: Input: `"1"` → Output: `"Error: Two sides missing"`
- **Test Case 2.2**: Input: `"abc def ghi"` → Output: `"Error: Invalid input"`
- **Test Case 2.3**: Input: `"Quit"` → Application exits.
- **Test Case 2.4**: Input: `"Exit"` → Application exits.

### 3. Performance Test Suite
- Provide 10,000 valid triangle inputs and verify response times.
- Test with large, malformed inputs to ensure graceful handling.

### 4. Reliability Test Suite
- Run the program for 1 hour with random valid inputs.
- Ensure consistent outputs across multiple runs.

### 5. Security Test Suite
- Test for SQL injection attempts and unexpected inputs.
- Ensure negative side lengths are handled safely.

---

## Test Criteria
- **Pass**: Application outputs correct triangle classification or error message.
- **Fail**: Application crashes, hangs, or provides incorrect output.
