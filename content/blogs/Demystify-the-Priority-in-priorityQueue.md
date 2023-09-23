---
title: "Demystify the Priority in PriorityQueue"
date: 2021-05-27T18:41:18-04:00
draft: false
robotsdisallow: true
categories: ["C++", "guide"]
---
## Introduction
Priority Queue, STL Container in C++ helps in working with Heap Data Structure to access elements based on Priority. Refer the References section below, to learn more about the Heaps & Priority Queue. In this post we will see examples and tricks that is useful when workin with priority Queues.  
**What do we Demystify?** The Compare Functions! and the custom Type T! - This is an useful starterpack for you to work directly on priorityQ ~ (I will address them as **pQ** from now!)  
  
```C++
template<class T, 
class Container = std::vector<T>, 
class Compare = std::less<typename Container::value_type>>
class priority_queue;
```  

## A General Use-Case
In a `Queue` Data Structure has a FIFO (First-in First-out) technique on pushing, popping elements. What if we need the Queue, to have an ordering such that the element is either the `least/largest` you need at that moment get's returned.  

Assume, we have menu items from 10 Restaraunts and more items get added each minute that passes, I want to find the cheapest item on the Menu, at any moment. Just Sort the entries, each time and get the cheapest item. Simple, right? but what if there are millions of items, then sort each time is expensive on insert.  

* What if the `Queue` is able to balance itself?  
* How about giving priority for `OliveGarden`, because they pay premium for our platform?   
*I do not endorse them* :sweat_smile:  

So `priority_queue` uses heap operations to give as acceptable and cheap runtimes for such problems!  

{{< highlight c "linenos=inline,hl_lines=1-3">}}
priority_queue<int> pQ;
// = priority_queue<int, vector<int>> pQ;
// = priority_queue<int, vector<int>, greater<int>> pQ;
vector<int> sample = {1,10,-1,3,8};
// Push 1 10 -1 3 8
for(int &i:sample) {
    pQ.push(i);
}
// Pops 10 8 3 1 -1
while(!pQ.empty()) {
    cout << pQ.top() << " ";
    pQ.pop();
}
{{< /highlight >}}  

* **Line 1-3** : Show the same syntax but abstracted by default by C++  
* for a `min_heap` we can use `std::lesser<int>` in our comparator

But we need more, not a simple max/min `heap` -> let's demystify another layer from the priority_queue!

## Priority Kitchen
Let's define a user-defined type with a custom ordering as a member function where the `operator <` or `operator >` can be overloaded to have defined ordering on our struct!  
Here the `menuItem` structure has an `operator<` that allows for `<`
``` c++
struct menuItem {
    float price;
    string item;
    string store;
    // 0 -> Free Customer, 1 -> Pro Customer, 2 -> Super Pro Customer
    // Customer as in Subscribed Restaraunteer
    int priority;
    menuItem(string store, string item, float price) : \
        store(store), price(price), item(item), priority(0) {}
    menuItem(string store, string item, float price,int priority) : \
        store(store), price(price), item(item), priority(priority) {}
    // Less Price
    bool operator < (const menuItem& item) const { return item.price < price; }
};
```
Now defining function objects to priority Queue. This premium ordering compares both price & priority.
```C++
struct premiumOrdering {
    // Items sorted by Price - Min
    bool operator() (struct menuItem& item1, struct menuItem& item2) {
        // When Price is Lower, push, the top priority customer on top
        if (item1.price < item2.price) {
            return item1.priority > item2.priority;
        }
        else {
            return item1.priority < item2.priority;
        }
    }
};
```
Now let's define the Queues and see an example.
```c++
priority_queue<menuItem, vector<menuItem>, less<menuItem>> min_price_Q;
priority_queue<menuItem, vector<menuItem>, premiumOrdering> top_partner_Q;
```

Shall we see the beautiful output, that our system generates on popping!
```c++
// Items Ordered by their pricing using the `less<menuItem>` custom compare<T>
// overloaded as a member function in the struct
Tandoori Globe Chicken Briyani 14.99 0
Pot Mirchi Mutton Briyani 14.99 1
Pot Mirchi Chicken Briyani 16.99 1
Tandoori Globe Mutton Briyani 18.99 0
Briyani Dome Chickem Briyani 19.99 2

// Items Ordered by their pricing & an addition priority variable using the compare object
Pot Mirchi Mutton Briyani 14.99 1
Pot Mirchi Chicken Briyani 16.99 1
Briyani Dome Chickem Briyani 19.99 2
Tandoori Globe Chicken Briyani 14.99 0
Tandoori Globe Mutton Briyani 18.99 0
```

Now Reader<T> go ahead and solve this LeetCode question, [Single Threaded CPU](https://leetcode.com/problems/single-threaded-cpu/) also refer to my [LC Discussion Post](https://leetcode.com/problems/single-threaded-cpu/discuss/1165656/C%2B%2B-or-The-Inefficient-Single-Threaded-CPU-or-600ms-151MB), regarding hints on this problem.



## References
* [C++ Reference Doc for priorityQ](https://en.cppreference.com/w/cpp/container/priority_queue)
* [HE Notes on Heap](https://www.hackerearth.com/practice/notes/heaps-and-priority-queues/)
* [YT: Weak, Linear Ordering Principle](https://www.youtube.com/watch?v=GWgobwdUCtE)