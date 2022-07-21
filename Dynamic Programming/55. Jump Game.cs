public class MemoizationSolution {
    private bool dfs(int curr_index, int[] nums,
                     int last_index, IDictionary<int, bool> memo){
        if(memo.ContainsKey(curr_index))
        {
            return memo[curr_index];
        }
        if(curr_index == last_index)
        {
            return true;
        }
        int furthest_jump = Math.Min(nums[curr_index],
                                     last_index-curr_index);
        for(int i=1;i<=furthest_jump;i++)
        {
            bool res = dfs(curr_index+i, nums, last_index, memo);
            if(res)
            {
                memo.Add(curr_index, true);
                return true;
            }
        }
        memo.Add(curr_index, false);
        return false;
    }
    public bool CanJump(int[] nums) {
        int last_index = nums.Length - 1;
        IDictionary<int, bool> memo = new Dictionary<int, bool>();
        return dfs(0, nums, last_index, memo);

    }
}