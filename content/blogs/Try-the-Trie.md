---
title: "Try the Trie with Py"
date: 2021-06-25T13:00:45-04:00
draft: true
robotsdisallow: true
categories: ["design", "data-structures", "guide", "python"]
---
Trie, such a beautiful N-ary Tree with a purpose. We traverse Nodes based on prefix and return the paths (words) formed by the prefix from the tree. But there was a case that confused for me, the termination of words in the tree.   
Designing the leaf nodes with a bool variable `is_end` was fine for a word *(example: Harry Potter)*, but what if there's another word that embeds the previous word *(example: Harry Potter Movies)*.  
**So let's break pieces and design the Data Structure functionality-wise.**

## Basics
The Trie implementation that we are considering is a raw case, with only considering the application, search complexity but not on the space. There are efficient solutions to reduce the Trie space, which can be read from the [wiki](https://en.wikipedia.org/wiki/Trie).  

* So how is the Trie defined?
* What about the complexity?

## Analysis of the Case
{{<mermaid align="center">}}
graph LR;
    B --> A
    A --> T:::isEnd
    T --> M
    T --> G --> ...
    M --> E
    M --> A1[A]
    A1 --> N:::isEnd
    E --> N
    classDef isEnd fill:#f9f,stroke:#333,stroke-width:4px
{{< /mermaid >}}


## 

## References
* [Trie Implementation - git gist](https://gist.github.com/guhan62/64e60a5f9813e28ee4149496864b60a2)
* [Wiki - Trie](https://en.wikipedia.org/wiki/Trie)
* [GFG - Trie Search|Insert](https://www.geeksforgeeks.org/trie-insert-and-search/)
* [GFG - Trie Usage](https://www.geeksforgeeks.org/advantages-trie-data-structure/)