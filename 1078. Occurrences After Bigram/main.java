class Solution {
    public String[] findOcurrences(String text, String first, String second) {
        String[] str_list = text.split(" ");
        int i=0;
        ArrayList<String> result = new ArrayList<String>();
        while (i<str_list.length-2){
            if (str_list[i].equals(first) && str_list[i+1].equals(second)){
                result.add(str_list[i+2]);
                i+=2;
            } else {
                i+=1;
            }
            
        }
        return result.toArray(new String[result.size()]);
    }
}