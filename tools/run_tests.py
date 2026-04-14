import sys
import os
import unittest

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


def main():
    args = sys.argv[1:]

    start_dir = "tests/unit"
    pattern = "*_spec.py"
    top_level = ROOT
    verbosity = 1
    failfast = False
    k_filter = None

    i = 0
    while i < len(args):
        a = args[i]
        if a == "-s" and i + 1 < len(args):
            i += 1
            start_dir = args[i]
        elif a == "-p" and i + 1 < len(args):
            i += 1
            pattern = args[i]
        elif a == "-k" and i + 1 < len(args):
            i += 1
            k_filter = args[i]
        elif a == "-v":
            verbosity = 2
        elif a == "-f":
            failfast = True
        i += 1

    abs_start = os.path.join(ROOT, start_dir)

    loader = unittest.TestLoader()
    suite = loader.discover(start_dir=abs_start, pattern=pattern, top_level_dir=top_level)

    if k_filter:
        suite = _filter_suite(suite, k_filter)

    runner = unittest.TextTestRunner(verbosity=verbosity, failfast=failfast)
    result = runner.run(suite)
    sys.exit(0 if result.wasSuccessful() else 1)


def _filter_suite(suite, keyword):
    filtered = unittest.TestSuite()
    for item in suite:
        if isinstance(item, unittest.TestSuite):
            child = _filter_suite(item, keyword)
            if child.countTestCases() > 0:
                filtered.addTest(child)
        else:
            if keyword in item.id():
                filtered.addTest(item)
    return filtered


if __name__ == "__main__":
    main()
