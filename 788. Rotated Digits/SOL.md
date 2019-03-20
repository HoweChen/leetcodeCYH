# Rotated Digits (Leet Code 788)

![img](http://www.frankmadrid.com/ALudicFallacy/wp-content/uploads/2018/02/Rotation-768x257.png)

Posted on [February 28, 2018](http://www.frankmadrid.com/ALudicFallacy/2018/02/28/rotated-digits-leet-code-788/)by [That Math Guy](http://www.frankmadrid.com/ALudicFallacy/author/fmadrid/)

# Problem Statement

Given a positive number NN, how many numbers are good from 1 to NN where 1≤N≤100001≤N≤10000?

# Definitions

Good

A number is **good** if after rotating each digit individually by 180 degrees, we get a valid different number.

Valid

A number is **valid** if each digit remains a digit after rotation.

Rotation

0, 1, and 8 rotate to themselves; 2 and 5 rotate to each other; 6 and 9 rotate to each other, and the rest of the numbers do not rotate to any other number.

![img](https://i2.wp.com/www.frankmadrid.com/ALudicFallacy/wp-content/uploads/2018/02/Rotation.png?resize=640%2C214)**Figure 1:** A mapping of each digit to its rotation. Red digits do not rotate to any number and are thus invalid, green digits rotate to a new number and thus form a new number, while yellow digits rotate to the same number and leave the number unchanged.

For brevity, any number whose _rotation is a different number_ is a new number, any number whose _rotation is the same number_ is a same number, while any number whose _rotation is invalid_ is an invalid number.

# Summary

The problem is asking for the quantity of numbers in the range which exhibit the good property. A number is good if and only if:

- 1. After rotating each digit by 180 degrees, the number is still valid.

  The digits 3, 4, and 7 do not have valid rotations; thus, any number containing these digits are not good (i.e. contains only new numbers and same numbers).

- 2. The new number is different.

  Changing any digit generates a new number; thus, any good number must contain a 2, 5, 6, or 9 (i.e. contains a new number).

Thus, the problem reduces to finding such numbers which satisfy these two conditions.

### Solution #1 – Brute Force

The brute force solution iterates through each number from 11 to NN and checks each digit of the number to determine if the number satisfied conditions (1) and (2) above.

```cpp
  #include<iostream>
  #include<string>
  #include<cmath>

  // Returns true if a number is good; otherwise, returns false
  bool isGood(int n) {
      bool isNewNumber = false; // True if n contains a 2, 5, 6, or 9
      do {
          int digit = n % 10;  // Gets the least significant digit (i.e. one's place)
          switch(digit) {
              case 3:
              case 4:
              case 7: return false; // Digit is a 3, 4, or 7 (i.e. contains an invalid rotation)
                      break;
              case 2:
              case 5:
              case 6:
              case 9: isNewNumber = true; // Digit is a 2, 5, 6, or 9 (i.e. 'good' number)
                      break;
          }
          n /= 10;  // Shift decimal digits right 1
      } while(n != 0);

      return isNewNumber;
  }

  int main(int argc, char** argv) {
      const int N = std::atoi(argv[1]);
      int goodCount = 0;
      for(int i = 1; i <= N; i++)
          if(isGood(i))
              goodCount++;
      std::cout << "There are " << goodCount << " good number(s) between 1 and " << N << "./n";
      return 0;
  }
```

### Runtime Complexity

With a worst case time-complexity of O(n⋅logn)O(n⋅log⁡n), the algorithm is somewhat quick. But can we do better?

[**Example**](<javascript:toggle('LeetCode788Example1','titleText','LeetCode788Content1');>)

This solution performs many redundant digit comparisons. After determining if the numbers in the range of [1,9][1,9] are good, any comparisons performed on the second digit in the range [10,99][10,99] are redundant.

### Solution #2 - Dynamic Programming

For each digit xixi in NN, we can find all good numbers in the range [0,xi×10i)[0,xi×10i) in O(1)O(1) time by remembering if we have seen a new number.

Consider the following tree:

![img](https://i1.wp.com/www.frankmadrid.com/ALudicFallacy/wp-content/uploads/2018/02/image-10.png?zoom=2&resize=640%2C353)**Figure 2:** A decision tree representing 3 choices when choosing digits for a 3-digit number. The highlighted path represents 2727 valid numbers, yet not good numbers, consisting of the digits 00, 11, and 88. Note the options containing invalid digits are not considered.

From **Figure 2**, there are 7373 (seven choices for each of the three digits) or 343343 valid 3-digit numbers, ranging from 000000 to 999999; however one path, namely yellow-yellow-yellow (3333 valid numbers), do not result in a new number, since each good number must have at least one new number, leaving only 73−3373−33 or 316316 good numbers. If we have seen a good number, all 376376 valid numbers would have been good numbers.

We are generally not interested in finding every ll-digit good number, but rather, all good numbers less than or equal to some NN. **Figure 2** exemplifies how in constant time, we can find all 3-digit, 2-digit, and 1-digit good numbers in the range [0,1000)[0,1000). Thus if tasked with finding all good numbers less than or equal to 12341234, we can simply count the good numbers in the ranges [0,1000)[0,1000), [1000,1200)[1000,1200), [1200,1230)[1200,1230), [1230,1234)[1230,1234), and [1234][1234].

[**Example**](<javascript:toggle('LeetCode788Example2','titleText','LeetCode788Content2');>)

We can draw three ideas from the example:

- Idea 1: If there are mm digits remaining to be chosen, then there are (3+4)m(3+4)m possible valid numbers.

  Since we are never choosing invalid numbers, we will always have 77 valid numbers to choose from per digit.

- Idea #2: If a green number has been seen, each of the remaining (3+4)m(3+4)m possible valid numbers are good numbers; otherwise, 3m3mof those valid numbers are not good numbers and must be subtracted from the over estimation.

  If we have seen a new number, then by definition, the number is considered good since it is a valid number. If we have not seen a new number, one of the paths, namely the sole yellow-yellow-yellow path does not include any good numbers.

- Idea #3: The less significant digits do not affect the good numbers contained in the more significant digits.

  Consider the number 642642. We can break this apart into the three distinct regions [0,600)[0,600), [600,640)[600,640), [640,642)[640,642). The less significant digits 44 and 22 will have no effect on the amount of good numbers in the [0,600)[0,600) region.

The dynamic programming solution counts all valid numbers stemming from each digit, subtracting the same number branch if no new number has been encountered yet.

```cpp
  #include<iostream>
  #include<string>
  #include<cmath>
  // The following four arrays were defined to avoid long compound boolean expressions:
  // 'if(digit == 2 || digit == 5 || digit == 6 || digit == 9) { ... }'
  // which instead keeps track of such information cumulatively. For example,
  // differentRotation[7] = 3 means 3 numbers in the range of [0,7] are new numbers, namely,
  // the new numbers post-rotation 2,5, and 6.

  // Digits:                    0 1 2 3 4 5 6 7 8 9
  int type[10]               = {0,0,1,2,2,1,1,2,0,1};  // 'Same' 'New' or 'Invalid' numbers
  int differentRotations[10] = {0,0,1,1,1,2,3,3,3,4};  // Cumulative: New number
  int validRotations[10]     = {1,2,3,3,3,4,5,5,6,7};  // Cumulative: Valid number
  int sameRotations[10]      = {1,2,2,2,2,2,2,2,3,3};  // Cumulative: Same number

  // Counts the good numbers in the range of [000..0, X00..0] where str[0] = X. Implements
  // dynamic programming to indicate if a new number has been seen.
  int countRotations(std::string str, bool isNewNumber) {

      int digit = str[0] - '0';  // Converts char to int (see ASCII Table mathematics)
      if(str.length() == 1) return isNewNumber ? validRotations[digit] : differentRotations[digit];

      int ret = 0;
      if(digit != 0) {

          // Get all valid numbers (Idea #1)
          ret += validRotations[digit-1] * std::pow(7,str.length() - 1);

          // If a new number has not been seen, subtract all non-good number paths (Idea #2)
          if(!isNewNumber) ret -= sameRotations[digit-1] * std::pow(3, str.length() - 1);
      }

      if(type[digit] == 1) isNewNumber = true;

      // If the digit is valid, then recursively call function on remaining n-1 numbers
      if(type[digit] != 2) ret += countRotations(str.substr(1, std::string::npos), isNewNumber);

      return ret;
  }

  // Converts N into a string where the most significant bit is at index 0
  int rotatedDigits(int N) { return countRotations(std::to_string(N), false); }

  int main(int argc, char** argv) {
      int N = std::atoi(argv[1]);
      std::cout << "There are " << rotatedDigits(N) << " good numbers between 1 and " << N << ".\n";
      return 0;
  }
```

### Runtime Complexity

Since the recursive function is called at most once per each digit and the amount of work done in each function call is constant, this solution has a worst case time-complexity of O(logn)O(log⁡n).
