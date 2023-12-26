#include <iostream>
#include <string>
#include <stack>
#include <vector>
#include <sstream>
#include <map>

struct Node {
    std::string name;
    std::string content;
    std::vector<Node> children;

    Node() = default;
    explicit Node(std::string n) : name(std::move(n)) {}

    void addChild(const Node& node) {
        children.push_back(node);
    }

    bool isLeaf() const {
        return children.empty();
    }

    std::string repeat(const std::string& str, int times) const {
        std::string result;
        for (int i = 0; i < times; ++i) {
            result += str;
        }
        return result;
    }

    std::string toJSON(int indent = 0) const {
        std::stringstream ss;

        // Wrap the whole structure in the root name if it's the root node
        if (indent == 0 && !name.empty()) {
            indent += 1;
            ss <<  "{\n" <<  repeat("  ", indent)  << "\"" << name << "\": ";
        }

        if (isLeaf()) {
            ss << "\"" << content << "\"";
        } else {
            if (!isLeaf()) ss << "{\n"; // Begin object notation for non-leaf

            std::map<std::string, std::vector<Node>> groupedChildren;
            for (const auto& child : children) {
                groupedChildren[child.name].push_back(child);
            }

            for (auto it = groupedChildren.begin(); it != groupedChildren.end(); ++it) {
                if (it->second.size() == 1) {
                    ss << repeat("  ", indent + 1) << "\"" << it->first << "\": " << it->second[0].toJSON(indent + 1);
                } else {
                    ss << repeat("  ", indent + 1) << "\"" << it->first << "\": [\n";
                    for (size_t i = 0; i < it->second.size(); ++i) {
                        ss << repeat("  ", indent + 2) << it->second[i].toJSON(indent + 2);
                        if (i < it->second.size() - 1) ss << ",";
                        ss << "\n";
                    }
                    ss << repeat("  ", indent + 1) << "]";
                }
                ss << (std::next(it) == groupedChildren.end() ? "\n" : ",\n");
            }

            if (!isLeaf()) ss << repeat("  ", indent) << "}"; // End object notation for non-leaf
        }

        if (indent == 1 && !name.empty()) {
            ss << "\n}"; 
        }

        return ss.str();
    }
};

Node parseXML(const std::string& xml) {
    std::stack<Node> stack;
    std::string temp;
    Node root;
    bool isTag = false;

    for (char ch : xml) {
        if (ch == '<') {
            if (!temp.empty()) {
                size_t start = temp.find_first_not_of(" \n\r\t");
                size_t end = temp.find_last_not_of(" \n\r\t");
                if (start != std::string::npos && end != std::string::npos)
                    stack.top().content = temp.substr(start, end - start + 1);
                temp.clear();
            }
            isTag = true;
        } else if (ch == '>') {
            if (!stack.empty() && temp[0] == '/') {
                Node completedNode = stack.top();
                stack.pop();
                if (stack.empty()) {
                    root = completedNode;
                } else {
                    stack.top().addChild(completedNode);
                }
            } else {
                stack.push(Node(temp));
            }
            temp.clear();
            isTag = false;
        } else if (!isTag && ch == '\n') {
            continue;
        } else {
            temp += ch;
        }
    }
    return root;
}