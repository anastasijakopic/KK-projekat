void test(int x) {
  switch (x) {
    case 1:
      throw Exception("Greška");
    case 2:
      return;
    default:
      return;
  }

  while (true) {
    if (x > 5) {
      break;
    } else {
      continue;
    }
  }
}
