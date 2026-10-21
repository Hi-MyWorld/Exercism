# These tests are auto-generated with test data from:
# https://github.com/exercism/problem-specifications/tree/main/exercises/square-root/canonical-data.json
# File last updated on 2023-07-19
# Extended with LARGE PERFECT SQUARES only

import unittest

from square_root import (
    square_root,
)


class SquareRootPerfectSquaresTest(unittest.TestCase):
    # ---------- مربع‌های کامل پایه ----------
    def test_root_of_1(self):
        self.assertEqual(square_root(1), 1)

    def test_root_of_4(self):
        self.assertEqual(square_root(4), 2)

    def test_root_of_25(self):
        self.assertEqual(square_root(25), 5)

    def test_root_of_81(self):
        self.assertEqual(square_root(81), 9)

    def test_root_of_196(self):
        self.assertEqual(square_root(196), 14)

    def test_root_of_65025(self):
        self.assertEqual(square_root(65025), 255)

    # ---------- مربع‌های کامل چهار رقمی ----------
    def test_root_of_1024(self):
        """1024 = 32²"""
        self.assertEqual(square_root(1024), 32)

    def test_root_of_2401(self):
        """2401 = 49²"""
        self.assertEqual(square_root(2401), 49)

    def test_root_of_4096(self):
        """4096 = 64²"""
        self.assertEqual(square_root(4096), 64)

    def test_root_of_6561(self):
        """6561 = 81²"""
        self.assertEqual(square_root(6561), 81)

    def test_root_of_9801(self):
        """9801 = 99²"""
        self.assertEqual(square_root(9801), 99)

    # ---------- مربع‌های کامل پنج رقمی ----------
    def test_root_of_10000(self):
        """10000 = 100²"""
        self.assertEqual(square_root(10000), 100)

    def test_root_of_12321(self):
        """12321 = 111²"""
        self.assertEqual(square_root(12321), 111)

    def test_root_of_22201(self):
        """22201 = 149²"""
        self.assertEqual(square_root(22201), 149)

    def test_root_of_50625(self):
        """50625 = 225²"""
        self.assertEqual(square_root(50625), 225)

    def test_root_of_99856(self):
        """99856 = 316²"""
        self.assertEqual(square_root(99856), 316)

    # ---------- مربع‌های کامل شش رقمی ----------
    def test_root_of_1000000(self):
        """1,000,000 = 1000²"""
        self.assertEqual(square_root(1000000), 1000)

    def test_root_of_1234321(self):
        """1,234,321 = 1111²"""
        self.assertEqual(square_root(1234321), 1111)

    def test_root_of_998001(self):
        """998001 = 999²"""
        self.assertEqual(square_root(998001), 999)

    # ---------- مربع‌های کامل هفت رقمی ----------
    def test_root_of_10000000_plus(self):
        """10,000,000 = 3162² + ... نیست؛ اما 10,046,004 = 3168²"""
        self.assertEqual(square_root(10046004), 3168)

    def test_root_of_49999041(self):
        """49,999,041 = 7071²"""
        self.assertEqual(square_root(49999041), 7071)

    # ---------- مربع‌های کامل هشت رقمی ----------
    def test_root_of_100000000(self):
        """10⁸ = 10000²"""
        self.assertEqual(square_root(100000000), 10000)

    def test_root_of_12345678_squared(self):
        """12345678² = 152415765279684 — نه، 8 رقمی نیست.
        اما 12345² = 152,399,025 (9 رقمی)؛
        در اینجا 9999² = 99,980,001 (8 رقمی)"""
        self.assertEqual(square_root(99980001), 9999)

    # ---------- مربع‌های کامل نه رقمی ----------
    def test_root_of_123454321(self):
        """123,454,321 = 11111²"""
        self.assertEqual(square_root(123454321), 11111)

    def test_root_of_998001000_plus(self):
        """نیاز به بررسی؛ 31623² = 1,000,014,129 (10 رقمی).
        اما 99999² = 9,999,800,001 (10 رقمی)"""
        # در ادامه می‌آید
        pass

    def test_root_of_152399025(self):
        """152,399,025 = 12345²"""
        self.assertEqual(square_root(152399025), 12345)

    # ---------- مربع‌های کامل ده رقمی ----------
    def test_root_of_10000000000(self):
        """10¹⁰ = 100000²"""
        self.assertEqual(square_root(10**10), 100000)

    def test_root_of_9999800001(self):
        """9,999,800,001 = 99999²"""
        self.assertEqual(square_root(9999800001), 99999)

    def test_root_of_4294836225(self):
        """4,294,836,225 = 65535²"""
        self.assertEqual(square_root(4294836225), 65535)

    # ---------- مربع‌های کامل یازده رقمی ----------
    def test_root_of_1234567654321(self):
        """1,234,567,654,321 = 1111111²"""
        self.assertEqual(square_root(1234567654321), 1111111)

    # ---------- مربع‌های کامل دوازده رقمی ----------
    def test_root_of_10_power_12(self):
        """10¹² = 1,000,000²"""
        self.assertEqual(square_root(10**12), 1000000)

    def test_root_of_999999_squared(self):
        """999,999² = 999,998,000,001"""
        self.assertEqual(square_root(999998000001), 999999)

    # ---------- مربع‌های کامل سیزده رقمی ----------
    def test_root_of_12345654321_squared(self):
        """1111111² = 1,234,567,654,321 (قبلاً تست شد)
        اما 3,162,277² = 9,999,996,??? — بهتر است از 11111111² استفاده کنیم"""
        pass

    def test_root_of_11111111_squared(self):
        """11,111,111² = 123,456,787,654,321 (15 رقمی — در ادامه)"""
        pass

    # ---------- مربع‌های کامل ۱۵ رقمی ----------
    def test_root_of_11111111_squared(self):
        """11,111,111² = 123,456,787,654,321"""
        self.assertEqual(square_root(123456787654321), 11111111)

    # ---------- مربع‌های کامل ۱۶ رقمی ----------
    def test_root_of_10_power_16(self):
        """10¹⁶ = 100,000,000²"""
        self.assertEqual(square_root(10**16), 100000000)

    def test_root_of_4294967296(self):
        """4,294,967,296 = 65536² = 2³²"""
        self.assertEqual(square_root(4294967296), 65536)

    def test_root_of_99999999_squared(self):
        """99,999,999² = 9,999,999,800,000,001"""
        self.assertEqual(square_root(9999999800000001), 99999999)

    # ---------- مربع‌های کامل ۱۸ رقمی ----------
    def test_root_of_10_power_18(self):
        """10¹⁸ = 1,000,000,000²"""
        self.assertEqual(square_root(10**18), 1000000000)

    def test_root_of_123456789_squared(self):
        """123,456,789² = 15,241,578,750,190,521"""
        self.assertEqual(square_root(15241578750190521), 123456789)

    def test_root_of_999999999_squared(self):
        """999,999,999² = 999,999,998,000,000,001"""
        self.assertEqual(square_root(999999998000000001), 999999999)

    # ---------- مربع‌های کامل ۲۰ رقمی ----------
    def test_root_of_10_power_20(self):
        """10²⁰ = 10,000,000,000²"""
        self.assertEqual(square_root(10**20), 10000000000)

    def test_root_of_1234567890_squared(self):
        """1,234,567,890² = 1,524,157,875,019,052,100"""
        self.assertEqual(square_root(1524157875019052100), 1234567890)

    # ---------- مربع‌های کامل ۲۴ رقمی ----------
    def test_root_of_10_power_24(self):
        """10²⁴ = 1,000,000,000,000²"""
        self.assertEqual(square_root(10**24), 10**12)

    # ---------- مربع‌های کامل ۳۰ رقمی ----------
    def test_root_of_10_power_30(self):
        """10³⁰ = 10¹⁵² — عدد بسیار بزرگ"""
        self.assertEqual(square_root(10**30), 10**15)

    # ---------- مربع‌های کامل ۵۰ رقمی ----------
    def test_root_of_10_power_50(self):
        """10⁵⁰ = (10²⁵)²"""
        self.assertEqual(square_root(10**50), 10**25)

    # ---------- مربع‌های کامل ۱۰۰ رقمی ----------
    def test_root_of_10_power_100(self):
        """10¹⁰⁰ = (10⁵⁰)²"""
        self.assertEqual(square_root(10**100), 10**50)

    # ---------- مربع اعداد خاص ----------
    def test_root_of_two_power_64(self):
        """2⁶⁴ = (2³²)² = 18,446,744,073,709,551,616"""
        self.assertEqual(square_root(2**64), 2**32)

    def test_root_of_two_power_100(self):
        """2¹⁰⁰ = (2⁵⁰)²"""
        self.assertEqual(square_root(2**100), 2**50)

    def test_root_of_two_power_128(self):
        """2¹²⁸ = (2⁶⁴)²"""
        self.assertEqual(square_root(2**128), 2**64)

    def test_root_of_two_power_200(self):
        """2²⁰⁰ = (2¹⁰⁰)²"""
        self.assertEqual(square_root(2**200), 2**100)

    def test_root_of_three_power_100(self):
        """3¹⁰⁰ = (3⁵⁰)²"""
        self.assertEqual(square_root(3**100), 3**50)

    def test_root_of_factorial_like(self):
        """(10!)² = 3,628,800² = 13,168,189,440,000"""
        self.assertEqual(square_root(13168189440000), 3628800)

    # ---------- مربع اعداد متوالی (الگو) ----------
    def test_root_of_1001_squared(self):
        """1001² = 1,002,001"""
        self.assertEqual(square_root(1002001), 1001)

    def test_root_of_9999_squared(self):
        """9999² = 99,980,001"""
        self.assertEqual(square_root(99980001), 9999)

    def test_root_of_100001_squared(self):
        """100,001² = 10,000,200,001"""
        self.assertEqual(square_root(10000200001), 100001)

    # ---------- مربع اعداد پالیندروم ----------
    def test_root_of_12321(self):
        """12321 = 111² (پالیندروم)"""
        self.assertEqual(square_root(12321), 111)

    def test_root_of_1234321(self):
        """1,234,321 = 1111² (پالیندروم)"""
        self.assertEqual(square_root(1234321), 1111)

    def test_root_of_123454321(self):
        """123,454,321 = 11111² (پالیندروم)"""
        self.assertEqual(square_root(123454321), 11111)

    def test_root_of_1234567654321(self):
        """1,234,567,654,321 = 1,111,111² (پالیندروم)"""
        self.assertEqual(square_root(1234567654321), 1111111)

    def test_root_of_123456787654321(self):
        """123,456,787,654,321 = 11,111,111² (پالیندروم)"""
        self.assertEqual(square_root(123456787654321), 11111111)

    # ---------- مربع اعداد با الگوی خاص ----------
    def test_root_of_66666_squared(self):
        """66,666² = 4,444,355,556"""
        self.assertEqual(square_root(4444355556), 66666)

    def test_root_of_99999_squared(self):
        """99,999² = 9,999,800,001"""
        self.assertEqual(square_root(9999800001), 99999)

    def test_root_of_1000001_squared(self):
        """1,000,001² = 1,000,002,000,001"""
        self.assertEqual(square_root(1000002000001), 1000001)


if __name__ == "__main__":
    unittest.main()
