# tests/test_detector.py
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from chottobondhu_gaza.detector import detect_trauma

def test_detect_trauma():
    # Test case 1: Text with trauma-related keywords
    text1 = "I am scared of the bomb and my brother is hurt."
    result1 = detect_trauma(text1)
    assert result1 == "⚠️ Possible trauma detected", f"Test failed: {result1}"

    # Test case 2: Text without trauma-related keywords
    text2 = "I love playing with my friends."
    result2 = detect_trauma(text2)
    assert result2 == "No critical signs", f"Test failed: {result2}"

    print("All tests passed!")

# Run the test
test_detect_trauma()
