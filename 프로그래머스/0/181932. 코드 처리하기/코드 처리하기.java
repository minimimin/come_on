class Solution {
    public String solution(String code) {
        StringBuilder ret = new StringBuilder();
        int mode = 0;
        
        for(int idx = 0;idx < code.length(); idx++){
            char nowChar = code.charAt(idx);
            if (nowChar == '1'){
                mode = (mode == 1) ? 0 : 1;
                continue;
            }
            if (idx % 2 == mode){ret.append(nowChar);}
        }
        return (ret.length() == 0) ? "EMPTY" : ret.toString();
    }
}