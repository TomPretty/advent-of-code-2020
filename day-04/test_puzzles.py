from puzzles import (
    is_valid_byr,
    is_valid_ecl,
    is_valid_eyr,
    is_valid_hcl,
    is_valid_hgt,
    is_valid_iyr,
    is_valid_pid,
)


def test_byr_is_required():
    assert is_valid_byr({}) is False
    assert is_valid_byr({"byr": "1920"}) is True


def test_byr_must_be_4_digits():
    assert is_valid_byr({"byr": "192"}) is False
    assert is_valid_byr({"byr": "1920"}) is True
    assert is_valid_byr({"byr": "19200"}) is False


def test_byr_must_be_between_1920_and_2002():
    assert is_valid_byr({"byr": "1919"}) is False
    assert is_valid_byr({"byr": "1950"}) is True
    assert is_valid_byr({"byr": "2003"}) is False


def test_iyr_is_required():
    assert is_valid_iyr({}) is False
    assert is_valid_iyr({"iyr": "2015"}) is True


def test_iyr_must_be_4_digits():
    assert is_valid_iyr({"iyr": "201"}) is False
    assert is_valid_iyr({"iyr": "2015"}) is True
    assert is_valid_iyr({"iyr": "20150"}) is False


def test_iyr_must_be_between_2010_and_2020():
    assert is_valid_iyr({"iyr": "2009"}) is False
    assert is_valid_iyr({"iyr": "2015"}) is True
    assert is_valid_iyr({"iyr": "2021"}) is False


def test_eyr_is_required():
    assert is_valid_eyr({}) is False
    assert is_valid_eyr({"eyr": "2025"}) is True


def test_eyr_must_be_4_digits():
    assert is_valid_eyr({"eyr": "202"}) is False
    assert is_valid_eyr({"eyr": "2025"}) is True
    assert is_valid_eyr({"eyr": "20250"}) is False


def test_eyr_must_be_between_2020_and_2030():
    assert is_valid_eyr({"eyr": "2019"}) is False
    assert is_valid_eyr({"eyr": "2025"}) is True
    assert is_valid_eyr({"eyr": "2031"}) is False


def test_hgt_is_required():
    assert is_valid_hgt({}) is False
    assert is_valid_hgt({"hgt": "180cm"}) is True


def test_hgt_must_have_height_and_units():
    assert is_valid_hgt({"hgt": "180"}) is False
    assert is_valid_hgt({"hgt": "cm"}) is False
    assert is_valid_hgt({"hgt": "180cm"}) is True


def test_hgt_must_be_in_cm_or_in():
    assert is_valid_hgt({"hgt": "6ft"}) is False
    assert is_valid_hgt({"hgt": "180cm"}) is True
    assert is_valid_hgt({"hgt": "60in"}) is True


def test_hgt_in_cm_must_be_between_150_and_193():
    assert is_valid_hgt({"hgt": "149cm"}) is False
    assert is_valid_hgt({"hgt": "180cm"}) is True
    assert is_valid_hgt({"hgt": "194cm"}) is False


def test_hgt_in_in_must_be_between_59_and_76():
    assert is_valid_hgt({"hgt": "58in"}) is False
    assert is_valid_hgt({"hgt": "60in"}) is True
    assert is_valid_hgt({"hgt": "77in"}) is False


def test_hcl_is_required():
    assert is_valid_hcl({}) is False
    assert is_valid_hcl({"hcl": "#ffffff"}) is True


def test_hcl_must_be_a_hex_value():
    assert is_valid_hcl({"hcl": "ffffff"}) is False
    assert is_valid_hcl({"hcl": "#ffffff"}) is True
    assert is_valid_hcl({"hcl": "#gggggg"}) is False
    assert is_valid_hcl({"hcl": "#555555"}) is True
    assert is_valid_hcl({"hcl": "#5555555"}) is False


def test_ecl_is_required():
    assert is_valid_ecl({}) is False
    assert is_valid_ecl({"ecl": "amb"}) is True


def test_ecl_must_be_in_accepted_values():
    assert is_valid_ecl({"ecl": "blk"}) is False
    for ecl in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        assert is_valid_ecl({"ecl": ecl}) is True


def test_pid_is_required():
    assert is_valid_pid({}) is False
    assert is_valid_pid({"pid": "000000000"}) is True


def test_pid_must_only_contain_digits():
    assert is_valid_pid({"pid": "aaaaaaaaa"}) is False
    assert is_valid_pid({"pid": "000000000"}) is True


def test_pid_must_be_9_digits():
    assert is_valid_pid({"pid": "00000000"}) is False
    assert is_valid_pid({"pid": "000000000"}) is True
    assert is_valid_pid({"pid": "0000000000"}) is False
