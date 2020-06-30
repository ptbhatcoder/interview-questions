/**
 * 

Write an algorithm to determine if a number n is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Return True if n is a happy number, and False if not.

Example: 

Input: 19
Output: true
Explanation: 
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
 */

 export const isHappy = num => {
     const transform = val => {
         let p = 0;
         while(val){
             digit = val%10;
             p += digit*digit;
             val = Math.floor(val/10);
         }
         return p;
     }

     let hare = num;
     let tortoise = num;
     do {
         hare = transform(transform(hare));
         tortoise = transform(tortoise);
     } while (hare !== tortoise);

     hare = num;
     do {
         hare = transform(hare);
         tortoise = transform(tortoise);
     } while(hare !== tortoise);

     return hare === 1;
 }

 /**
  * Time complexity : O(number of steps to make num coverge to a value)
  * Space complexity: O(1)
  */