class Solution {
public:

string intToString(int elements) {
  string result = "";
  if (elements < 10) {
    result = "00" + to_string(elements);
  } else if (elements < 99) {
    result = "0" + to_string(elements);
  } else {
    result = to_string(elements);
  }
  return result;
}

string encode(vector<string> &strs) {
  int elements = strs.size();
  string result = intToString(elements);
  string words = "";
  for (const string &str : strs) {
    result += intToString(str.length());
    words += str;
  }
  return result + words;
}

vector<string> decode(string s) {
  int words = stoi(s.substr(0, 3));
  int wordLengthStart = 3;
  int wordStart = 3 + (3 * words);
  vector<string> result;
  for (int x = 0; x < words; x++) {
    int wordLength = stoi(s.substr(wordLengthStart, 3));
    string word = s.substr(wordStart, wordLength);
    result.push_back(word);
    wordLengthStart = wordLengthStart + 3;
    wordStart += wordLength;
  }
  return result;
}
};
