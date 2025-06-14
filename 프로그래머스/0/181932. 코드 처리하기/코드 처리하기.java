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
            if (mode == 0){
                ret = (idx%2 == 0)? ret+codeIndex : ret;
            }else{
                ret = (idx%2 == 0)? ret : ret + codeIndex;
            }
        }
        return (ret == "")? "EMPTY" : ret;
    }
}