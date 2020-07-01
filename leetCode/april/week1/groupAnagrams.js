/**
 
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
 */

const primes = [
  2,
  3,
  5,
  7,
  11,
  13,
  17,
  19,
  23,
  29,
  31,
  37,
  41,
  43,
  47,
  53,
  59,
  61,
  67,
  71,
  73,
  79,
  83,
  89,
  97,
  101,
];

/**
 * @param {string[]} strs
 * @return {string[][]}
 */
export const groupAnagrams = (strs) =>
  Object.values(
    strs.reduce((map, str) => {
      const hash = [...str].reduce(
        (p, c, i) => p * primes[str.charCodeAt(i) - "a".charCodeAt(0)],
        1
      );
      map[hash] = map[hash] || [];
      map[hash].push(str);
      return map;
    }, {})
  );
