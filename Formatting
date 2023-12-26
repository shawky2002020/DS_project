/* 
 * Name : Mohaned Khaled Hassan
 * ID   : 2001372
 * Date : 26/12/2023
 */

#include <bits/stdc++.h>

using namespace std;

bool hasOpenTag(string &line) {
    size_t pos = line.find('<');
    return pos != string::npos && line[pos + 1] != '/';
}

bool hasCloseTag(string &line) {
    size_t pos = line.find("</");
    return pos != string::npos;
}

string removeLeadingSpaces(string str) {
    // Find the first non-space character
    size_t pos = str.find_first_not_of(' ');

    // Erase leading spaces
    if (pos != string::npos) {
        str.erase(0, pos);
    } else {
        // If the string is all spaces, clear the string
        str.clear();
    }
    return str;
}

string formatting(string &input) {
    string output;
    istringstream iss(input);
    string line;
    int flag = 0;
    int spaces = 0;

    for (int i = 1; i < input.length(); ++i) {
        if (input[i] == '<') {
            if (input[i - 1] != '\n') {
                input.insert(i, "\n");
            }
        }
        if (input[i] == '>') {
            if (input[i + 1] != '\n') {
                input.insert(i + 1, "\n");
            }
        }
    }

    while (getline(iss, line)) {
        int i;
        string newLine = removeLeadingSpaces(line);
        bool hasOpen = hasOpenTag(newLine);
        bool hasClose = hasCloseTag(newLine);
        
        if (hasOpen && hasClose) {
            if (flag == 2) {
                spaces++;
            }
            flag = 3;

        } else if (hasOpen) {
            if (flag == 2) {
                spaces++;
            }
            flag = 2;
        } else if (hasClose) {
            spaces--;
            flag = 1;
        } else {
            if (flag == 2) {
                spaces++;
            }
            flag = 0;
        }

        i = spaces;

        if (i > 0) {
            while (i--) {
                newLine.insert(0, "   ");
            }
        }

        output = output + newLine + "\n";
    }
    return output;
}


//Test Function
int main() {
    string input = "<users><user><id>1</id><name>AhmedAli</name><posts><post><body>Lorem ipsum dolor sit amet, consectetur adipiscing elit,"
                   "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ul"
                   "lamco laboris nisi ut aliquip ex ea commodo consequat.</body><topics><topic>economy</topic><topic>finance</topic></topic"
                   "s></post><post><body>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore"
                   " et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commod"
                   "o consequat.</body><topics><topic>solar_energy</topic></topics></post></posts><followers><follower><id>2</id></follower>"
                   "<follower><id>3</id></follower></followers></user><user><id>2</id><name>YasserAhmed</name><posts><post><body>Lorem ipsum"
                   " dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim"
                   " ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</body><topics><topi"
                   "c>education</topic></topics></post></posts><followers><follower><id>1</id></follower></followers></user><user><id>3</id>"
                   "<name>MohamedSherif</name><posts><post><body>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tem"
                   "por incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi"
                   " ut aliquip ex ea commodo consequat.</body><topics><topic>sports</topic></topics></post></posts><followers><follower><id"
                   ">1</id></follower></followers></user></users>";

    formatting(input);

    cout << formatting(input);

    return 0;
}






//Finish here, the remaining is just comments
//*************************************************************//

/** compensate for loop that at beginning of formatting function but doesn't work correctly yet */
/*
bool hasCloseAndOthers(string &line) {
    size_t pos = line.find("</");
    size_t pos2 = line.find('<');
    return pos != 0 && pos != string::npos && line[pos2 + 1] == '/';
}

bool hasOpenAndOthers(string &line) {
    size_t pos = line.find('<');
    size_t pos2 = line.find('>');
    size_t pos3 = line.find("</");
    return pos3 == string::npos && pos != string::npos && line[pos2 + 1] != '\n';
}

if (hasCloseAndOthers(newLine)) {
    size_t pos = newLine.find("</");
    newLine.insert(pos, "\n");
    size_t posLine2 = newLine.find('\n') + 1;

    i = spaces;
    if (i > 0) {
        while (i--) {
            newLine.insert(posLine2, "   ");
        }
    }

    i = spaces + 1;
    if (i > 0) {
        while (i--) {
            newLine.insert(0, "   ");
        }
    }
    flag = 1;
}
 else if (hasOpenAndOthers(newLine)) {
    size_t pos = newLine.find('>');
    newLine.insert(pos + 1, "\n");
    size_t posLine2 = newLine.find('\n') + 1;

    if (flag == 2) {
        spaces++;
    }

    i = spaces;
    if (i > 0) {
        while (i--) {
            newLine.insert(0, "   ");
        }
    }

    i = spaces + 1;
    if (i > 0) {
        while (i--) {
            newLine.insert(posLine2, "   ");
        }
    }
    flag = 0;
}*/

