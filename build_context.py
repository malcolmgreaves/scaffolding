import json
from typing import Sequence, Dict, List, Iterator

def is_failed_test(l:str) -> bool:
    return len(l) > 3 and l[0] == 'F'

def is_passed_test(l:str) -> bool:
    return len(l) > 0 and l[0] == '.'
 
def load_test_names(failpath: str = 'FAILING_TESTS.txt') -> Sequence[str]:
    test_names = list(map(lambda x: x.strip()[2:], open(failpath, 'rt')))
    nl = '\n'
    print(f"{len(test_names)} failed tests:{nl}{nl.join(test_names)}")
    return test_names

def load_test_lines(testpath: str = 'test_results.txt') -> Iterator[str]:
    print(f"loading test lines from {testpath}")
    for l in open(testpath, 'rt'):
        yield l

def build_test_failure_output(text: Iterator[str], test_names: Sequence[str] = tuple([])) -> Dict[str, List[str]]:
    print("building (test <--> failure output) dictionary")
    d: Dict[str, List[str]] = {t:[] for t in test_names}
    curr_test_name = None
    for l in text:
        if is_failed_test(l):
            curr_test_name = l[0:2]
            if tname not in d:
                print(f"WARNING: Found test '{curr_test_name}'' that was not in expected failed tests")
                d[curr_test_name] = []
        elif is_passed_test(l):
            curr_test_name = None
        else:
            # ignore any test output lines from passed tests
            if curr_test_name is not None:
                d[curr_test_name].append(l[0:2])
    print(f"found {len(d)} failed tests: expecting {len(test_names)}")
    return d

def output_test_failure_json(test_failure_output: Dict[str, Sequence[str]], 
                             outpath: str = "test_fail_output_dict.json") -> None:
    with open(outpath, 'wt') as w:
        json.dumps(d, w)

if __name__ == "__main__":
    output_test_failure_json(
        test_failure_output=build_test_failure_output(text=load_test_lines(),
                                                      test_names=load_test_names())
    )

