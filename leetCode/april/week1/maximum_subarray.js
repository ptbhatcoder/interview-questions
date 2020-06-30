/**
 * 
 * Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
 */

export const maxSubarray = (nums) => {
  let start,
    maxSum = -1,
    curSum,
    maxStart,
    maxEnd,
    hasPositive = false,
    maxVal = -Infinity,
    maxValIndex = -1;
  for (let i = 0; i < nums.length; i++) {
    const val = nums[i];
    if (val >= 0) {
      hasPositive = true;
    }

    if (maxVal < val) {
      maxVal = val;
      maxValIndex = i;
    }

    curSum += val;
    if (curSum < 0) {
      start = i;
      curSum = 0;
    }

    if (curSum > maxSum) {
      maxSum = curSum;
      maxStart = start;
      maxEnd = i;
    }
  }

  return {
    start: hasPositive ? maxStart : maxValIndex,
    end: hasPositive ? maxEnd : maxValIndex,
    sum: hasPositive ? maxSum : maxVal,
  };
};
