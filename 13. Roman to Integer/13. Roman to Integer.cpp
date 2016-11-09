class Solution {
public:
    int romanToInt(string s) {
        map<char, int> T = {{'I', 1},
                            {'V', 5},
                            {'X', 10},
                            {'L', 50},
                            {'C', 100},
                            {'D', 500},
                            {'M', 1000}
        };

        int result = T[s.back()];
        for(int i = s.length()-2;i>=0;--i){
            if(T[s[i]]<T[s[i+1]]){
                result = result - T[s[i]];
            } else {
                result = result + T[s[i]];
            }
        }
        return result;
    }
};
