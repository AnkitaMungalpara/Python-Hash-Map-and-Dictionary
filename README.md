**Merging Word Frequency Dictionaries**

**Objective:**

we've word frequency data from multiple servers. Each server processes text data and returns a dictionary where the keys are words and the values are their frequencies. we want  to merge these dictionaries into a single dictionary that contains all the words and their combined frequencies from all servers.

**Requirements:**

1. **Implement Two Functions:**

   - **a. Using `defaultdict`:** Implement a function named `merge_with_defaultdict(*dicts)` that merges the dictionaries using `collections.defaultdict`.
   - **b. Using `Counter`:** Implement a function named `merge_with_counter(*dicts)` that merges the dictionaries using `collections.Counter`.

2. **Sorting (Bonus):**

   - **Optional:** For bonus points, return the merged dictionary sorted by frequency in descending order (highest to lowest).

**Constraints:**

- You may receive any number of dictionaries as input.
- The words are strings, and frequencies are integers.
- The functions should handle an arbitrary number of dictionaries.
- **Do not use the provided example solution in your implementation.** Write your own code for both functions.

**Examples:**

Given the following dictionaries from three servers:

```python
d1 = {'python': 10, 'java': 3, 'c#': 8, 'javascript': 15}
d2 = {'java': 10, 'c++': 10, 'c#': 4, 'go': 9, 'python': 6}
d3 = {'erlang': 5, 'haskell': 2, 'python': 1, 'pascal': 1}
```

- **Merging all three dictionaries:**

  ```python
  result = {
      'python': 17,
      'javascript': 15,
      'java': 13,
      'c#': 12,
      'c++': 10,
      'go': 9,
      'erlang': 5,
      'haskell': 2,
      'pascal': 1
  }
  ```

- **Merging only `d1` and `d2`:**

  ```python
  result = {
      'python': 16,
      'javascript': 15,
      'java': 13,
      'c#': 12,
      'c++': 10,
      'go': 9
  }
  ```

**Instructions:**

1. **Implement the Functions:**

   - Write  functions in a file named `student_merge.py`.
   - Ensure that  functions accept any number of dictionaries and merge them correctly.
   - For the bonus, ensure the returned dictionary is sorted by frequency in descending order.

2. **Testing:**

   - A test file using `pytest` is provided below.
   - Make sure your implementations pass all the tests when running `pytest`.

3. **CI/CD:**

   - Submit  implementation in the `student_merge.py` file.
   - GitHub Actions to automatically run the tests upon submission.

**Provided Test File (`test_merge.py`):**

```python
# test_merge.py

import pytest

# Import the student's merge functions
from student_merge import merge_with_defaultdict, merge_with_counter

def test_merge_with_defaultdict_all_dicts():
    d1 = {'python': 10, 'java': 3, 'c#': 8, 'javascript': 15}
    d2 = {'java': 10, 'c++': 10, 'c#': 4, 'go': 9, 'python': 6}
    d3 = {'erlang': 5, 'haskell': 2, 'python': 1, 'pascal': 1}

    result = merge_with_defaultdict(d1, d2, d3)
    expected = {
        'python': 17,
        'javascript': 15,
        'java': 13,
        'c#': 12,
        'c++': 10,
        'go': 9,
        'erlang': 5,
        'haskell': 2,
        'pascal': 1
    }
    assert result == expected

def test_merge_with_defaultdict_two_dicts():
    d1 = {'python': 10, 'java': 3, 'c#': 8, 'javascript': 15}
    d2 = {'java': 10, 'c++': 10, 'c#': 4, 'go': 9, 'python': 6}

    result = merge_with_defaultdict(d1, d2)
    expected = {
        'python': 16,
        'javascript': 15,
        'java': 13,
        'c#': 12,
        'c++': 10,
        'go': 9
    }
    assert result == expected

def test_merge_with_counter_all_dicts():
    d1 = {'python': 10, 'java': 3, 'c#': 8, 'javascript': 15}
    d2 = {'java': 10, 'c++': 10, 'c#': 4, 'go': 9, 'python': 6}
    d3 = {'erlang': 5, 'haskell': 2, 'python': 1, 'pascal': 1}

    result = merge_with_counter(d1, d2, d3)
    expected = {
        'python': 17,
        'javascript': 15,
        'java': 13,
        'c#': 12,
        'c++': 10,
        'go': 9,
        'erlang': 5,
        'haskell': 2,
        'pascal': 1
    }
    assert result == expected

def test_merge_with_counter_two_dicts():
    d1 = {'python': 10, 'java': 3, 'c#': 8, 'javascript': 15}
    d2 = {'java': 10, 'c++': 10, 'c#': 4, 'go': 9, 'python': 6}

    result = merge_with_counter(d1, d2)
    expected = {
        'python': 16,
        'javascript': 15,
        'java': 13,
        'c#': 12,
        'c++': 10,
        'go': 9
    }
    assert result == expected

def test_merge_with_defaultdict_empty():
    result = merge_with_defaultdict()
    expected = {}
    assert result == expected

def test_merge_with_counter_empty():
    result = merge_with_counter()
    expected = {}
    assert result == expected

def test_merge_with_defaultdict_single_dict():
    d1 = {'python': 5, 'java': 7}
    result = merge_with_defaultdict(d1)
    expected = {'java': 7, 'python': 5}
    assert result == expected

def test_merge_with_counter_single_dict():
    d1 = {'python': 5, 'java': 7}
    result = merge_with_counter(d1)
    expected = {'java': 7, 'python': 5}
    assert result == expected

def test_merge_with_defaultdict_negative_counts():
    d1 = {'python': -2, 'java': 3}
    d2 = {'python': 5, 'c++': -1}
    result = merge_with_defaultdict(d1, d2)
    expected = {'python': 3, 'java': 3, 'c++': -1}
    assert result == expected

def test_merge_with_counter_negative_counts():
    d1 = {'python': -2, 'java': 3}
    d2 = {'python': 5, 'c++': -1}
    result = merge_with_counter(d1, d2)
    expected = {'python': 3, 'java': 3, 'c++': -1}
    assert result == expected

def test_merge_with_defaultdict_unsorted():
    d1 = {'b': 2, 'a': 3}
    d2 = {'c': 1}
    result = merge_with_defaultdict(d1, d2)
    expected = {'a': 3, 'b': 2, 'c': 1}
    assert result == expected

def test_merge_with_counter_unsorted():
    d1 = {'b': 2, 'a': 3}
    d2 = {'c': 1}
    result = merge_with_counter(d1, d2)
    expected = {'a': 3, 'b': 2, 'c': 1}
    assert result == expected

def test_merge_with_defaultdict_bonus_sorting():
    d1 = {'python': 2, 'java': 3}
    d2 = {'python': 1, 'c++': 5}
    result = merge_with_defaultdict(d1, d2)
    expected = {'c++': 5, 'java': 3, 'python': 3}
    assert result == expected

def test_merge_with_counter_bonus_sorting():
    d1 = {'python': 2, 'java': 3}
    d2 = {'python': 1, 'c++': 5}
    result = merge_with_counter(d1, d2)
    expected = {'c++': 5, 'java': 3, 'python': 3}
    assert result == expected
```


-----------
-----------

**Validate Dictionary Structure Against a Template**

**Objective:**

Task is to implement a function that validates the structure of a nested dictionary against a given template. This is a common requirement when working with JSON data in APIs, where you need to ensure that the received data conforms to a specific structure before processing it.

**Specifications:**

- We will implement a function named `validate(data, template)` that takes two arguments:
  - `data`: A dictionary representing the data to be validated.
  - `template`: A dictionary representing the template against which the data should be validated.

- The function should return a tuple `(state, error)` where:
  - `state` is a boolean value:
    - `True` if the data matches the template.
    - `False` if the data does not match the template.
  - `error` is a string:
    - An empty string `''` if `state` is `True`.
    - A descriptive error message if `state` is `False`, indicating the first error encountered. The error message should be in one of the following formats:
      - For a missing key: `'mismatched keys: key_path'`
      - For a wrong data type: `'bad type: key_path'`
    - The `key_path` should represent the nested path to the problematic key, with keys separated by dots (e.g., `'bio.birthplace.city'`).

**Constraints:**

- Values in the dictionaries can be:
  - Single values (e.g., integers, strings).
  - Dictionaries (nested recursively).
- **No lists** are included as possible values.
- All keys in the template are **required**, and **no extra keys** are permitted in the data.
- You should only check for structure and data types, **not** the actual values.

**Example:**

Given the following `template`:

```python
template = {
    'user_id': int,
    'name': {
        'first': str,
        'last': str
    },
    'bio': {
        'dob': {
            'year': int,
            'month': int,
            'day': int
        },
        'birthplace': {
            'country': str,
            'city': str
        }
    }
}
```

1. **Valid Data:**

```python
john = {
    'user_id': 100,
    'name': {
        'first': 'John',
        'last': 'Cleese'
    },
    'bio': {
        'dob': {
            'year': 1939,
            'month': 11,
            'day': 27
        },
        'birthplace': {
            'country': 'United Kingdom',
            'city': 'Weston-super-Mare'
        }
    }
}

validate(john, template)  # Should return (True, '')
```

2. **Missing Key:**

```python
eric = {
    'user_id': 101,
    'name': {
        'first': 'Eric',
        'last': 'Idle'
    },
    'bio': {
        'dob': {
            'year': 1943,
            'month': 3,
            'day': 29
        },
        'birthplace': {
            'country': 'United Kingdom'
            # Missing 'city' key
        }
    }
}

validate(eric, template)  # Should return (False, 'mismatched keys: bio.birthplace.city')
```

3. **Wrong Data Type:**

```python
michael = {
    'user_id': 102,
    'name': {
        'first': 'Michael',
        'last': 'Palin'
    },
    'bio': {
        'dob': {
            'year': 1943,
            'month': 'May',  # Should be an int
            'day': 5
        },
        'birthplace': {
            'country': 'United Kingdom',
            'city': 'Sheffield'
        }
    }
}


validate(michael, template)  # Should return (False, 'bad type: bio.dob.month')
```

**Instructions:**

1. **Implement the `validate` Function:**

   -  function should recursively compare the keys and data types in `data` against the `template`.
   - If the `data` matches the `template`, return `(True, '')`.
   - If there is a mismatch, return `(False, error_message)` as per the specifications.

2. **Error Handling:**

   - The function should stop at the **first error** encountered and return the appropriate error message.
   - The error message should accurately reflect whether it's a missing key or a bad data type, along with the correct `key_path`.

3. **Testing:**

   - A test file using `pytest` is provided below.
   - Ensure that your implementation passes all the tests when running `pytest`.


**Provided Test File (`test_validate.py`):**

```python
# test_validate.py

import pytest

# Import the student's validate function
from student_code import validate

# The template dictionary
template = {
    'user_id': int,
    'name': {
        'first': str,
        'last': str
    },
    'bio': {
        'dob': {
            'year': int,
            'month': int,
            'day': int
        },
        'birthplace': {
            'country': str,
            'city': str
        }
    }
}

def test_valid_data():
    john = {
        'user_id': 100,
        'name': {
            'first': 'John',
            'last': 'Cleese'
        },
        'bio': {
            'dob': {
                'year': 1939,
                'month': 11,
                'day': 27
            },
            'birthplace': {
                'country': 'United Kingdom',
                'city': 'Weston-super-Mare'
            }
        }
    }
    state, error = validate(john, template)
    assert state == True
    assert error == ''

def test_missing_key():
    eric = {
        'user_id': 101,
        'name': {
            'first': 'Eric',
            'last': 'Idle'
        },
        'bio': {
            'dob': {
                'year': 1943,
                'month': 3,
                'day': 29
            },
            'birthplace': {
                'country': 'United Kingdom'
            }
        }
    }
    state, error = validate(eric, template)
    assert state == False
    assert error == 'mismatched keys: bio.birthplace.city'

def test_bad_type():
    michael = {
        'user_id': 102,
        'name': {
            'first': 'Michael',
            'last': 'Palin'
        },
        'bio': {
            'dob': {
                'year': 1943,
                'month': 'May',  # Should be int
                'day': 5
            },
            'birthplace': {
                'country': 'United Kingdom',
                'city': 'Sheffield'
            }
        }
    }
    state, error = validate(michael, template)
    assert state == False
    assert error == 'bad type: bio.dob.month'

def test_extra_key():
    # Data with an extra key
    graham = {
        'user_id': 103,
        'name': {
            'first': 'Graham',
            'last': 'Chapman',
            'middle': 'Arthur'  # Extra key not in template
        },
        'bio': {
            'dob': {
                'year': 1941,
                'month': 1,
                'day': 8
            },
            'birthplace': {
                'country': 'United Kingdom',
                'city': 'Leicester'
            }
        }
    }
    state, error = validate(graham, template)
    assert state == False
    assert error == 'mismatched keys: name.middle'

def test_wrong_type_at_top_level():
    # Data where a top-level key has wrong type
    terry_j = {
        'user_id': '104',  # Should be int
        'name': {
            'first': 'Terry',
            'last': 'Jones'
        },
        'bio': {
            'dob': {
                'year': 1942,
                'month': 2,
                'day': 1
            },
            'birthplace': {
                'country': 'United Kingdom',
                'city': 'Colwyn Bay'
            }
        }
    }
    state, error = validate(terry_j, template)
    assert state == False
    assert error == 'bad type: user_id'

def test_missing_top_level_key():
    # Data missing a top-level key
    terry_g = {
        # 'user_id' is missing
        'name': {
            'first': 'Terry',
            'last': 'Gilliam'
        },
        'bio': {
            'dob': {
                'year': 1940,
                'month': 11,
                'day': 22
            },
            'birthplace': {
                'country': 'United States',
                'city': 'Minneapolis'
            }
        }
    }
    state, error = validate(terry_g, template)
    assert state == False
    assert error == 'mismatched keys: user_id'

def test_additional_nested_key():
    # Data with an additional nested key
    neil = {
        'user_id': 105,
        'name': {
            'first': 'Neil',
            'last': 'Innes'
        },
        'bio': {
            'dob': {
                'year': 1944,
                'month': 12,
                'day': 9
            },
            'birthplace': {
                'country': 'United Kingdom',
                'city': 'Danbury',
                'postcode': 'CM3'  # Extra key
            }
        }
    }
    state, error = validate(neil, template)
    assert state == False
    assert error == 'mismatched keys: bio.birthplace.postcode'

def test_empty_dictionary():
    # Empty data
    empty_data = {}
    state, error = validate(empty_data, template)
    assert state == False
    assert error == 'mismatched keys: user_id'

def test_none_value():
    # Data with None as value
    carol = {
        'user_id': 106,
        'name': {
            'first': 'Carol',
            'last': None  # Should be str
        },
        'bio': {
            'dob': {
                'year': 1942,
                'month': 8,
                'day': 24
            },
            'birthplace': {
                'country': 'United Kingdom',
                'city': 'Bedford'
            }
        }
    }
    state, error = validate(carol, template)
    assert state == False
    assert error == 'bad type: name.last'

def test_correct_types_but_extra_keys():
    # Correct types but extra keys
    connie = {
        'user_id': 107,
        'name': {
            'first': 'Connie',
            'last': 'Booth'
        },
        'bio': {
            'dob': {
                'year': 1940,
                'month': 1,
                'day': 31
            },
            'birthplace': {
                'country': 'United States',
                'city': 'Indianapolis'
            },
            'spouse': 'John Cleese'  # Extra key
        }
    }
    state, error = validate(connie, template)
    assert state == False
    assert error == 'mismatched keys: bio.spouse'

def test_wrong_type_in_nested_dict():
    # Wrong type in nested dictionary
    chapman = {
        'user_id': 108,
        'name': {
            'first': 'Chapman',
            'last': 'Brothers'
        },
        'bio': {
            'dob': {
                'year': 1962,
                'month': 9,
                'day': 14
            },
            'birthplace': {
                'country': 'United Kingdom',
                'city': ['Cheltenham']  # Should be str, not list
            }
        }
    }
    state, error = validate(chapman, template)
    assert state == False
    assert error == 'bad type: bio.birthplace.city'
```

