#!/usr/bin/python
# -*- coding:utf-8 -*-

'''
217.存在重复元素
给定一个整数数组，判断是否存在重复元素。

如果任何值在数组中出现至少两次，函数返回 true。如果数组中每个元素都不相同，则返回 false。

示例 1:

输入: [1,2,3,1]
输出: true
示例 2:

输入: [1,2,3,4]
输出: false
示例 3:

输入: [1,1,1,3,3,4,3,2,4,2]
输出: true
'''

class Solution:

    # 排序后前后两位数相同则为True反之为False
    def containsDuplicate(self, nums):
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1]:
                return True
            else:
                continue
        return False


if __name__ == "__main__":

    S = Solution()

    S.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2])
