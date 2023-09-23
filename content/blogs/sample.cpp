#include <bits/stdc++.h>
using namespace std;

struct menuItem {
    float price;
    string item;
    string store;
    // 0 -> Free Customer, 1 -> Pro Customer, 2 -> Super Pro Customer
    int priority;
    menuItem(string store, string item, float price) : store(store), price(price), item(item), priority(0) {}
    menuItem(string store, string item, float price,int priority) : store(store), price(price), item(item), priority(priority) {}
    // Less Price
    bool operator < (const menuItem& item) const { return item.price < price; }
};

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
int main() {
    priority_queue<menuItem, vector<menuItem>, less<menuItem>> min_price_Q;
    priority_queue<menuItem, vector<menuItem>, premiumOrdering> top_partner_Q;
    
    menuItem item1("Tandoori Globe","Chicken Briyani", 14.99), item2("Tandoori Globe","Mutton Briyani", 18.99), \
    item3("Pot Mirchi","Chicken Briyani", 16.99, 1), item4("Pot Mirchi","Mutton Briyani", 14.99, 1), item5("Briyani Dome", "Chickem Briyani", 19.99, 2);

    min_price_Q.push(item1), min_price_Q.push(item2), min_price_Q.push(item3), min_price_Q.push(item4), min_price_Q.push(item5);
    top_partner_Q.push(item1), top_partner_Q.push(item2), top_partner_Q.push(item3), top_partner_Q.push(item4), top_partner_Q.push(item5);

    while(!min_price_Q.empty()) {
        auto mt = min_price_Q.top();
        cout << mt.store << " " << mt.item << " " << mt.price << " " << mt.priority << "\n";
        min_price_Q.pop();
    }
    cout<<"\n";
    while(!top_partner_Q.empty()) {
        auto mt = top_partner_Q.top();
        cout << mt.store << " " << mt.item << " " << mt.price << " " << mt.priority << "\n";
        top_partner_Q.pop();
    }
    return 0;
}