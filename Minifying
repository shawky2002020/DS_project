/*
 * Name : Mohaned Khaled Hassan'
 * ID   : 2001372
 * Date : 26/12/2023
 */


#include <bits/stdc++.h>

using namespace std;

string compressXML(string &input) {
    string compressed;
    int flag = 1;
    for (int i = 0; i < input.length(); i++) {
        if (input[i] == '<' && input[i + 1] == 'b') {
            flag = 0;
            compressed += "<body>";
            i += 6;
            while (input[i] == ' ' || input[i] == '\t' || input[i] == '\n' || input[i] == '\r') {
                i++;
            }
        }

        if (flag) {
            if (input[i] != ' ' && input[i] != '\t' && input[i] != '\n' && input[i] != '\r')
                compressed += input[i];
        } else {
            if (input[i] != '\n') {
                compressed += input[i];
            }
            else {
                flag = 1;
            }
        }
    }
    return compressed;
}

//Test Minifying Function
int main() {
    string input = "\n"
                   "<users>\n"
                   "    <user>\n"
                   "        <id>1</id>\n"
                   "        <name>Ahmed Ali</name>\n"
                   "        <posts>\n"
                   "            <post>\n"
                   "                <body>\n"
                   "                    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.\n"
                   "                </body>\n"
                   "                <topics>\n"
                   "                    <topic>\n"
                   "                        economy\n"
                   "                    </topic>\n"
                   "                    <topic>\n"
                   "                        finance\n"
                   "                    </topic>\n"
                   "                </topics>\n"
                   "            </post>\n"
                   "            <post>\n"
                   "                <body>\n"
                   "                    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.\n"
                   "                </body>\n"
                   "                <topics>\n"
                   "                    <topic>\n"
                   "                        solar_energy\n"
                   "                    </topic>\n"
                   "                </topics>\n"
                   "            </post>\n"
                   "        </posts>\n"
                   "        <followers>\n"
                   "            <follower>\n"
                   "                <id>2</id>\n"
                   "            </follower>\n"
                   "            <follower>\n"
                   "                <id>3</id>\n"
                   "            </follower>\n"
                   "        </followers>\n"
                   "    </user>\n"
                   "    <user>\n"
                   "        <id>2</id>\n"
                   "        <name>Yasser Ahmed</name>\n"
                   "        <posts>\n"
                   "            <post>\n"
                   "                <body>\n"
                   "                    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.\n"
                   "                </body>\n"
                   "                <topics>\n"
                   "                    <topic>\n"
                   "                        education\n"
                   "                    </topic>\n"
                   "                </topics>\n"
                   "            </post>\n"
                   "        </posts>\n"
                   "        <followers>\n"
                   "            <follower>\n"
                   "                <id>1</id>\n"
                   "            </follower>\n"
                   "        </followers>\n"
                   "    </user>\n"
                   "    <user>\n"
                   "        <id>3</id>\n"
                   "        <name>Mohamed Sherif</name>\n"
                   "        <posts>\n"
                   "            <post>\n"
                   "                <body>\n"
                   "                    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.\n"
                   "                </body>\n"
                   "                <topics>\n"
                   "                    <topic>\n"
                   "                        sports\n"
                   "                    </topic>\n"
                   "                </topics>\n"
                   "            </post>\n"
                   "        </posts>\n"
                   "        <followers>\n"
                   "            <follower>\n"
                   "                <id>1</id>\n"
                   "            </follower>\n"
                   "        </followers>\n"
                   "    </user>\n"
                   "</users>\n"
                   "sample.xml\n"
                   "Displaying sample.xml.";

    cout << compressXML(input);
}
