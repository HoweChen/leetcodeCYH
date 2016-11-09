class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        size_t pos = 0;
        for(size_t i = 0; i< ransomNote.size();++i){
            size_t pos = magazine.find(ransomNote[i], 0);
            if(pos != std::string::npos){
                magazine.erase(pos,1);
            } else {
                return false;
            }
        }
        return true;
    }
};
