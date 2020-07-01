/**
 * Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
The input is to be sorted in place hence do not return anything
 */

/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
export const moveZeroesToRight = (nums) => {
  for (let lastSwapped = -1, i = 0; i < nums.length; i++) {
    if (nums[i]) {
      lastSwapped++;
      [nums[i], nums[lastSwapped]] = [nums[lastSwapped], nums[i]];
    }
  }
};

/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
export const moveZeroesToLeft = (nums) => {
  for (let lastSwapped = nums.length, i = nums.length - 1; i >= 0; i--) {
    if (nums[i]) {
      lastSwapped--;
      [nums[i], nums[lastSwapped]] = [nums[lastSwapped], nums[i]];
    }
  }
};

/**
 * Time compexity = O(n)
 * Space Complexity = O(1)
 */
