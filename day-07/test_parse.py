from parse import parse_rule


def test_parse_rule_parses_a_single_quantity_single_bag_rule():
    rule = "posh maroon bags contain 1 bright salmon bag."
    expected = {"bright salmon": (1, "posh maroon")}

    actual = parse_rule(rule)

    assert actual == expected


def test_parse_rule_parses_a_multiple_quantity_single_bag_rule():
    rule = "posh maroon bags contain 2 bright salmon bags."
    expected = {"bright salmon": (2, "posh maroon")}

    actual = parse_rule(rule)

    assert actual == expected


def test_parse_rule_parses_a_multiple_quantity_multiple_bag_rule():
    rule = "posh maroon bags contain 2 bright salmon bags, 5 drab blue bags."
    expected = {"bright salmon": (2, "posh maroon"), "drab blue": (5, "posh maroon")}

    actual = parse_rule(rule)

    assert actual == expected


def test_parse_rule_returns_none_for_no_contain_rule():
    rule = "posh maroon bags contain no other bags."

    actual = parse_rule(rule)

    assert actual is None
