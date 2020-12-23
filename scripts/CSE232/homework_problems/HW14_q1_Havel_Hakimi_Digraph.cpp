/*
Recall Homework 10 problem 1.

In that homework we discussed the Havel-Hakimi algorithm and introduced the concepts of graphs. In this we introduce direction graphs or digraphs. Digraphs are just like regular graphs except each edge also contains a direction: in other words if you have two vertices a and b, just because a is connected to b doesn't necessarily mean b is connected to a.

As a result, we don't just have a degree sequence, each vertex has an in-degree and out-degree. Intuitively, the in-degree is how many edges going into a vertex, an the out-degree is the number of edges leaving the vertex. Note an edge may be leaving and entering at the same time.

We would like to extend Havel-Hakimi to the domain of digraphs. The algorithm is very similar however we consider instead of the degree sequence, a sequence of pairs, where each pair is of the form (a, b), with a being the out-degree and b being the in-degree. This sequence is sorted from largest to smallest by the out-degree first, and then in-degree, so consider the graph above. The sequence will be as follows (clockwise starting upper left).

{(1, 1), (1, 2), (2, 1)}.

If we sort this as described above our sequence becomes {(2, 1), (1, 2), (1, 1)}. The Havel-Hakimi algorithm then sets the out-degree of the first node to 0, whatever number that is, say x, it then subtracts 1 from the next x vertices' in-degree skipping zeros, and then resorts. Again, an empty list results in true, and any list of all 0s results in true. Also again, if the subtraction operation results in 'extra' values not being subtracted (e.g. need to subtract 5 times but the list is only of length 4),that also results in false. An example of the algorithm of the above graph is as follows:

Base case: {(2, 1), (1, 2), (1, 1)}

The out-degree is 2 so after setting the first vertex to 0 we get {(0, 1), (1, 2), (1, 1)}

Subtracting 1 from the next 2 vertices we get: {(0, 1), (1, 1), (1, 0)}

Resort: {(1, 1), (1, 0), (0, 1)}

Repeat the setting of 0, saving the 1: {(0, 1), (1, 0), (0, 1)}

Subtract 1 from the next 1 vertex skipping 0s: {(0, 1), (1, 0), (0, 0)}

Resort: {(1, 0), (0, 1), (0, 0)}

{(0, 0), (0, 1), (0, 0)}

{(0 0), (0, 0), (0, 0)}

Which leads to an all 0 sequence which is trivially true.

For this homework write a function called havel_hakimi_digraph that takes in a vector<pair<int, int>> and then returns whether or not the graph is graphical.
*/

// solution code 

#include <vector>
#include <utility>
#include <string>
#include <algorithm>
#include <exception>
#include <iostream>



void prune(std::vector<std::pair<int, int>> & degree_sequence) {
    std::vector<std::pair<int, int>> result;

    for (auto p: degree_sequence) {
        if (!(p.first == 0 && p.second == 0)) {
            result.push_back(p);
        }
    }

    degree_sequence = result;
}

bool comparator(const std::pair<int, int> & a, const std::pair<int, int> & b) {
    if (a.first > b.first) {
        return true;
    }
    if (a.first == b.first) {
        return a.second > b.second;
    }
    return false;
}

bool check_for_outdegree(const std::vector<std::pair<int, int>> & degree_sequence) {
    for (auto p: degree_sequence) {
        if (p.first > 0) {
            return true;
        }
    }
    return false;
}

bool havel_hakimi_digraph(std::vector<std::pair<int, int>> degree_sequence) {
    std::sort(degree_sequence.begin(), degree_sequence.end(), comparator);
    prune(degree_sequence);

    while(static_cast<int>(degree_sequence.size()) > 0) {
        if (!check_for_outdegree(degree_sequence)) {
            return false;
        }
        int to_remove = degree_sequence.front().first;
        degree_sequence.front().first = 0;
        if (to_remove > static_cast<int>(degree_sequence.size())-1) {
            return false;
        }

        int connected = 0;
        for (int i = 1; i < static_cast<int>(degree_sequence.size()); ++i) {
            if (connected == to_remove) {
                break;
            }
            if (degree_sequence[i].second > 0) {
                degree_sequence[i].second--;
                connected++;
            }
        }

        if (connected != to_remove) {
            return false;
        }

        prune(degree_sequence);
        std::sort(degree_sequence.begin(), degree_sequence.end(), comparator);
    }

    return true;


}
