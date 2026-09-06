import heapq

class ListNode:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next


class ListNodeDouble:
    def __init__(self, val, next = None, back = None):
        self.val = val
        self.next = next
        self.back = back


# Create a linked list from a python list

def createLinkedList(nums):
    if not nums:
        return None
    head = ListNode(nums[0])  # head

    curr_node = head
    for i in range(1, len(nums)):
        new_node = ListNode(nums[i])
        curr_node.next = new_node
        curr_node = new_node

    return head


def createLinkedListDouble(nums):
    if not nums:
        return None
    head = ListNodeDouble(nums[0])  # head

    curr_node = head
    for i in range(1, len(nums)):
        new_node = ListNodeDouble(nums[i], back=curr_node)
        curr_node.next = new_node
        curr_node = new_node
    return head


def traverseLinkedList(nums = None, head = None):
    if not head:
        head = createLinkedList(nums)

    curr_node = head
    while curr_node:
        print(curr_node.val)
        curr_node = curr_node.next


def lengthOfLinkedList(nums):
    head = createLinkedList(nums)
    
    length = 0
    curr_node = head
    while curr_node:
        length += 1
        curr_node = curr_node.next
    return length


def searchElementInLinkedList(nums, elem):
    head = createLinkedList(nums)

    curr_node = head
    while curr_node:
        if curr_node.val == elem:
            return True
        curr_node = curr_node.next
    return False


# Insertion and Deletion

# Deletion

def deleteFirstNode(nums):
    head = createLinkedList(nums)

    if head is None or head.next is None:
        return None

    temp = head
    head = head.next
    del temp

    return head


def deleteLastNode(nums):
    head = createLinkedList(nums)

    if head is None or head.next is None:
        return None

    temp = head
    while temp:
        if temp.next.next is None:
            temp.next = None

        temp = temp.next

    return head


def deleteKthNode(nums, k):
    head = createLinkedList(nums)

    if head is None or head.next is None:
        return None

    if k == 1:
        temp = head
        head = head.next
        del temp

        return head

    temp = head
    counter = 0
    prev_node = None

    while temp:
        counter += 1

        if counter == k:
            prev_node.next = temp.next

        prev_node = temp
        temp = temp.next

    return head


def deleteElemFromNode(nums, elem):
    head = createLinkedList(nums)

    if head is None:
        return None

    if head.val == elem:
        temp = head
        head = head.next
        del temp

        return head

    temp = head
    prev_node = None

    while temp:
        if temp.val == elem:
            prev_node.next = temp.next

        prev_node = temp
        temp = temp.next

    return head


# Insertion

def insertIntoFirstPosition(nums, elem):
    head = createLinkedList(nums)

    if head is None:
        return ListNode(elem)

    temp = head
    head = ListNode(elem, temp)

    return head


def insertIntoLastPosition(nums, elem):
    head = createLinkedList(nums)

    if head is None:
        return ListNode(elem)

    temp = head
    while temp.next:
        temp = temp.next

    temp.next = ListNode(elem)
    return head


def insertIntoKthPosition(nums, elem, k):
    head = createLinkedList(nums)

    if head is None:
        if k == 1:
            return ListNode(k)
        else:
            return None

    if k == 1:
        temp = head
        head = ListNode(elem, temp)
        return head

    temp = head
    counter = 0

    while temp.next:
        counter += 1

        if counter == k-1:
            new_node = ListNode(elem, temp.next)
            temp.next = new_node
            break
        temp = temp.next

    return head


def insertBeforeElem(nums, elem, new_elem):
    head = createLinkedList(nums)

    if head is None:
        return None

    if head.val == elem:
        temp = head
        head = ListNode(new_elem, temp)
        return head

    temp = head

    while temp.next:
        if temp.next.val == elem:
            new_node = ListNode(new_elem, temp.next)
            temp.next = new_node
            break
        temp = temp.next

    return head


# Reverse a linked list

# Iterative approach
def reverseLinkedList(nums):
    # considering we will always be given a valid head
    head = createLinkedList(nums)

    if head.next is None:
        return head

    prev_node, curr_node = None, head

    while curr_node:
        next_node = curr_node.next
        curr_node.next = prev_node
        prev_node = curr_node
        curr_node = next_node

    return prev_node


# Recursive approach
def reverseLinkedListRecursive(head: ListNode):
    # considering we will always be given a valid head

    if head.next is None:
        return head

    new_head = reverseLinkedListRecursive(head.next)

    next_node = head.next
    next_node.next = head
    head.next = None
    return new_head


# Reverse a double linked list

# Iterative approach
def reverseLinkedListDouble(nums):
    # considering we will always be given a valid head
    head = createLinkedListDouble(nums)

    if head.next is None:
        return head

    prev_node, curr_node = None, head

    while curr_node:
        prev_node = curr_node.back
        curr_node.back = curr_node.next
        curr_node.next = prev_node
        curr_node = curr_node.back

    return prev_node.back


# Recursive approach
def reverseLinkedListDoubleRecursive(head: ListNodeDouble):
    # considering we will always be given a valid head

    if head.next is None:
        return head, None

    new_head, prev_node = reverseLinkedListDoubleRecursive(head)

    next_node = head.next
    next_node.next = head
    next_node.back = prev_node
    head.next = None
    head.back = next_node

    return new_head, next_node


# Detect a loop in a linked list

# Using floyd's algorithm
def containsLoop(nums):
    # considering we will always be given a valid head
    def next_node(node):
        return node.next or node

    head = createLinkedList(nums)

    if head.next is None:
        return head

    tortoise = next_node(head)
    hare = next_node(next_node(head))

    while hare != tortoise and hare.next is not None:
        tortoise = next_node(tortoise)
        hare = next_node(next_node(hare))

    return hare.next is not None


# Design browser history
class Browser:
    def __init__(self):
        self.current = None

    def hompage(self, url: str):
        node = ListNodeDouble(url)
        self.current = node

    def visit(self, url: str):
        page = self.current
        node = ListNodeDouble(url, back=self.current)
        page.next = node
        self.current = node

        return self.current

    def forward(self, steps):
        while steps:
            if self.current.next:
                self.current = self.current.next
            else:
                break

            steps -= 1

        return self.current

    def backward(self, steps):
        while steps:
            if self.current.back:
                self.current = self.current.back
            else:
                break
        
            steps -= 1
        
        return self.current


# Leetcode - Problem: 21

def mergeTwoSortedLists(nums1, nums2):
    head1 = createLinkedList(nums1)
    head2 = createLinkedList(nums2)

    t1 = head1
    t2 = head2

    dummy_node = ListNode(-1)
    curr_node = dummy_node

    while t1 and t2:
        if t1.val <= t2.val:
            curr_node.next = t1
            curr_node = t1
            t1 = t1.next
        else:
            curr_node.next = t2
            curr_node = t2
            t2 = t2.next

    if t1:
        curr_node.next = t1
    else:
        curr_node.next = t2

    return dummy_node.next

# Leetcode - Problem: 23

def mergeKsortedLists(lists: list[ListNode]):
    if not lists:
        return

    task_queue = []
    for i in lists:
        if i:
            heapq.heappush(task_queue, (i.val, i))

    if not task_queue:
        return

    dummy_node = ListNode(-1)
    curr_node = dummy_node

    while task_queue:
        _, node = heapq.heappop(task_queue)
        curr_node.next = node
        curr_node = node

        next_node = node.next

        if next_node:
            heapq.heappush(task_queue, (next_node.val, next_node))

    return dummy_node.next


# Find the starting node of a cycle

def cycleStartingNode(nums):
    head = createLinkedList(nums)

    def next_node(node):
        return node.next or node

    tortoise = next_node(head)
    hare = next_node(next_node(head))

    while hare != tortoise and hare.next is not None:
        tortoise = next_node(head)
        hare = next_node(next_node(head))

    if not hare.next:
        return None

    tortoise = head

    while tortoise:
        if tortoise == hare:
            break

        hare = hare.next
        tortoise = tortoise.next
    return tortoise

# Leetcode - Problem: 19

def removeNthNode(nums, n):
    head = createLinkedList(nums)

    fast = head
    for _ in range(n):
        fast = fast.next

    if not fast:
        return head.next

    slow = head
    while fast.next:
        slow = slow.next
        fast = fast.next

    next_node = slow.next
    slow.next = next_node.next

    return head


def findListMiddleNode(nums):
    head = createLinkedList(nums)

    if head is None:
        return

    hare = head
    tortoise = head

    while tortoise and tortoise.next:
        hare = hare.next.next
        tortoise = tortoise.next

    return tortoise

# Leetcode - Problem: 2095

def deleteListMiddleNode(nums):
    head = createLinkedList(nums)

    if head is None or head.next is None:
        return

    tortoise = head
    hare = head.next.next

    while hare and hare.next:
        hare = hare.next.next
        tortoise = tortoise.next

    tortoise.next = tortoise.next.next

    return head


def lengthOfCycle(head):
    def next_node(node):
        return node.next or node

    tortoise = next_node(head)
    hare = next_node(next_node(head))

    while hare != tortoise and hare.next is not None:
        tortoise = next_node(tortoise)
        hare = next_node(next_node(hare))

    if not hare.next:
        return 0

    counter = 1
    tortoise = tortoise.next

    while tortoise != hare:
        counter += 1
        tortoise = tortoise.next
    return counter


# Leetcode - Problem: 2

def addTwoNumbers(head1, head2):
    t1, t2, carry = head1, head2, 0

    dummy_node = ListNode(-1)
    curr_node = dummy_node

    while t1 or t2:
        if not t1.next and t2.next:
            t1.next = ListNode(0)

        if not t2.next and t1.next:
            t2.next = ListNode(0)

        res = t1.val + t2.val + carry

        if res > 9:
            carry, res = res // 10, res % 10
        else:
            carry = 0

        t1.val = int(res)
        curr_node.next = t1
        curr_node = t1

        t1 = t1.next
        t2 = t2.next

    if carry > 0:
        curr_node.next = ListNode(carry)

    return dummy_node.next
