while left < right:                total = nums[i] + nums[left] + nums[right]                if abs(total - target) < abs(closest - target):                    closest = total                if total < target:                    left += 1                elif total > target:                    right -= 1                else:                    return total        return closest

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if abs(total - target) < abs(closest - target):
                    closest = total

                if total < target:
                    left += 1
                elif total > target:
                    right -= 1
                else:
                    return total

        return closest