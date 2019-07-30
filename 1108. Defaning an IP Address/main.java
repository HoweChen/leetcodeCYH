class Solution {
    public String defangIPaddr(String address) {
        StringBuilder strBuilder = new StringBuilder();
        for(char character:address.toCharArray()){
            if (character=='.'){
                strBuilder.append("[.]");
            }
            else{
                strBuilder.append(character);
            }
        }
        return strBuilder.toString();
    }
}