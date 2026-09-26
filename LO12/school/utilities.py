"""Utility functions for student management."""

def calculate_total(scores):
    return sum(scores)

def calculate_average(scores):
    return sum(scores) / len(scores) if scores else 0

def display_header():
    print("=" * 40)
    print("      STUDENT MANAGEMENT APPLICATION")
    print("=" * 40)
