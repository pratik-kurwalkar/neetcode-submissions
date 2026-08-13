class Solution {
public:
    bool isPalindrome(string s) {
        int ptr1 = 0;
        int ptr2 = s.length()-1;
        while(ptr1 < ptr2) {
            if (isalnum(s[ptr1])) {
                if (isalnum(s[ptr2])) {
                    // cout << "comparing " << tolower(s[ptr1]) << " and " << tolower(s[ptr2]) << endl;
                    if (tolower(s[ptr1])==tolower(s[ptr2])) {
                        ptr2--;
                        ptr1++;
                    } else {
                        return false;
                    }
                } else {
                    ptr2--;
                }
            } else {
                ptr1++;
            }
        }
        return true;
    }
};
