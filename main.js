function beeramid(bonus, price) {
  let totalPayed = 0;
  let i = 0;
  while (totalPayed <= bonus) {
    const bottlesInRow = i ** 2;
    const rowPrice = bottlesInRow * price;
    if (totalPayed + rowPrice > bonus) break;
    totalPayed += rowPrice;
    i++;
  }
  return i;
}

beeramid(9, 2);
