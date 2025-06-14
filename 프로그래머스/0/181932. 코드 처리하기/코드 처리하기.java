class Solution {
    public String solution(String code) {
        String ret = "";
        int mode = 0;
        int codeLen = code.length();
        
        for(int idx = 0;idx < codeLen; idx++){
            char codeIndex = code.charAt(idx);
            if (codeIndex == '1'){
                mode = (mode == 1) ? 0 : 1;
                continue;
            }
            ret = (idx%2 == mode) ? ret+codeIndex : ret;
        }
        return (ret == "")? "EMPTY" : ret;
    }
}