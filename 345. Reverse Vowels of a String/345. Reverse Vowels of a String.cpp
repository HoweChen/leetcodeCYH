class Solution {
public:
  string reverseVowels(string s) {
    queue<int> vowelPos;
    stack<char> vowelAfterReverse;

    // add position into the queue and the vowel to the stack
    // due to the FILO rule, the vowel string would be reversed after pop()
    for (int i = 0; i < int(s.length()); ++i) {
      if (s.at(i) == 'A' || s.at(i) == 'E' || s.at(i) == 'I' ||
          s.at(i) == 'O' || s.at(i) == 'U' || s.at(i) == 'a' ||
          s.at(i) == 'e' || s.at(i) == 'i' || s.at(i) == 'o' ||
          s.at(i) == 'u') {
        vowelPos.push(i);
        vowelAfterReverse.push(s.at(i));
      }
    }

    // change the char at the flag to the vowel, then pop() both queue and stack
    while (!vowelPos.empty()) {
      //        cout<<"test"<<endl;
      int flag = vowelPos.front();
      s[flag] = vowelAfterReverse.top();
      vowelPos.pop();
      vowelAfterReverse.pop();
    }
    return s;
  }
};

// complete code
// #include <iostream>
// #include <cstring>
// #include <vector>
// #include <queue>
// #include <stack>
//
// using namespace std;
//
// int main() {
//     queue<int> vowelPos;
//     stack<char> vowelAfterReverse;
//     string s = "Race Car";
//
//     //remember the position of vowel to the queue
//     for (int i = 0; i < int(s.length()); ++i) {
//         if (s.at(i) == 'A' || s.at(i) == 'E' || s.at(i) == 'I' || s.at(i) ==
//         'O' || s.at(i) == 'U'
//             || s.at(i) == 'a' || s.at(i) == 'e' || s.at(i) == 'i' || s.at(i)
//             == 'o' || s.at(i) == 'u') {
//             vowelPos.push(i);
//             vowelAfterReverse.push(s.at(i));
//         }
//     }
//
//     while(!vowelPos.empty()){
// //        cout<<"test"<<endl;
//         int flag = vowelPos.front();
//         s[flag] = vowelAfterReverse.top();
//         vowelPos.pop();
//         vowelAfterReverse.pop();
//     }
//     cout << s << endl;
//     return 0;
// }
