class Solution {
    public int solution(String myString, String pat) {
        String string = myString.toLowerCase();
        String findWord = pat.toLowerCase();
        // return (string.contains(findWord)) ? 1 : 0;
        return (string.indexOf(findWord) == -1) ? 0 : 1;
    }
}