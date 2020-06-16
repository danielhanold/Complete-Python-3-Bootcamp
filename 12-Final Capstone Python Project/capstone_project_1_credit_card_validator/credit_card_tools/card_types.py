"""
Defines credit card types, patterns, names etc.
Based on https://github.com/braintree/credit-card-type/blob/master/README.md.

Each card type has a patterns attribute that is an array of numbers and
ranges of numbers (represented by an array of 2 values, a min and a max).
"""

from functools import reduce

card_types = {
    "visa": {
        "niceType": 'Visa',
        "type": 'visa',
        "patterns": [
            4
        ],
        "gaps": [4, 8, 12],
        "lengths": [16, 18, 19],
        "code": {
            "name": 'CVV',
            "size": 3
        }
    },
    "mastercard": {
        "niceType": 'Mastercard',
        "type": 'mastercard',
        "patterns": [
            [51, 55],
            [2221, 2229],
            [223, 229],
            [23, 26],
            [270, 271],
            2720
        ],
        "gaps": [4, 8, 12],
        "lengths": [16],
        "code": {
            "name": 'CVC',
            "size": 3
        }
    },
    'american-express': {
        "niceType": 'American Express',
        "type": 'american-express',
        "patterns": [
            34,
            37
        ],
        "gaps": [4, 10],
        "lengths": [15],
        "code": {
            "name": 'CID',
            "size": 4
        }
    },
    'diners-club': {
        "niceType": 'Diners Club',
        "type": 'diners-club',
        "patterns": [
            [300, 305],
            36,
            38,
            39
        ],
        "gaps": [4, 10],
        "lengths": [14, 16, 19],
        "code": {
            "name": 'CVV',
            "size": 3
        }
    },
    "discover": {
        "niceType": 'Discover',
        "type": 'discover',
        "patterns": [
            6011,
            [644, 649],
            65
        ],
        "gaps": [4, 8, 12],
        "lengths": [16, 19],
        "code": {
            "name": 'CID',
            "size": 3
        }
    },
    "jcb": {
        "niceType": 'JCB',
        "type": 'jcb',
        "patterns": [
            2131,
            1800,
            [3528, 3589]
        ],
        "gaps": [4, 8, 12],
        "lengths": [16, 17, 18, 19],
        "code": {
            "name": 'CVV',
            "size": 3
        }
    },
    "unionpay": {
        "niceType": 'UnionPay',
        "type": 'unionpay',
        "patterns": [
            620,
            [624, 626],
            [62100, 62182],
            [62184, 62187],
            [62185, 62197],
            [62200, 62205],
            [622010, 622999],
            622018,
            [622019, 622999],
            [62207, 62209],
            [622126, 622925],
            [623, 626],
            6270,
            6272,
            6276,
            [627700, 627779],
            [627781, 627799],
            [6282, 6289],
            6291,
            6292,
            810,
            [8110, 8131],
            [8132, 8151],
            [8152, 8163],
            [8164, 8171]
        ],
        "gaps": [4, 8, 12],
        "lengths": [14, 15, 16, 17, 18, 19],
        "code": {
            "name": 'CVN',
            "size": 3
        }
    },
    "maestro": {
        "niceType": 'Maestro',
        "type": 'maestro',
        "patterns": [
            493698,
            [500000, 506698],
            [506779, 508999],
            [56, 59],
            63,
            67,
            6
        ],
        "gaps": [4, 8, 12],
        "lengths": [12, 13, 14, 15, 16, 17, 18, 19],
        "code": {
            "name": 'CVC',
            "size": 3
        }
    },
    "elo": {
        "niceType": 'Elo',
        "type": 'elo',
        "patterns": [
            401178,
            401179,
            438935,
            457631,
            457632,
            431274,
            451416,
            457393,
            504175,
            [506699, 506778],
            [509000, 509999],
            627780,
            636297,
            636368,
            [650031, 650033],
            [650035, 650051],
            [650405, 650439],
            [650485, 650538],
            [650541, 650598],
            [650700, 650718],
            [650720, 650727],
            [650901, 650978],
            [651652, 651679],
            [655000, 655019],
            [655021, 655058]
        ],
        "gaps": [4, 8, 12],
        "lengths": [16],
        "code": {
            "name": 'CVE',
            "size": 3
        }
    },
    "mir": {
        "niceType": 'Mir',
        "type": 'mir',
        "patterns": [
            [2200, 2204]
        ],
        "gaps": [4, 8, 12],
        "lengths": [16, 17, 18, 19],
        "code": {
            "name": 'CVP2',
            "size": 3
        }
    },
    "hiper": {
        "niceType": 'Hiper',
        "type": 'hiper',
        "patterns": [
            637095,
            637568,
            637599,
            637609,
            637612
        ],
        "gaps": [4, 8, 12],
        "lengths": [16],
        "code": {
            "name": 'CVC',
            "size": 3
        }
    },
    "hipercard": {
        "niceType": 'Hipercard',
        "type": 'hipercard',
        "patterns": [
            606282
        ],
        "gaps": [4, 8, 12],
        "lengths": [16],
        "code": {
            "name": 'CVC',
            "size": 3
        }
    }
}

def get_length_boundaries(end='upper'):
    """
    Determine the shortest and longest possible number of integers
    for any supported credit card number.
    """
    card_lengths_aggregate = [card['lengths'] for card in card_types.values()]

    # Create a singular list of lengths.
    card_lengths = []
    for lengths in card_lengths_aggregate:
        for length in lengths:
            card_lengths.append(length)

    # Return lower or upper limit.
    if end == 'lower':
        return min(card_lengths)
    else:
        return max(card_lengths)

def get_type(number):
    """
    Determine the card type based on a credit card number.

    Follows logic from https://github.com/braintree/credit-card-type/blob/master/README.md#pattern-detection
    """
    # Cast credit card number as a string.
    num_string = str(number)

    # Find all cards that match by pattern.
    matching_types = []
    for card_type, card_details in card_types.items():
        for pattern in card_details['patterns']:
            # Account for individual numbers and number ranges.
            try:
                num_range = range(pattern[0], pattern[1] + 1)
            except:
                num_range = range(pattern, pattern + 1)

            for num in num_range:
                if num_string.startswith(str(num)):
                    matching_types.append((card_type, num))

    # Determine best match out of all matches.
    best_match = reduce(lambda x, y: x if (x[1] > y[1]) else y, matching_types)

    # Return the matching type.
    return card_types[best_match[0]]

# Always determine lower and upper boundary.
min_number = get_length_boundaries('lower')
max_number = get_length_boundaries('upper')
