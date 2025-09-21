void test(int x) {
  try {
    if (x < 0) {
      throw Exception("Negativan broj");
    }
    print("Sve je u redu");
  } catch (e) {
    print("Greška: ${e.toString()}");
  } finally {
    print("Ovo se uvek izvršava");
  }
}
