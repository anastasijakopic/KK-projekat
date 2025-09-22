void main() {
    var numbers = [1, 2, 3, 4, 5];
    var sum = 0;
    
    for (var i = 0; i < 5; i++) {
        if (numbers[i] % 2 == 0) {
            sum = sum + numbers[i];
        }
    }
    
    print(sum);
}