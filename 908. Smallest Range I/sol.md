#### Approach 1: Mathematical

**Intuition and Algorithm**

Let `A` be the original array, and `B` be the array after all our modifications. Towards trying to minimize `max(B) - min(B)`, let's try to minimize `max(B)`and maximize `min(B)` separately.

The smallest possible value of `max(B)` is `max(A) - K`, as the value `max(A)`cannot go lower. Similarly, the largest possible value of `min(B)` is `min(A) + K`. So the quantity `max(B) - min(B)` is at least `ans = (max(A) - K) - (min(A) + K)`.

We can attain this value (if `ans >= 0`), by the following modifications:

- If A[i] \leq \min(A) + K*A*[*i*]≤min(_A_)+_K_, then B[i] = \min(A) + K*B*[*i*]=min(_A_)+_K_
- Else, if A[i] \geq \max(A) - K*A*[*i*]≥max(_A_)−*K*, then B[i] = \max(A) - K*B*[*i*]=max(_A_)−*K*
- Else, B[i] = A[i]_B_[*i*]=_A_[*i*].

If `ans < 0`, the best answer we could have is `ans = 0`, also using the same modification.

<iframe src="https://leetcode.com/playground/hn3nSh7u/shared" frameborder="0" width="100%" height="225" name="hn3nSh7u" style="box-sizing: border-box; margin: 20px 0px; color: rgba(0, 0, 0, 0.65); font-family: -apple-system, system-ui, &quot;Segoe UI&quot;, &quot;PingFang SC&quot;, &quot;Hiragino Sans GB&quot;, &quot;Microsoft YaHei&quot;, &quot;Helvetica Neue&quot;, Helvetica, Arial, sans-serif, &quot;Apple Color Emoji&quot;, &quot;Segoe UI Emoji&quot;, &quot;Segoe UI Symbol&quot;; font-size: 14px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-style: initial; text-decoration-color: initial;"></iframe>

**Complexity Analysis**

- Time Complexity: O(N)_O_(_N_), where N*N* is the length of `A`.
- Space Complexity: O(1)_O_(1).
