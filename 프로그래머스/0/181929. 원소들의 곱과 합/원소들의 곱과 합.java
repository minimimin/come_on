class Solution {
    public int solution(int[] num_list) {
        int multi = 1;
        int plus = 0;
        
        for(int i=0; i < num_list.length; i++){
            multi *= num_list[i];
            plus += num_list[i];
        }

        return (multi < (plus*plus)) ? 1: 0;
    }
}